<template>
    <Layout>
        <div class="container-inner mx-auto py-16">

            <h1 class="text-4xl font-bold leading-tight">Tools</h1>

            <div class="w-full sm:flex text-xl text-gray-600 sm:mx-auto">
                <div class="l-auto h-auto rounded-lg ">
                    <categories class="list"/>
                </div>
                <div class="w-full px-auto bg-gray-100 ml-8">
                    <apps :category=$page.category.belongsTo.apps />
                </div>
            </div>

        </div>
    </Layout>
</template>

<page-query>
    query Category ($id: String!) {
    category: category (id: $id) {
    title
    belongsTo{
    totalCount
    pageInfo {
    totalPages
    currentPage
    }
    apps:edges {
    node {
    ...on App {
    title
    path
    summary
    thumbnail
    url
    }
    }
    }
    }
    }
    }
</page-query>

<script>
    import Apps from '../layouts/Apps'
    import Categories from '../layouts/Categories'


    export default {
        metaInfo: {
            title: 'Apps'
        },
        components: {
            Apps, Categories
        }
    }
</script>

