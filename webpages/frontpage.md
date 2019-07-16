---
title: Front Page
path: /testfront
summary: Front page of Brick site
show_on_navbar: false
---

## What is Brick?

Brick is an open-source effort to standardize semantic descriptions of the **physical, logical and virtual assets** in buildings and **the relationships between them**.
Brick consists of an **extensible dictionary** of terms and concepts in and around buildings, a set of **relationships** for linking and composing concepts together, and a **flexible data model** permitting seamless integration of Brick with existing tools and databases.
Through the use of powerful Semantic Web technology, Brick can describe the broad set of idiosyncratic and custom features, assets and subsystems found across the building stock in a consistent matter.

Brick:

- lowers the cost of deploying analytics, energy effiency measures and intelligent controls across buildings
- presents an integrated, cross-vendor representation of the multitude of subsystems in modern buildings: HVAC, lighting, fire, security and so on
- simplifies the development of smart analytics and control applications
- reduces the reliance upon the non-standard, unstructured labels endemic to building management systems

Brick is free and open-sourced under the BSD 3-Clause license. The source code for Brick, this website, and related tools developed by the Brick team are available on **[GitHub](https://github.com/BrickSchema)**.

## How Does Brick Compare to X?

**Project Haystack** ([link](https://project-haystack.org/)) is a popular tagging system for describing building assets using semi-structured sets of tags.
Because there are no formal rules for how tags can be used, Haystack-based descriptions of buildings tend to consist of ad-hoc collections of tags, resulting in highly custom and inconsistent modeling practices across sites.
Brick includes a tagging system similar to Haystack that augments tags with formal semantic rules that promote consistency and interpretability.

**Industry Foundation Classes** ([link](https://technical.buildingsmart.org/)) and **Building Information Models** ([link](https://www.nationalbimstandard.org/)) emerged from the need for a common exchange model for the 3D architectural drawings needed for a building's construction. BIM models capture structural information, but lack descriptions of how the constituent equipment and points function together.

**Building Topology Ontology (BOT)** ([link](https://w3c-lbd-cg.github.io/bot/)) is a complementary effort for semantic building metadata from the [Linked Building Data W3C Community Group](https://www.w3.org/community/lbd/) that focuses on capturing topological concepts in buildings such as sites, floors, zones and rooms. Because BOT is built using the Semantic Web, it can be used in tandem with Brick.

**Smart Appliances REFerence Ontology (SAREF)** ([link](https://sites.google.com/site/smartappliancesproject/ontologies/reference-ontology)) is an ontology capturing high level aspects of smart and connected appliances. While SAREF does not capture the the full spectrum of equipment and sensors that exist in buildings, SAREF models can be easily integrated into Brick.
