// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const fs = require("fs");
const path = require("path");
const pick = require("lodash.pick");
const brickClasses = require("./static/ontology/all_classes.json");
const brickRelationships = require("./static/ontology/all_relationships.json");
const brickEntityProperties = require("./static/ontology/all_entity_properties.json");
const brickShapes = require("./static/ontology/all_shapes.json");
const brickNamespaces = require("./static/ontology/all_namespaces.json");
const { pathPrefix } = require("./gridsome.config");
const cacheVersion = new Date().getTime();

module.exports = function (api, options) {
    api.loadSource((store) => {
        /*
                Clean the pathPrefix
                ====================
                not used =>  '/'
                ''       =>  '/'
                '/'      =>  '/'
                '/path'  =>  '/path'
                'path'   =>  '/path'
                'path/'  =>  '/path'
                '/path/' =>  '/path'
                */
        const cleanedPathPrefix = `${
            pathPrefix
                ? ["", ...pathPrefix.split("/").filter((dir) => dir.length)].join("/")
                : ""
        }`;

        /*
                Query
                =====
                <static-query>        <!-- or a page-query -->
                {
                  metadata{
                    pathPrefix
                  }
                }
                </static-query>
                Requests for static files should look like this:
                ===============================================
                Using static-queries: axios( this.$static.metadata.pathPrefix + "/fileName" )
                Using page-queries,   axios( this.$page.metadata.pathPrefix   + "/fileName" )
                */
        store.addMetadata("pathPrefix", cleanedPathPrefix);
        store.addMetadata("cacheVersion", cacheVersion);

        let usageData = {}
        const usageDetails = store.getContentType('UsageDetail').collection.data;
        usageDetails.forEach(usageDetail=>{
            usageDetail.targets.forEach(id=>{
                if(!usageData[id]){
                    usageData[id] = []
                }
                usageData[id].push(usageDetail.id)
            })
        })

        const classes = store.addCollection({
            typeName: "Class",
        });
        const relationships = store.addCollection({
            typeName: "Relationship",
        });
        const namespaces = store.addCollection({
            typeName: "Namespace",
        });

        brickClasses.forEach((node) => {
            if (node.path.charAt(0) == "/")
                classes.addNode({
                    id: node.id,
                    name: node.name,
                    version: node.version,
                    type: node.type,
                    types: node.types,
                    namespace: store.createReference("Namespace", node.namespace),
                    path: node.path,
                    labels: node.labels,
                    generatedLabel: node.generatedLabel,
                    generatedAlias: node.generatedAlias,
                    superclasses: store.createReference("Class", node.superclasses),
                    subclasses: store.createReference("Class", node.subclasses),
                    comments: node.comments,
                    definitions: node.definitions,
                    equivalentClasses: store.createReference(
                        "Class",
                        node.equivalentClasses
                    ),
                    hierarchy: node.hierarchy,
                    inRangeOf: store.createReference("Relationship", node.inRangeOf),
                    inDomainOf: store.createReference("Relationship", node.inDomainOf),
                    usageDetails: store.createReference("UsageDetail", usageData[node.id]),
                });
        });
        brickRelationships.forEach((node) => {
            if (node.path.charAt(0) == "/")
                relationships.addNode({
                    id: node.id,
                    name: node.name,
                    version: node.version,
                    type: node.type,
                    types: node.types,
                    namespace: store.createReference("Namespace", node.namespace),
                    path: node.path,
                    labels: node.labels,
                    generatedLabel: node.generatedLabel,
                    generatedAlias: node.generatedAlias,
                    superProperties: store.createReference(
                        "Relationship",
                        node.superProperties
                    ),
                    subProperties: store.createReference(
                        "Relationship",
                        node.subProperties
                    ),
                    inverseProperties: store.createReference(
                        "Relationship",
                        node.inverseProperties
                    ),
                    comments: node.comments,
                    definitions: node.definitions,
                    hierarchy: node.hierarchy,
                    range: store.createReference("Class", node.range),
                    domain: store.createReference("Class", node.domain),
                    usageDetails: store.createReference("UsageDetail", usageData[node.id]),
                });
        });
        brickEntityProperties.forEach((node) => {
            if (node.path.charAt(0) == "/")
                relationships.addNode({
                    id: node.id,
                    name: node.name,
                    version: node.version,
                    type: node.type,
                    types: node.types,
                    namespace: store.createReference("Namespace", node.namespace),
                    path: node.path,
                    labels: node.labels,
                    generatedLabel: node.generatedLabel,
                    generatedAlias: node.generatedAlias,
                    superProperties: store.createReference(
                        "Relationship",
                        node.superProperties
                    ),
                    subProperties: store.createReference(
                        "Relationship",
                        node.subProperties
                    ),
                    inverseProperties: store.createReference(
                        "Relationship",
                        node.inverseProperties
                    ),
                    comments: node.comments,
                    definitions: node.definitions,
                    hierarchy: node.hierarchy,
                    range: store.createReference("Class", node.range),
                    domain: store.createReference("Class", node.domain),
                    usageDetails: store.createReference("UsageDetail", usageData[node.id]),
                });
        });
        brickShapes.forEach((node) => {
            if (node.path.charAt(0) == "/")
                classes.addNode({
                    id: node.id,
                    name: node.name,
                    version: node.version,
                    type: node.type,
                    types: node.types,
                    namespace: store.createReference("Namespace", node.namespace),
                    path: node.path,
                    labels: node.labels,
                    generatedLabel: node.generatedLabel,
                    generatedAlias: node.generatedAlias,
                    superclasses: store.createReference("Class", node.superclasses),
                    subclasses: store.createReference("Class", node.subclasses),
                    comments: node.comments,
                    definitions: node.definitions,
                    equivalentClasses: store.createReference(
                        "Class",
                        node.equivalentClasses
                    ),
                    hierarchy: node.hierarchy,
                    inRangeOf: store.createReference("Relationship", node.inRangeOf),
                    inDomainOf: store.createReference("Relationship", node.inDomainOf),
                    shaclDetails: node.shaclDetails,
                    usageDetails: store.createReference("UsageDetail", usageData[node.id]),
                });
        });
        brickNamespaces.forEach((node) => {
            if (node.path.charAt(0) == "/")
                namespaces.addNode({
                    id: node.id,
                    type: node.type,
                    version: node.version,
                    value: node.value,
                    path: node.path,
                    labels: node.labels,
                    generatedLabel: node.generatedLabel,
                    generatedAlias: node.generatedAlias,
                    comments: node.comments,
                    usageDetails: store.createReference("UsageDetail", usageData[node.id]),
                });
        });
    });

    api.beforeBuild(({ config, store }) => {
        // Generate an index file for Fuse to search webpages
        const pagesCollection = store.getContentType("Webpage").collection;

        const webpages = pagesCollection.data.map((webpage) => {
            return pick(webpage, ["title", "path", "summary"]);
        });

        const output = {
            dir: "./static",
            name: "search.json",
            ...options.output,
        };

        const outputPath = path.resolve(process.cwd(), output.dir);
        const outputPathExists = fs.existsSync(outputPath);
        const fileName = output.name.endsWith(".json")
            ? output.name
            : `${output.name}.json`;

        if (outputPathExists) {
            fs.writeFileSync(
                path.resolve(process.cwd(), output.dir, fileName),
                JSON.stringify(webpages)
            );
        } else {
            fs.mkdirSync(outputPath);
            fs.writeFileSync(
                path.resolve(process.cwd(), output.dir, fileName),
                JSON.stringify(webpages)
            );
        }
    });
};
