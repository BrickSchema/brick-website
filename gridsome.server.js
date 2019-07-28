// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const fs = require('fs');
const path = require('path');
const pick = require('lodash.pick');
const tagsets =  require('./static/tagsets.json')
const { pathPrefix } = require('./gridsome.config')

module.exports = function (api, options) {
  api.loadSource(store => {
      /*
      Clean the pathPrefix
      ====================
      not used =>  '/'
      ''       =>  '/'
      '/'      =>  '/'
      '/path'  =>  '/path'
      'path'   =>  '/path'
      'path/'  =>  '/path'
      '/path/' =>  '/path'
      */
      const cleanedPathPrefix = `${pathPrefix ? ['', ...pathPrefix.split('/').filter(dir=>dir.length)].join('/') : ''}`

      /*
      Query
      =====
      <static-query>        <!-- or a page-query -->
      {
        metaData{
          pathPrefix
        }
      }
      </static-query>
      Requests for static files should look like this:
      ===============================================
      Using static-queries: axios( this.$static.metaData.pathPrefix + "/fileName" )
      Using page-queries,   axios( this.$page.metaData.pathPrefix   + "/fileName" )
      */
      store.addMetaData('pathPrefix', cleanedPathPrefix)
      const classes = store.addContentType({
          typeName:'TagSet',
      })

      const removeEncoding = function(string) {
          let tokens = string.split('"');
          string = (tokens.length === 3) ? tokens[1] : string;
          return string.split('@').shift();
      }
      tagsets.forEach(node=>{
              classes.addNode({
              id: node.id,
              path: 'tagsets/' + node.id.split('#').pop(),
              labels: node.labels,
              generatedLabel: node.generatedLabel,
              generatedAlias: node.generatedAlias,
              superclasses: store.createReference('TagSet', node.superclasses),
              subclasses: store.createReference('TagSet', node.subclasses),
              comments: node.comments,
              definitions: node.definitions.map(def => removeEncoding(def)),
              equivalentClasses: store.createReference('TagSet', node.equivalentClasses),
              hierarchy: store.createReference('TagSet', node.hierarchy.split('>'))
          })

          const outputPath = path.resolve(process.cwd(), './static/hierarchy')
          const outputPathExists = fs.existsSync(outputPath)
          const fileName = node.id.split('#').pop().endsWith('.json')
              ? node.id.split('#').pop()
              : `${node.id.split('#').pop()}.json`

          if (outputPathExists) {
              fs.writeFileSync(path.resolve(process.cwd(), './static/hierarchy', fileName), JSON.stringify({
                  subclasses: node.subclasses,
              }))
          } else {
              fs.mkdirSync(outputPath)
              fs.writeFileSync(path.resolve(process.cwd(), './static/hierarchy', fileName), JSON.stringify({
                  subclasses: node.subclasses,
              }))
          }

      })
  })

  api.beforeBuild(({ config, store }) => {

      // Generate an index file for Fuse to search webpages
      const pagesCollection = store.getContentType('Webpage').collection;

      const webpages = pagesCollection.data.map(webpage => {
          return pick(webpage, ['title', 'path', 'summary']);
      });


      // Generate an index file for Fuse to search TagSets
      const tagSets = store.getContentType('TagSet').collection;

      const classes = tagSets.data.map(className => {
          return{
              generatedLabel: className.generatedLabel,
              labels: className.labels,
              generatedAlias: className.generatedAlias,
              definitions: className.definitions,
              path: className.path
          }
      });

    const output = {
      dir: './static',
      name: 'search.json',
      ...options.output
    }

    const outputPath = path.resolve(process.cwd(), output.dir)
    const outputPathExists = fs.existsSync(outputPath)
    const fileName = output.name.endsWith('.json')
      ? output.name
      : `${output.name}.json`

    if (outputPathExists) {
        fs.writeFileSync(path.resolve(process.cwd(), output.dir, fileName), JSON.stringify([...classes, ...webpages]))
    } else {
      fs.mkdirSync(outputPath)
        fs.writeFileSync(path.resolve(process.cwd(), output.dir, fileName), JSON.stringify([...classes, ...webpages]))
    }
  })
}
