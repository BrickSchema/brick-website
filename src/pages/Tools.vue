<template>
    <Layout>
        <div class="mx-auto py-16 px-4 sm:px-8">

            <h1 class="text-4xl ml-4 pb-2 font-bold leading-tight border-b border-primary-200">Tools</h1>

            <div class="w-full sm:flex text-xl text-gray-600 sm:mx-auto">
                <div class="h-auto sm:border-r border-primary-200">
                    <categories class="list"/>
                </div>
                <div class="w-full px-auto p-4">
                    <apps />
                </div>
            </div>

        </div>
    </Layout>
</template>

<script>
    import Apps from '../layouts/Apps'
    import Categories from '../layouts/Categories'


    export default {
        metaInfo: {
            title: 'Tools'
        },
        components: {
            Apps, Categories
        }
    }
</script>
