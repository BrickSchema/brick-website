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

Description of the persona (for future use)
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
 - Use images as you would normally use.
 - Keeping similar pages in the same folder makes more sense. Example: (/concepts/summary.md and /concepts/indepth.md)
 - Try to give users access to related pages. Example: summary.md >> For more detailed concepts, see [this](path for indepth concepts)
 - To avoid haveing longer pages, split the content into multiple pages and use md hyperlinks [example](/webpages/concepts/technical.md). (These pages would ideally have show_on_navbar: false with a few/no personas)

## Suggesting content
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
Use the personas list to mark this page as important/useful for the mentioned personas.

# Modifying the home page
The homepage will have the following structure:
```
The content of /about markdown file
---
If you are a personaX, check out these pages:
- list of pages (titles) that have persona X in the list of personas

If you are a personaY, check out these pages:
- list of pages (titles) that have persona Y in the list of personas

...
```
Where `/about` is the webpage with "/about" as its path.
 
