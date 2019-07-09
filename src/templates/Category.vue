<template>
    <Layout>
        <div class="mx-auto py-16 w-5/6">

            <h1 class="text-4xl font-bold leading-tight m-8">Category: {{$page.category.title}}</h1>

            <div class="w-full sm:flex text-xl text-gray-600 mx-auto">
                <div class="l-auto h-auto md:w-1/6 h-12 bg-gray-200 rounded-lg  px-4 py-2 m-8">
                    <categories class="list"/>
                </div>
                <div class="w-full h-auto md:w-5/6 h-12 overflow-auto bg-gray-100 rounded-lg px-auto py-2 md:m-8">
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