---
targets: 
    - 1.2^https://brickschema.org/schema/Brick#TimeseriesReference
    - 1.2^https://brickschema.org/schema/Brick#Database
    - 1.2^https://brickschema.org/schema/Brick#hasTimeseriesId
    - 1.2^https://brickschema.org/schema/Brick#timeseries
    - 1.2^https://brickschema.org/schema/Brick#storedAt
---

## Example usage

```turtle
:sensor1    a   brick:Temperature_Sensor ;
    brick:hasUnit unit:DEG_F ;
    brick:timeseries [
        brick:hasTimeseriesId   "8f541ba4-c437-43ba-ba1d-5c946583fe54" ;
        brick:storedAt  :database ;
    ] ;
.

:sensor2    a   brick:Temperature_Sensor ;
    brick:hasUnit unit:DEG_F ;
    brick:timeseries [
        brick:hasTimeseriesId   "38b5fa0e-407e-4a23-8800-6ec4f6d60785" ;
        brick:storedAt  :database ;
    ] ;
.

# the properties on the database instance are non-normative
:database   a   brick:Database ;
    rdfs:label  "Postgres Timeseries Storage" ;
    :connstring "postgres://1.2.3.4/data" ;
.
```

Read more about [Timeseries Storage](https://docs.brickschema.org/metadata/timeseries-storage.html) here.
