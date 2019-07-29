---
title: Resources
path: /resources
summary: Brick core files, papers and example buildings
show_on_navbar: true
---

## Brick Distribution
---

The Brick ontology is distributed as a set of [Turtle][15] files.
Turtle is a compact textual format that is understood by most Semantic Web tools.


- **Latest Version (1.0.3)**:
   - [Brick.ttl][1]: Brick classes and tagsets
   - [BrickFrame.ttl][2]: Brick relationship definitions
   - [BrickTag.ttl][3]: Brick tags (internal)
   - [BrickUse.ttl][4]: Brick "uses" relationships (internal)

## Reference Brick Models
---
These five models are representative examples of how Brick can be used to model real buildings.
For an in-depth discussion of the creation and evaluation of these Brick models, please refer to the [BuildSys 2016][6] and [Applied Energy 2018][5] papers.

Building  |Location| BMS  | Built | Sq Ft | Points | Classified | Relationships
----------|--------|------|-------|-------|----------|--------------|----------------
[Soda Hall][10] | Berkeley, CA | Barrington Systems | 1994  | 110,565  | 1,586  | 98.7%  | 1,939
[Gates Hillman Center][11]  | Pittsburgh, PA, USA  | Automated Logic Controls | 2009  | 217,000 | 8,292  | 99%  | 35,693
[Rice Hall][12]  | Charlottesville, VA, USA  | | 2011  | 100,000 | 1,300  | 98.5%  | 2,158
[Engineering Building Unit 3B][13]  | San Diego, CA, USA  | Johnson Controls  | 2004 | 150,000 | 4,594 | 96% | 8,383
[Green Tech House][14] | Vejle, Denmark | Niagara | 2014 | 38,000 | 956 | 98.8% | 19,086

- **Points**: the number of BMS points contained in the model
- **Relationships**: the number of relationships contained in the model
- **Classified**: the percentage of points classified with Brick

## Academic Publications
---

#### 2018

[Brick: Metadata Schema for Portable Smart Building Applications][5].    
Bharathan Balaji, Arka Bhattacharya, Gabriel Fierro, Jingkun Gao, Joshua Gluck, Dezhi Hong, Aslak Johansen, Jason Koh, Joern Ploennigs, Yuvraj Agarwal, Mario Berges, David Culler, Rajesh Gupta, Mikkel Baun Kjærgaard, Mani Srivastava, and Kamin Whitehouse. Applied Energy 226 (2018) 1273-1292.    
DOI: https://doi.org/10.1016/j.apenergy.2018.02.091    

[Design and Analysis of a Query Processor for Brick][17].    
Gabe Fierro and David E. Culler. ACM Transactions on Sensor Networks 14, 3-4, Article 18 (November 2018), 25 pages.    
DOI: https://doi.org/10.1145/3199666

[Mortar: An Open Testbed for Portable Building Analytics][18].    
Gabe Fierro, Marco Pritoni, Moustafa AbdelBaky, Paul Raftery, Therese Peffer, Greg Thomson, and David E. Culler. In Proceedings of the 5th Conference on Systems for Built Environments (BuildSys 2018).    
DOI: https://doi.org/10.1145/3276774.3276796

[Scrabble: Transferrable Semi-Automated Semantic Metadata Normalization Using Intermediate Representation][19].    
Jason Koh, Bharathan Balaji, Dhiman Sengupta, Julian McAuley, Rajesh Gupta, and Yuvraj Agarwal.  In Proceedings of the 5th Conference on Systems for Built Environments (BuildSys 2018).    
DOI: https://doi.org/10.1145/3276774.3276795

[Plaster: an Integration, Benchmark, and Development Framework for Metadata Normalization Methods][20].     
Jason Koh, Dezhi Hong, Rajesh Gupta, Kamin Whitehouse, Hongning Wang, and Yuvraj Agarwal. In Proceedings of the 5th Conference on Systems for Built Environments (BuildSys 2018).    
DOI: https://doi.org/10.1145/3276774.3276794

#### 2017

[HodDB: a Query Processor for Brick][16].    
Gabe Fierro, David E. Culler. In Proceedings of the 4th ACM International Conference on Systems for Energy-Efficient Built Environment (BuildSys 2017).    
DOI: https://doi.org/10.1145/3137133.3141449

#### 2016

[Brick: Towards a Unified Metadata Schema For Buildings][6].    
Bharathan Balaji, Arka Bhattacharya, Gabriel Fierro, Jingkun Gao, Joshua Gluck, Dezhi Hong, Aslak Johansen, Jason Koh, Joern Ploennigs, Yuvraj Agarwal, Mario Berges, David Culler, Rajesh Gupta, Mikkel Baun Kjærgaard, Mani Srivastava, and Kamin Whitehouse. In Proceedings of the 3rd ACM International Conference on Systems for Energy-Efficient Built Environments (BuildSys 2016).    
DOI: https://doi.org/10.1145/2993422.2993577    

[Demo Abstract: Portable Queries Using the Brick Schema for Building Applications][8].    
Bharathan Balaji, Arka Bhattacharya, Gabriel Fierro, Jingkun Gao, Joshua Gluck, Dezhi Hong, Aslak Johansen, Jason Koh, Joern Ploennigs, Yuvraj Agarwal, Mario Berges, David Culler, Rajesh Gupta, Mikkel Baun Kjærgaard, Mani Srivastava, and Kamin Whitehouse. In Proceedings of the 3rd ACM International Conference on Systems for Energy-Efficient Built Environments (BuildSys 2016).    
DOI: https://doi.org/10.1145/2993422.2996411

#### 2015

[Short Paper: Analyzing Metadata Schemas for Buildings —The Good, The Bad, and The Ugly][21].   
Arka Bhattacharya, Joern Ploennigs, and David Culler. 2015. Short Paper: Analyzing Metadata Schemas for Buildings: The Good, the Bad, and the Ugly. In Proceedings of the 2nd ACM International Conference on Embedded Systems for Energy-Efficient Built Environments (BuildSys 2015).    
DOI: https://doi.org/10.1145/2821650.2821669

## White Papers

[White Paper | Brick Schema: Building Blocks for Smart Buildings](https://www.memoori.com/wp-content/uploads/2016/06/Brick_Schema_Whitepaper.pdf)
Memoori 2019

[Leaflet | Brick : Metadata Schema for Buildings for Building Applications][9]

## Presentations
[Presentation | Brick: Towards a Unified Metadata Schema For Buildings][7]
BuildSys 2016


[1]: https://brickschema.org/ttl/Brick.ttl
[2]: https://brickschema.org/ttl/BrickFrame.ttl
[3]: https://brickschema.org/ttl/BrickTag.ttl
[4]: https://brickschema.org/ttl/BrickUse.ttl
[5]: https://www.sciencedirect.com/science/article/pii/S0306261918302162
[6]: https://brickschema.org/papers/Brick-BuildSys2016.pdf
[7]: https://brickschema.org/papers/Brick_BuildSys_Presentation.pdf
[8]: https://brickschema.org/papers/Brick_BuildSys2016_Demo.pdf
[9]: https://brickschema.org/docs/Brick-Leaflet.pdf
[10]: https://brickschema.org/ttl/soda_brick.ttl
[11]: https://brickschema.org/ttl/ghc_brick.ttl
[12]: https://brickschema.org/ttl/rice_brick.ttl
[13]: https://brickschema.org/ttl/ebu3b_brick.ttl
[14]: https://brickschema.org/ttl/gtc_brick.ttl
[15]: https://www.w3.org/TR/turtle/
[16]: http://people.eecs.berkeley.edu/~gtfierro/papers/hoddb.pdf
[17]: http://people.eecs.berkeley.edu/~gtfierro/papers/hoddb_tosn.pdf
[18]: http://people.eecs.berkeley.edu/~gtfierro/papers/mortar.pdf
[19]: http://mesl.ucsd.edu/pubs/Jason_BuildSys2018Scrabble.pdf
[20]: https://jbkoh.github.io/pdf/buildsys2018_plaster.pdf
[21]: http://sdb.cs.berkeley.edu/sdb/files/publications/sdb/buildsys2015_metadatasurvey.pdf
