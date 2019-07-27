# brick-website

[![Website](https://img.shields.io/website/https/brick.andrew.cmu.edu.svg?logo=vue.js&style=for-the-badge)](https://brick.andrew.cmu.edu/)

This is a website for BrickSchema.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation

```sh
git clone https://github.com/shreyasnagare/brick-website.git
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
