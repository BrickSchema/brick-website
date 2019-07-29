// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const fs = require('fs');
const path = require('path');
const pick = require('lodash.pick');
const brickClasses = require('./static/ontology/1.1.0/classes.json')
const brickRelationships = require('./static/ontology/1.1.0/relationships.json')
const brickNamespaces = require('./static/ontology/1.1.0/namespaces.json')
const brickClassesOld = require('./static/ontology/1.0.3/classes.json')
const brickRelationshipsOld = require('./static/ontology/1.0.3/relationships.json')
const brickNamespacesOld = require('./static/ontology/1.0.3/namespaces.json')
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
          typeName:'Class',
      })
      const relationships = store.addContentType({
          typeName:'Relationship',
      })
      const namespaces = store.addContentType({
          typeName:'Namespace',
      })

      brickClasses.forEach(node=>{
              classes.addNode({
                  id: node.id,
                  version: node.version,
                  type: node.type,
                  types: node.types,
                  namespace: store.createReference('Namespace', node.namespace),
                  name: node.name,
                  path: node.path,
                  labels: node.labels,
                  generatedLabel: node.generatedLabel,
                  generatedAlias: node.generatedAlias,
                  superclasses: store.createReference('Class', node.superclasses),
                  subclasses: store.createReference('Class', node.subclasses),
                  comments: node.comments,
                  definitions: node.definitions,
                  equivalentClasses: store.createReference('Class', node.equivalentClasses),
                  hierarchy: node.hierarchy,
                  inRangeOf: store.createReference('Relationship', node.inRangeOf),
                  inDomainOf: store.createReference('Relationship', node.inDomainOf)
              })
      })
      brickRelationships.forEach(node=>{
          relationships.addNode({
              id: node.id,
              version: node.version,
              type: node.type,
              types: node.types,
              namespace: store.createReference('Namespace', node.namespace),
              name: node.name,
              path: node.path,
              labels: node.labels,
              generatedLabel: node.generatedLabel,
              generatedAlias: node.generatedAlias,
              superProperties: store.createReference('Relationship', node.superProperties),
              subProperties: store.createReference('Relationship', node.subProperties),
              inverseProperties: store.createReference('Relationship', node.inverseProperties),
              comments: node.comments,
              definitions: node.definitions,
              hierarchy: node.hierarchy,
              range: store.createReference('Class', node.range),
              domain: store.createReference('Class', node.domain)
          })
      })
      brickNamespaces.forEach(node=>{
          namespaces.addNode({
              id: node.id,
              type: node.type,
              version: node.version,
              value: node.value,
              path: node.path,
              labels: node.labels,
              generatedLabel: node.generatedLabel,
              generatedAlias: node.generatedAlias,
              comments: node.comments,
          })
      })

      brickClassesOld.forEach(node=>{
          classes.addNode({
              id: node.id,
              version: node.version,
              type: node.type,
              types: node.types,
              namespace: store.createReference('Namespace', node.namespace),
              name: node.name,
              path: node.path,
              labels: node.labels,
              generatedLabel: node.generatedLabel,
              generatedAlias: node.generatedAlias,
              superclasses: store.createReference('Class', node.superclasses),
              subclasses: store.createReference('Class', node.subclasses),
              comments: node.comments,
              definitions: node.definitions,
              equivalentClasses: store.createReference('Class', node.equivalentClasses),
              hierarchy: node.hierarchy,
              inRangeOf: store.createReference('Relationship', node.inRangeOf),
              inDomainOf: store.createReference('Relationship', node.inDomainOf)
          })
      })
      brickRelationshipsOld.forEach(node=>{
          relationships.addNode({
              id: node.id,
              version: node.version,
              type: node.type,
              types: node.types,
              namespace: store.createReference('Namespace', node.namespace),
              name: node.name,
              path: node.path,
              labels: node.labels,
              generatedLabel: node.generatedLabel,
              generatedAlias: node.generatedAlias,
              superProperties: store.createReference('Relationship', node.superProperties),
              subProperties: store.createReference('Relationship', node.subProperties),
              inverseProperties: store.createReference('Relationship', node.inverseProperties),
              comments: node.comments,
              definitions: node.definitions,
              hierarchy: node.hierarchy,
              range: store.createReference('Class', node.range),
              domain: store.createReference('Class', node.domain)
          })
      })
      brickNamespacesOld.forEach(node=>{
          namespaces.addNode({
              id: node.id,
              type: node.type,
              version: node.version,
              value: node.value,
              path: node.path,
              labels: node.labels,
              generatedLabel: node.generatedLabel,
              generatedAlias: node.generatedAlias,
              comments: node.comments,
          })
      })
  })

  api.beforeBuild(({ config, store }) => {

      // Generate an index file for Fuse to search webpages
      const pagesCollection = store.getContentType('Webpage').collection;

      const webpages = pagesCollection.data.map(webpage => {
          return pick(webpage, ['title', 'path', 'summary']);
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
        fs.writeFileSync(path.resolve(process.cwd(), output.dir, fileName), JSON.stringify(webpages))
    } else {
      fs.mkdirSync(outputPath)
        fs.writeFileSync(path.resolve(process.cwd(), output.dir, fileName), JSON.stringify(webpages))
    }
  })
}
