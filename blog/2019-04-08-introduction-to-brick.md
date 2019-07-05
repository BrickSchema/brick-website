---
title: Why use Brick
path: introduction-to-brick
date: 2019-04-05
summary: Brick is an open-source, BSD-licensed development effort to create a uniform schema for representing metadata in buildings.
tags: ['brick']
---

![background](./images/blog_bg_1.jpg)

> Commercial buildings have long since been a primary target for applications from a number of areas: from cyber-physical systems to building energy use to improved human interactions in built environments. While technological advances have been made in these areas, such solutions rarely experience widespread adoption due to the lack of a common descriptive schema reducing the now-prohibitive cost of porting these applications and systems to different buildings.
### Why Brick?

- **Local development with hot-reloading** - See code changes in real-time.
- **Data source plugins** - Use it for any popular Headless CMSs, APIs or Markdown-files.
- **File-based page routing** - Quickly create and manage routes with files.
- **Centralized data managment** - Pull data into a local, unified GraphQL data layer.
- **Vue.js for frontend** - A lightweight and approachable front-end framework.
- **Auto-optimized code** - Get code-splitting and asset optimization out-of-the-box.
- **Static files generation** - Deploy securely to any CDN or static web host.

[Learn more about how Brick works](/docs/how-it-works)

```js
<template>
  <Layout>
    <div class="container-inner mx-auto my-16">
      <h1 class="text-4xl font-bold leading-tight">{{ $page.post.title }}</h1>
      <div class="text-xl text-gray-600 mb-8">{{ $page.post.date }}</div>
      <div class="markdown-body" v-html="$page.post.content" />
    </div>
  </Layout>
</template>
```


### Prerequisites
You should have basic knowledge about HTML, CSS, [Vue.js](https://vuejs.org) and how to use the [Terminal](https://www.linode.com/docs/tools-reference/tools/using-the-terminal/). Knowing how [Vue Single File components](https://vuejs.org/v2/guide/single-file-components.html) & [GraphQL](https://www.graphql.com/) works is a plus, but not required. Brick is a great way to learn both.

Brick requires **Node.js** and recommends **Yarn**. [How to setup](/docs/prerequisites)

![background](./images/background.jpg)

### 1. Install Brick CLI tool

Using yarn:
`yarn global add @brick/cli`

Using npm:
`npm install --global @brick/cli`

### 2. Create a Brick project

1. `brick create my-brick-site` to create a new project </li>
2. `cd my-brick-site` to open folder
3. `brick develop` to start local dev server at `http://localhost:8080`
4. Happy coding 🎉🙌

### 3. Next steps

1. Create `.vue` components in the `/pages` directory to create page routes.
2. Use `brick build` to generate static files in a `/dist` folder


- [How it works](/docs/how-it-works)
- [How Pages work](/docs/pages)
- [How to deploy](/docs/deployment)
