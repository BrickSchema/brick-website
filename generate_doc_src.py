from util import generate_doc_src, auto_dict
from rdflib import Graph
from urllib.error import URLError

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
