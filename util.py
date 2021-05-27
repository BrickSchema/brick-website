import json
from collections import defaultdict

from rdflib import Graph, URIRef, RDFS, query

from rdflib.term import BNode

auto_dict = lambda: defaultdict(auto_dict)
import os


def minify(iri):
    # Note: Some IRIs might not have a '#'.
    if type(iri) == query.ResultRow:
        iri = iri[0]
    iri = str(iri)
    return iri.split("/")[-1].split("#")[-1]


def get_ns(iri):
    # Note: Some IRIs might not have a '#'.
    if type(iri) == query.ResultRow:
        iri = iri[0]
    iri = str(iri)
    path_blocks = iri.split("/")
    last = path_blocks[-1]
    if "#" in last:
        path_blocks[-1] = "#".join(last.split("#")[:-1])
        return "/".join(path_blocks) + "#"
    else:
        return "/".join(path_blocks[:-1]) + "/"


def get_alias(iri):
    minified = minify(iri)
    alias = ""
    for letter in minified:
        if letter <= "Z":
            alias += letter
    return alias


def get_shacl_details(graph, shape):
    shacl_details = {}
    q = """SELECT ?propname ?enum {
        <%s> sh:property ?prop .
        ?prop sh:path ?propname .
        ?prop sh:in/rdf:rest*/rdf:first ?enum .
    }"""%(shape)
    for row in graph.query(q):
        propname = str(row[0])
        enum = str(row[1])
        if propname not in shacl_details:
            shacl_details[propname] = {"http://www.w3.org/ns/shacl#in": list()}
        shacl_details[propname]["http://www.w3.org/ns/shacl#in"].append(enum)

    q = """SELECT ?propname ?datatype {
        <%s> sh:property ?prop .
        ?prop sh:path ?propname .
        ?prop sh:datatype ?datatype .
    }"""%(shape)
    for row in graph.query(q):
        propname = str(row[0])
        datatype = str(row[1])
        if propname not in shacl_details:
            shacl_details[propname] = {"http://www.w3.org/ns/shacl#datatype": list()}
        shacl_details[propname]["http://www.w3.org/ns/shacl#datatype"].append(datatype)
    return json.dumps(shacl_details)


def generate_doc_src(doc_spec):
    all_classes = []
    all_relationships = []
    all_entity_properties = []
    all_shapes = []
    all_namespaces = []


    for version in doc_spec:
        print(f"[ ] Brick v{version}...", end="\r")
        g = Graph()

        for directory in doc_spec[version]["input"]:
            for root, dirs, files in os.walk(directory):
                if root != directory:
                    continue
                for file in files:
                    if file.endswith(".ttl"):
                        g.parse(os.path.join(*[directory, file]), format="turtle")
        visited = set()

        ns_restriction_str = lambda var: "||".join(
            [
                f'STRSTARTS( STR({var}), "{ns}" )'
                for ns in doc_spec[version]["ns_restriction"]
            ]
        )

        # Classes
        classes = []
        class_tree = {"name": f"/ontology/{version}/#Classes", "children": []}
        root_classes = g.query(
            """SELECT ?iri WHERE {
             ?iri a owl:Class .
             FILTER NOT EXISTS {
                ?iri rdfs:subClassOf ?something .
                FILTER ( %s )
             }
         }"""
            % (ns_restriction_str("?something"))
        )
        for iri in root_classes:
            if type(iri[0]) is not BNode:
                class_tree["children"].append({"iri": iri[0]})

        def get_class_details(iri, hierarchy=[]):
            return {
                "id": f"{version}^{iri}",
                "version": version,
                "namespace": f"{version}^{get_ns(iri)}",
                "type": "class",
                "types": [
                    f"{instance_type[0]}"
                    for instance_type in g.query(
                        f"SELECT DISTINCT ?instance_type WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/a ?instance_type . }}"
                    )
                ],
                "name": minify(iri),
                "path": f"/ontology/{version}/classes/{minify(iri)}",
                "labels": [
                    label[0]
                    for label in g.query(
                        f"SELECT DISTINCT ?label WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/rdfs:label ?label . }}"
                    )
                ],
                "generatedLabel": " ".join(minify(iri).split("_")),
                "generatedAlias": get_alias(iri),
                "superclasses": [
                    f"{version}^{superclass[0]}"
                    for superclass in g.query(
                        f"SELECT DISTINCT ?superclass WHERE {{ <{iri}> rdfs:subClassOf/(owl:equivalentClass|^owl:equivalentClass)* ?superclass . }}"
                    )
                ],
                "subclasses": [
                    f"{version}^{subclass[0]}"
                    for subclass in g.query(
                        f"SELECT DISTINCT ?subclass WHERE {{ ?subclass (owl:equivalentClass|^owl:equivalentClass)*/rdfs:subClassOf <{iri}> . }}"
                    )
                ],
                "comments": [
                    comment[0]
                    for comment in g.query(
                        f"SELECT DISTINCT ?comment WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/rdfs:comment ?comment . }}"
                    )
                ],
                "definitions": [
                    definition[0]
                    for definition in g.query(
                        f"SELECT DISTINCT ?definition WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/skos:definition ?definition . }}"
                    )
                ],
                "equivalentClasses": [
                    f"{version}^{klass[0]}"
                    for klass in g.query(
                        f"SELECT DISTINCT ?klass WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)* ?klass . FILTER (?klass != <{iri}>) . }}"
                    )
                ],
                "hierarchy": hierarchy,
                "inRangeOf": [
                    f"{version}^{relationship[0]}"
                    for relationship in g.query(
                        f"SELECT DISTINCT ?relationship WHERE {{ ?relationship rdfs:range ?range_class . <{iri}> (owl:equivalentClass|^owl:equivalentClass|rdfs:subClassOf)* ?range_class. }}"
                    )
                ],
                "inDomainOf": [
                    f"{version}^{relationship[0]}"
                    for relationship in g.query(
                        f"SELECT DISTINCT ?relationship WHERE {{ ?relationship rdfs:domain ?domain_class . <{iri}> (owl:equivalentClass|^owl:equivalentClass|rdfs:subClassOf)* ?domain_class. }}"
                    )
                ],
                "shaclDetails": get_shacl_details(g, iri),
            }

        def expand_class_tree(brick_classes, hierarchy=[]):
            for brick_class in brick_classes:
                iri = brick_class["iri"]
                del brick_class["iri"]
                brick_class["name"] = f"/ontology/{version}/classes/{minify(iri)}"
                brick_class["children"] = []
                classes.append(
                    get_class_details(iri, hierarchy + [brick_class["name"]])
                )
                if iri not in visited:
                    brick_class["children"] = [
                        {"iri": str(klass)}
                        for klass in g.subjects(
                            predicate=RDFS.subClassOf, object=URIRef(iri)
                        )
                    ]
                    brick_class["children"] = sorted(
                        brick_class["children"], key=lambda x: minify(x["iri"])
                    )
                    visited.add(iri)
                    expand_class_tree(
                        brick_class["children"], hierarchy + [brick_class["name"]]
                    )

        class_tree["children"] = sorted(
            class_tree["children"], key=lambda x: minify(x["iri"])
        )
        expand_class_tree(class_tree["children"], [class_tree["name"]])

        # Relationships
        relationships = []
        relationship_tree = {
            "name": f"/ontology/{version}/#Relationships",
            "children": [],
        }
        root_relationships = g.query(
            """SELECT ?iri WHERE {
             ?iri a owl:ObjectProperty .
             FILTER NOT EXISTS {
                ?iri rdfs:subPropertyOf ?something .
                FILTER ( %s )
             }
         }"""
            % (ns_restriction_str("?something"))
        )
        for iri in root_relationships:
            relationship_tree["children"].append({"iri": iri[0]})

        def get_relationship_details(iri, hierarchy=[]):
            return {
                "id": f"{version}^{iri}",
                "version": version,
                "namespace": f"{version}^{get_ns(iri)}",
                "type": "relationship",
                "types": [
                    f"{instance_type[0]}"
                    for instance_type in g.query(
                        f"SELECT DISTINCT ?instance_type WHERE {{ <{iri}> a ?instance_type . }}"
                    )
                ],
                "name": minify(iri),
                "path": f"/ontology/{version}/relationships/{minify(iri)}",
                "labels": [
                    label[0]
                    for label in g.query(
                        f"SELECT DISTINCT ?label WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/rdfs:label ?label . }}"
                    )
                ],
                "generatedLabel": " ".join(minify(iri).split("_")),
                "generatedAlias": get_alias(iri),
                "superProperties": [
                    f"{version}^{superproperty[0]}"
                    for superproperty in g.query(
                        f"SELECT DISTINCT ?superproperty WHERE {{ <{iri}> rdfs:subPropertyOf ?superproperty . }}"
                    )
                ],
                "subProperties": [
                    f"{version}^{subproperty[0]}"
                    for subproperty in g.query(
                        f"SELECT DISTINCT ?subproperty WHERE {{ ?subproperty rdfs:subPropertyOf <{iri}> . }}"
                    )
                ],
                "comments": [
                    comment[0]
                    for comment in g.query(
                        f"SELECT DISTINCT ?comment WHERE {{ <{iri}> rdfs:comment ?comment . }}"
                    )
                ],
                "definitions": [
                    definition[0]
                    for definition in g.query(
                        f"SELECT DISTINCT ?definition WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/skos:definition ?definition . }}"
                    )
                ],
                "equivalentClasses": [
                    f"{version}^{klass[0]}"
                    for klass in g.query(
                        f"SELECT DISTINCT ?klass WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)* ?klass . }}"
                    )
                ],
                "inverseProperties": [
                    f"{version}^{relationship[0]}"
                    for relationship in g.query(
                        f"SELECT DISTINCT ?relationship WHERE {{ <{iri}> (owl:inverseOf|^owl:inverseOf) ?relationship . }}"
                    )
                ],
                "hierarchy": hierarchy,
                "range": [
                    f"{version}^{klass[0]}"
                    for klass in g.query(
                        f"SELECT DISTINCT ?klass WHERE {{ <{iri}> rdfs:range/(owl:equivalentClass|^owl:equivalentClass)* ?klass . }}"
                    )
                ],
                "domain": [
                    f"{version}^{klass[0]}"
                    for klass in g.query(
                        f"SELECT DISTINCT ?klass WHERE {{ <{iri}> rdfs:domain/(owl:equivalentClass|^owl:equivalentClass)* ?klass . }}"
                    )
                ],
            }

        def expand_relationship_tree(brick_relationships, hierarchy=[]):
            for brick_relationship in brick_relationships:
                iri = brick_relationship["iri"]
                del brick_relationship["iri"]
                brick_relationship[
                    "name"
                ] = f"/ontology/{version}/relationships/{minify(iri)}"
                brick_relationship["children"] = []
                relationships.append(
                    get_relationship_details(
                        iri, hierarchy + [brick_relationship["name"]]
                    )
                )
                if iri not in visited:
                    brick_relationship["children"] = [
                        {"iri": str(klass)}
                        for klass in g.subjects(
                            predicate=RDFS.subPropertyOf, object=URIRef(iri)
                        )
                    ]
                    brick_relationship["children"] = sorted(
                        brick_relationship["children"], key=lambda x: minify(x["iri"])
                    )
                    visited.add(iri)
                    expand_relationship_tree(
                        brick_relationship["children"],
                        hierarchy + [brick_relationship["name"]],
                    )

        relationship_tree["children"] = sorted(
            relationship_tree["children"], key=lambda x: minify(x["iri"])
        )
        expand_relationship_tree(
            relationship_tree["children"], [relationship_tree["name"]]
        )

        # EntityProperties
        entity_properties = []
        entity_property_tree = {
            "name": f"/ontology/{version}/#EntityProperties",
            "children": [],
        }
        root_entity_properties = g.query(
            """SELECT ?iri WHERE {
             ?iri a brick:EntityProperty .
             FILTER NOT EXISTS {
                ?iri rdfs:subPropertyOf ?something .
                FILTER ( %s )
             }
         }"""
            % (ns_restriction_str("?something"))
        )
        for iri in root_entity_properties:
            entity_property_tree["children"].append({"iri": iri[0]})

        def get_entity_property_details(iri, hierarchy=[]):
            return {
                "id": f"{version}^{iri}",
                "version": version,
                "namespace": f"{version}^{get_ns(iri)}",
                "type": "entity_property",
                "types": [
                    f"{instance_type[0]}"
                    for instance_type in g.query(
                        f"SELECT DISTINCT ?instance_type WHERE {{ <{iri}> a ?instance_type . }}"
                    )
                ],
                "name": minify(iri),
                "path": f"/ontology/{version}/entity_properties/{minify(iri)}",
                "labels": [
                    label[0]
                    for label in g.query(
                        f"SELECT DISTINCT ?label WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/rdfs:label ?label . }}"
                    )
                ],
                "generatedLabel": " ".join(minify(iri).split("_")),
                "generatedAlias": get_alias(iri),
                "superProperties": [
                    f"{version}^{superproperty[0]}"
                    for superproperty in g.query(
                        f"SELECT DISTINCT ?superproperty WHERE {{ <{iri}> rdfs:subPropertyOf ?superproperty . }}"
                    )
                ],
                "subProperties": [
                    f"{version}^{subproperty[0]}"
                    for subproperty in g.query(
                        f"SELECT DISTINCT ?subproperty WHERE {{ ?subproperty rdfs:subPropertyOf <{iri}> . }}"
                    )
                ],
                "comments": [
                    comment[0]
                    for comment in g.query(
                        f"SELECT DISTINCT ?comment WHERE {{ <{iri}> rdfs:comment ?comment . }}"
                    )
                ],
                "definitions": [
                    definition[0]
                    for definition in g.query(
                        f"SELECT DISTINCT ?definition WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/skos:definition ?definition . }}"
                    )
                ],
                "equivalentClasses": [
                    f"{version}^{klass[0]}"
                    for klass in g.query(
                        f"SELECT DISTINCT ?klass WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)* ?klass . }}"
                    )
                ],
                "inverseProperties": [
                    f"{version}^{entity_property[0]}"
                    for entity_property in g.query(
                        f"SELECT DISTINCT ?entity_property WHERE {{ <{iri}> (owl:inverseOf|^owl:inverseOf) ?entity_property . }}"
                    )
                ],
                "hierarchy": hierarchy,
                "range": [
                    f"{version}^{klass[0]}"
                    for klass in g.query(
                        f"SELECT DISTINCT ?klass WHERE {{ <{iri}> rdfs:range/(owl:equivalentClass|^owl:equivalentClass)* ?klass . }}"
                    )
                ],
                "domain": [
                    f"{version}^{klass[0]}"
                    for klass in g.query(
                        f"SELECT DISTINCT ?klass WHERE {{ <{iri}> rdfs:domain/(owl:equivalentClass|^owl:equivalentClass)* ?klass . }}"
                    )
                ],
            }

        def expand_entity_property_tree(brick_entity_properties, hierarchy=[]):
            for brick_entity_property in brick_entity_properties:
                iri = brick_entity_property["iri"]
                del brick_entity_property["iri"]
                brick_entity_property[
                    "name"
                ] = f"/ontology/{version}/entity_properties/{minify(iri)}"
                brick_entity_property["children"] = []
                entity_properties.append(
                    get_entity_property_details(
                        iri, hierarchy + [brick_entity_property["name"]]
                    )
                )
                if iri not in visited:
                    brick_entity_property["children"] = [
                        {"iri": str(klass)}
                        for klass in g.subjects(
                            predicate=RDFS.subPropertyOf, object=URIRef(iri)
                        )
                    ]
                    brick_entity_property["children"] = sorted(
                        brick_entity_property["children"], key=lambda x: minify(x["iri"])
                    )
                    visited.add(iri)
                    expand_entity_property_tree(
                        brick_entity_property["children"],
                        hierarchy + [brick_entity_property["name"]],
                    )

        entity_property_tree["children"] = sorted(
            entity_property_tree["children"], key=lambda x: minify(x["iri"])
        )
        expand_entity_property_tree(
            entity_property_tree["children"], [entity_property_tree["name"]]
        )

        # Shapes
        shapes = []
        if version >= "1.2":
            shape_tree = {"name": f"/ontology/{version}/#Shapes", "children": []}
            root_shapes = g.query(
                """SELECT ?iri WHERE {
                 ?iri a sh:NodeShape .
                 FILTER NOT EXISTS {
                    ?iri rdfs:subClassOf ?something .
                    FILTER ( %s )
                 }
             }"""
                % (ns_restriction_str("?something"))
            )
            for iri in root_shapes:
                shape_tree["children"].append({"iri": iri[0]})

            def get_shape_details(iri, hierarchy=[]):
                return {
                    "id": f"{version}^{iri}",
                    "version": version,
                    "namespace": f"{version}^{get_ns(iri)}",
                    "type": "shape",
                    "types": [
                        f"{instance_type[0]}"
                        for instance_type in g.query(
                            f"SELECT DISTINCT ?instance_type WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/a ?instance_type . }}"
                        )
                    ],
                    "name": minify(iri),
                    "path": f"/ontology/{version}/shapes/{minify(iri)}",
                    "labels": [
                        label[0]
                        for label in g.query(
                            f"SELECT DISTINCT ?label WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/rdfs:label ?label . }}"
                        )
                    ],
                    "generatedLabel": " ".join(minify(iri).split("_")),
                    "generatedAlias": get_alias(iri),
                    "supershapes": [
                        f"{version}^{supershape[0]}"
                        for supershape in g.query(
                            f"SELECT DISTINCT ?supershape WHERE {{ <{iri}> rdfs:subClassOf/(owl:equivalentClass|^owl:equivalentClass)* ?supershape . }}"
                        )
                    ],
                    "subshapes": [
                        f"{version}^{subshape[0]}"
                        for subshape in g.query(
                            f"SELECT DISTINCT ?subshape WHERE {{ ?subshape (owl:equivalentClass|^owl:equivalentClass)*/rdfs:subClassOf <{iri}> . }}"
                        )
                    ],
                    "comments": [
                        comment[0]
                        for comment in g.query(
                            f"SELECT DISTINCT ?comment WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/rdfs:comment ?comment . }}"
                        )
                    ],
                    "definitions": [
                        definition[0]
                        for definition in g.query(
                            f"SELECT DISTINCT ?definition WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)*/skos:definition ?definition . }}"
                        )
                    ],
                    "equivalentClasses": [
                        f"{version}^{klass[0]}"
                        for klass in g.query(
                            f"SELECT DISTINCT ?klass WHERE {{ <{iri}> (owl:equivalentClass|^owl:equivalentClass)* ?klass . FILTER (?klass != <{iri}>) . }}"
                        )
                    ],
                    "hierarchy": hierarchy,
                    "inRangeOf": [
                        f"{version}^{relationship[0]}"
                        for relationship in g.query(
                            f"SELECT DISTINCT ?relationship WHERE {{ ?relationship rdfs:range ?range_shape . <{iri}> (owl:equivalentClass|^owl:equivalentClass|rdfs:subClassOf)* ?range_shape. }}"
                        )
                    ],
                    "inDomainOf": [
                        f"{version}^{relationship[0]}"
                        for relationship in g.query(
                            f"SELECT DISTINCT ?relationship WHERE {{ ?relationship rdfs:domain ?domain_shape . <{iri}> (owl:equivalentClass|^owl:equivalentClass|rdfs:subClassOf)* ?domain_shape. }}"
                        )
                    ],
                    "shaclDetails": get_shacl_details(g, iri),
                }

            def expand_shape_tree(brick_shapes, hierarchy=[]):
                for brick_shape in brick_shapes:
                    iri = brick_shape["iri"]
                    del brick_shape["iri"]
                    brick_shape["name"] = f"/ontology/{version}/shapes/{minify(iri)}"
                    brick_shape["children"] = []
                    shapes.append(
                        get_shape_details(iri, hierarchy + [brick_shape["name"]])
                    )
                    if iri not in visited:
                        brick_shape["children"] = [
                            {"iri": str(klass)}
                            for klass in g.subjects(
                                predicate=RDFS.subClassOf, object=URIRef(iri)
                            )
                        ]
                        brick_shape["children"] = sorted(
                            brick_shape["children"], key=lambda x: minify(x["iri"])
                        )
                        visited.add(iri)
                        expand_shape_tree(
                            brick_shape["children"], hierarchy + [brick_shape["name"]]
                        )

            shape_tree["children"] = sorted(
                shape_tree["children"], key=lambda x: minify(x["iri"])
            )
            expand_shape_tree(shape_tree["children"], [shape_tree["name"]])

        # Namespaces
        namespaces = []
        for prefix, namespace in g.namespaces():
            namespaces.append(
                {
                    "id": f"{version}^{namespace}",
                    "type": "namespace",
                    "version": version,
                    "value": prefix,
                    "path": f"/ontology/{version}/namespaces/{prefix}",
                    "labels": [],
                    "generatedLabel": minify(namespace),
                    "generatedAlias": get_alias(namespace),
                    "comments": [],
                }
            )

        all_classes += classes
        all_relationships += relationships
        all_entity_properties += entity_properties
        all_shapes += shapes
        all_namespaces += namespaces

        tree = [class_tree, relationship_tree]

        if entity_properties:
            tree.append(entity_property_tree)

        if version >= "1.2" and shapes:
            tree.append(shape_tree)

        directory = f"./static/ontology/{version}"
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(f"{directory}/tree.json", "w") as file:
            json.dump(tree, file)
        with open(f"{directory}/classes.json", "w") as file:
            json.dump(classes, file)
        with open(f"{directory}/relationships.json", "w") as file:
            json.dump(relationships, file)
        with open(f"{directory}/entity_properties.json", "w") as file:
            json.dump(entity_properties, file)
        with open(f"{directory}/shapes.json", "w") as file:
            json.dump(shapes, file)
        with open(f"{directory}/namespaces.json", "w") as file:
            json.dump(namespaces, file)

        # Search index
        search = []
        for item in relationships + classes + entity_properties + shapes:
            search.append(
                {
                    "generatedAlias": item["generatedAlias"],
                    "generatedLabel": item["generatedLabel"],
                    "definitions": item["definitions"],
                    "type": item["type"],
                    "path": item["path"],
                    "version": item["version"],
                    "namespace": item["namespace"].split("^")[-1],
                }
            )
        with open(f"{directory}/search.json", "w") as file:
            json.dump(search, file)

        print(f"[✓] Brick v{version}   ")

    print(f"[ ] Saving JSON files...", end="\r")
    with open("./static/ontology/all_classes.json", "w") as file:
        json.dump(all_classes, file)
    with open("./static/ontology/all_relationships.json", "w") as file:
        json.dump(all_relationships, file)
    with open("./static/ontology/all_entity_properties.json", "w") as file:
        json.dump(all_entity_properties, file)
    with open("./static/ontology/all_shapes.json", "w") as file:
        json.dump(all_shapes, file)
    with open("./static/ontology/all_namespaces.json", "w") as file:
        json.dump(all_namespaces, file)
    print(f"[✓] Saving JSON files   ")