# Modifying the personas:
The details of a persona are stored in a markdown file in the [personas](/personas) folder.

## Structure
```
---
label: What is this persona called? (this is displayed in the persona selector)
id: A unique id for this persona (this is used later to filter content)
path (optional): Automatically generated if not specified. This is for future use.
description (optional): Description of this persona (this is displayed in the persona selector)
thumbnail (optional): This is for future use.
---

Frontpage content for this persona in markdown
>> Example: layman friendly language and lesser details for non-technical users.

```

# Modifying the pages:
Every markdown file (even in subfolders) in the [webpages](/webpages) folder is converted to a webpage.

## Structure
```
---
title: Title of the page.
path: A unique path where this page will be created.
summary (optional): What information does this page provide?
show_on_navbar (optional): If set to true, the title of the webpage will be displayed on the navbar. (only to selected personas)
personas (optional): List of persona IDs this webpage is relevant to.
---

Webpage content in markdown.

```
### Tips:
 - You can use the same title for two different files (example: 'Concepts' for technical persona and 'Concepts' for non-technical persona). It would be a good idea to put different personas in each file.
 - Use images as you would normally use.
 - Keeping similar pages in the same folder makes more sense. Example: (/concepts/summary.md and /concepts/indepth.md)
 - Try to give users access to other pages. Example: summary.md >> For more detailed concepts, see [this](path for indepth concepts)
 - To avoid haveing longer pages, split the content into multiple pages and use md hyperlinks [example](/webpages/concepts/technical.md). (These pages would ideally have show_on_navbar: false with a few/no personas)

## Content filtering
Example webpage:
```
---
title: Contribute
path: /contribute
summary: How to contribute
show_on_navbar: true
personas: ['contributor','developer']
---
# Contributing to Brick
...
...
```
### Navbar
- will show "Contribute" tab on the the navbar if the current persona is either a contributor or a developer.
- tabs will be in the lexicographical order of the webpage's md filename. So, if the order matters, you can name the files '1.somepage.md' and '2.otherpage.md'
### Home Page
The homepage will have the following structure for persona X:
```
The content of personaX markdown file
---
Pages most relevant to your persona:
- list of pages (title with summary) that have persona X in the list of personas
```
 
