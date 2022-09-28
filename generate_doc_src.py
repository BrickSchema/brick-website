from util import generate_doc_src, auto_dict
from rdflib import Graph
from urllib.error import URLError
import os

# Pull the latest Brick.ttl to /static/schema
try:
    print("[ ] Fetching the latest version of Brick.ttl...", end="\r")
    g = Graph()
    g.parse("https://github.com/brickschema/Brick/releases/latest/download/Brick.ttl", format="turtle")
    g.serialize("static/schema/Brick.ttl", format="turtle")
    print("[✓] Fetching the latest version of Brick.ttl   ")
except URLError as e:
    print("[WARN]: Unable to pull the latest version of Brick!")


# Doc config
doc_spec = auto_dict()

# Brick v1.0.3
doc_spec["1.0.3"]["input"] = ["static/schema/1.0.3"]
doc_spec["1.0.3"]["ns_restriction"] = [
    "https://brickschema.org/schema/1.0.3/Brick#",
    "https://brickschema.org/schema/1.0.3/BrickFrame#",
]
doc_spec["1.0.3"]["classes"]["type_restriction"] = [
    "http://www.w3.org/2002/07/owl#Class"
]
doc_spec["1.0.3"]["relationships"]["type_restriction"] = [
    "http://www.w3.org/2002/07/owl#ObjectProperty"
]


# Brick v1.1
doc_spec["1.1"]["input"] = ["static/schema/1.1"]
doc_spec["1.1"]["ns_restriction"] = ["https://brickschema.org/schema/1.1/Brick#"]
doc_spec["1.1"]["classes"]["type_restriction"] = ["http://www.w3.org/2002/07/owl#Class"]
doc_spec["1.1"]["relationships"]["type_restriction"] = [
    "http://www.w3.org/2002/07/owl#ObjectProperty"
]


# Brick v1.2
doc_spec["1.2"]["input"] = ["static/schema/1.2"]
doc_spec["1.2"]["ns_restriction"] = ["https://brickschema.org/schema/Brick#"]
doc_spec["1.2"]["classes"]["type_restriction"] = ["http://www.w3.org/2002/07/owl#Class"]
doc_spec["1.2"]["relationships"]["type_restriction"] = [
    "http://www.w3.org/2002/07/owl#ObjectProperty"
]

# Brick v1.3
doc_spec["1.3.0"]["input"] = ["static/schema/1.3"]
doc_spec["1.3.0"]["ns_restriction"] = ["https://brickschema.org/schema/Brick#"]
doc_spec["1.3.0"]["classes"]["type_restriction"] = ["http://www.w3.org/2002/07/owl#Class"]
doc_spec["1.3.0"]["relationships"]["type_restriction"] = [
    "http://www.w3.org/2002/07/owl#ObjectProperty"
]

# Pull the latest Brick.ttl nightly to /static/schema
try:
    print("[ ] Fetching the latest nightly build of Brick.ttl...", end="\r")
    g = Graph()
    g.parse("https://github.com/BrickSchema/Brick/releases/download/nightly/Brick.ttl", format="turtle")
    os.makedirs("static/schema/nightly", exist_ok=True)
    g.serialize("static/schema/nightly/Brick.ttl", format="turtle")
    print("[✓] Fetching the latest nightly build of Brick.ttl   ")

    # Brick v1.2
    doc_spec["Nightly"]["input"] = ["static/schema/nightly"]
    doc_spec["Nightly"]["ns_restriction"] = ["https://brickschema.org/schema/Brick#"]
    doc_spec["Nightly"]["classes"]["type_restriction"] = ["http://www.w3.org/2002/07/owl#Class"]
    doc_spec["Nightly"]["relationships"]["type_restriction"] = [
        "http://www.w3.org/2002/07/owl#ObjectProperty"
    ]
except URLError as e:
    print("[WARN]: Unable to pull the latest version of Brick!")

if __name__ == "__main__":
    generate_doc_src(doc_spec)

# Structure
# doc_spec = {
#     "1.0.3": {
#         "ns_restriction":  ["https://brickschema.org/schema/1.0.3/Brick#", "https://brickschema.org/schema/1.0.3/BrickFrame#"]
#         "classes" : {
#             "roots": [],
#             "type_restriction": ["http://www.w3.org/2002/07/owl#Class"]
#             "ns_restriction": [
#               "https://brickschema.org/schema/1.0.3/Brick#",
#               "https://brickschema.org/schema/1.0.3/BrickFrame#"
#              ],
#             "parent_restriction": [],
#             "no_expansion": [],
#             "exclusions": []
#         }
#     }
# }
