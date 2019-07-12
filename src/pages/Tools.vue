<template>
    <Layout>
        <div class="mx-auto py-16 w-5/6">

            <h1 class="text-4xl font-bold leading-tight m-8">Tools</h1>

            <div class="w-full sm:flex text-xl text-gray-600 mx-auto">
                <div class="l-auto h-auto h-12 bg-gray-200 rounded-lg  px-4 py-2 m-8">
                    <categories class="list"/>
                </div>
                <div class="w-full h-auto h-12 overflow-auto bg-gray-100 rounded-lg px-auto py-2 md:m-8">
                    <apps/>
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
