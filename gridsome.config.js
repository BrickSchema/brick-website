// This is where project configuration and plugin options are located.
// Learn more: https://gridsome.org/docs/config

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`

const tailwind = require('tailwindcss')
// const purgecss = require('@fullhuman/postcss-purgecss')

const postcssPlugins = [
  tailwind(),
]

// if (process.env.NODE_ENV === 'production') postcssPlugins.push(purgecss())

module.exports = {
  siteName: 'BrickSchema',
  siteDescription: 'A uniform metadata schema for buildings',
  siteUrl: 'https://brickschema.org',
  plugins: [
    {
      use: '@gridsome/source-filesystem',
      options: {
        path: 'blog/**/*.md',
        typeName: 'Post',
        refs: {
          tags: {
            typeName: 'Tag',
            route: 'tags/:id',
            create: true
          }
        },
      }
    },
    {
      use: '@gridsome/source-filesystem',
      options: {
        path: 'tools/**/*.md',
        typeName: 'App',
        refs: {
          categories: {
            typeName: 'Category',
            route: 'categories/:id',
            create: true
          }
        },
      }
    },
    {
      use: '@gridsome/source-filesystem',
      options: {
        path: 'usageDetails/**/*.md',
        typeName: 'UsageDetail',
      }
    },
    {
      use: '@gridsome/source-filesystem',
      options: {
        path: 'personas/**/*.md',
        typeName: 'Persona'
      }
    },
    {
      use: '@gridsome/source-filesystem',
      options: {
        path: 'webpages/**/*.md',
        typeName: 'Webpage',
        refs: {
          personas: {
            typeName: 'Persona',
            route: 'personas/:id'
          }
        },
      }
    },
    {
      use: '@gridsome/source-filesystem',
      options: {
        path: 'ontologyPages/**/*.md',
        typeName: 'OntologyPage',
      }
    },
    {
      use: '@gridsome/source-filesystem',
      options: {
        path: 'usageDetails/**/*.md',
        typeName: 'UsageDetail',
      }
    },
    {
      use: 'gridsome-plugin-rss',
      options: {
        contentTypeName: 'Post',
        feedOptions: {
          title: 'BrickSchema',
          feed_url: 'https://brickschema.org/rss.xml',
          site_url: 'https://brickschema.org/'
        },
        feedItemOptions: node => ({
          title: node.title,
          description: node.summary,
          url: 'https://brickschema.org' + node.path,
          author: 'Shreyas Nagare',
          date: node.date
        }),
        output: {
          dir: './static',
          name: 'rss.xml'
        }
      }
    },
    {
      use: '@gridsome/plugin-sitemap',
      options: {
        cacheTime: 600000, // default
      }
    },
  ],
  transformers: {
    remark: {
      externalLinksTarget: '_blank',
      externalLinksRel: ['nofollow', 'noopener', 'noreferrer'],
      anchorClassName: 'icon icon-link',
      plugins: [
        ['remark-attr'],
        [ '@gridsome/remark-prismjs', { transformInlineCode: false } ],
        ['gridsome-plugin-remark-youtube', {width: '85%', align: 'auto'}],
      ]
    }
  },
  css: {
    loaderOptions: {
      postcss: {
        plugins: postcssPlugins,
      },
    },
  },
}
