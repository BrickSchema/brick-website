# brick-website

[![Netlify Status](https://api.netlify.com/api/v1/badges/41fc2de2-860a-48de-b3fc-bcc58f173dbf/deploy-status)](https://app.netlify.com/sites/brickschema/deploys)

This is a website for [BrickSchema](https://brickschema.org/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation

```sh
git clone https://github.com/BrickSchema/brick-website.git
```
```sh
cd brick-website
npm install
npm run develop
```
This will start a local development server. The server will start at http://localhost:8080/ with hot-reloading etc.

### Deployment

```sh
cd brick-website
npm run build
```
This will generate static files in the `./dist` directory which can be hosted anywhere, even on a CDN. There is no need for a Node.js server.
 
## Built With
 
 * [Vue.js](https://vuejs.org/) - The javascript framework
 * [Gridsome](https://gridsome.org/) - The Vue.js framework
 * [gridsome-portfolio-starter](https://github.com/drehimself/gridsome-portfolio-starter) - Theme for Gridsome
 
## License
 
 This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
