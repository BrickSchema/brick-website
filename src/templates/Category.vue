<template>
    <Layout>
        <div class="mx-auto py-16 px-4 sm:px-8">

            <h1 class="text-4xl ml-4 pb-2 font-bold leading-tight border-b border-primary-200">Tools: {{ $page.category.title }}</h1>

            <div class="w-full sm:flex text-xl text-gray-600 sm:mx-auto">
                <div class="h-auto border-b sm:border-b-0 sm:border-r border-primary-200">
                    <categories class="list"/>
                </div>
                <div class="w-full px-auto p-4">
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
            title: `Tools`
        },
        components: {
            Apps, Categories
        }
    }
</script>

