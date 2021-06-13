---
title: py-brickschema
path: /tools/py-brickschema
date: 2020-01-01
summary: Python library for managing and querying Brick models
categories: ['utility','Python','library']
thumbnail: ./images/python-logo.png
url: https://pypi.org/project/brickschema/
---

- [Documentation](https://brickschema.readthedocs.io/en/latest/)
- [Source Code](https://github.com/BrickSchema/py-brickschema)

## Features

- wrapper around [RDFlib](https://github.com/RDFLib/rdflib) providing syntactic sugar and simplified use
- automatic loading of Brick ontology into graphs
- embedded SPARQL server and web interface
- built-in reasoning and inference (OWL, SHACL, RDFS)

## Quickstart

The main `Graph` object is just a subclass of the excellent [RDFlib Graph](https://rdflib.readthedocs.io/en/stable/) library, so all features on `rdflib.Graph` will also work here.

Brief overview of the main features of the `brickschema` package:

```python
import brickschema

# creates a new rdflib.Graph with a recent version of the Brick ontology
# preloaded.
g = brickschema.Graph(load_brick=True)
# OR use the absolute latest Brick:
# g = brickschema.Graph(load_brick_nightly=True)
# OR create from an existing model
# g = brickschema.Graph(load_brick=True).from_haystack(...)

# load in data files from your file system
g.load_file("mbuilding.ttl")
# ...or by URL (using rdflib)
g.parse("https://brickschema.org/ttl/soda_brick.ttl", format="ttl")

# perform reasoning on the graph (edits in-place)
g.expand(profile="owlrl")
g.expand(profile="shacl") # infers Brick classes from Brick tags

# validate your Brick graph against built-in shapes (or add your own)
valid, _, resultsText = g.validate()
if not valid:
    print("Graph is not valid!")
    print(resultsText)

# perform SPARQL queries on the graph
res = g.query("""SELECT ?afs ?afsp ?vav WHERE  {
    ?afs    a       brick:Air_Flow_Sensor .
    ?afsp   a       brick:Air_Flow_Setpoint .
    ?afs    brick:isPointOf ?vav .
    ?afsp   brick:isPointOf ?vav .
    ?vav    a   brick:VAV
}""")
for row in res:
    print(row)

# start a blocking web server with an interface for performing
# reasoning + querying functions
g.serve("localhost:8080")
# now visit in http://localhost:8080
```

## Features

## Inference

`brickschema` makes it easier to employ reasoning on your graphs. Simply call the `expand` method on the Graph object with one of the following profiles:
- `"rdfs"`: RDFS reasoning
- `"owlrl"`: OWL-RL reasoning (using 1 of 3 implementations below)
- `"vbis"`: add VBIS tags to Brick entities
- `"tag"`: infer Brick classes from Brick tags


```python
from brickschema import Graph

g = Graph(load_brick=True)
g.load_file("test.ttl")
g.expand(profile="owlrl")
print(f"Inferred graph has {len(g)} triples")
```


The package will automatically use the fastest available reasoning implementation for your system:

- `reasonable` (fastest, Linux-only for now): `pip install brickschema[reasonable]`
- `Allegro` (next-fastest, requires Docker): `pip install brickschema[allegro]`
- OWLRL (default, native Python implementation): `pip install brickschema`

To use a specific reasoner, specify `"reasonable"`, `"allegrograph"` or `"owlrl"` as the value for the `backend` argument to `graph.expand`.

## Haystack Translation

`brickschema` can produce a Brick model from a JSON export of a Haystack model.
Then you can use this package as follows:

```python
import json
from brickschema import Graph
model = json.load(open("haystack-export.json"))
g = Graph(load_brick=True).from_haystack("http://project-haystack.org/carytown#", model)
points = g.query("""SELECT ?point ?type WHERE {
    ?point rdf:type/rdfs:subClassOf* brick:Point .
    ?point rdf:type ?type
}""")
print(points)
```

## VBIS Translation

`brickschema` can add [VBIS](https://vbis.com.au/) tags to a Brick model easily

```python
from brickschema import Graph
g = Graph(load_brick=True)
g.load_file("mybuilding.ttl")
g.expand(profile="vbis")

vbis_tags = g.query("""SELECT ?equip ?vbistag WHERE {
    ?equip  <https://brickschema.org/schema/1.1/Brick/alignments/vbis#hasVBISTag> ?vbistag
}""")
```

## Web-based Interaction

`brickschema` now supports interacting with a Graph object in a web browser. Executing `g.serve(<http address>)` on a graph object from your Python script or interpreter will start a webserver listening (by default) at http://localhost:8080 . This uses [Yasgui](https://yasgui.triply.cc/) to provide a simple web interface supporting SPARQL queries and inference.


## Brick model validation

The module utilizes the [pySHACL](https://github.com/RDFLib/pySHACL) package to validate a building ontology against the Brick Schema, its default constraints (shapes) and user provided shapes.

```python
from brickschema import Graph

g = Graph(load_brick=True)
g.load_file('myBuilding.ttl')
valid, _, _ = g.validate()
print(f"Graph is valid? {valid}")

# validating using externally-defined shapes
external = Graph()
external.load_file("other_shapes.ttl")
valid, _, _ = g.validate(shape_graphs=[external])
print(f"Graph is valid? {valid}")
```

The module provides a command
`brick_validate` similar to the `pyshacl` command.  The following command is functionally
equivalent to the code above.
```bash
brick_validate myBuilding.ttl -s other_shapes.ttl
```
