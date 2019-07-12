<template>
    <Layout>
        <div class="container-inner mx-auto py-16">

            <h1 class="text-4xl font-bold leading-tight">Tools</h1>

            <div class="w-full sm:flex text-xl text-gray-600 sm:mx-auto">
                <div class="l-auto h-auto rounded-lg ">
                    <categories class="list"/>
                </div>
                <div class="w-full px-auto bg-gray-100 ml-8">
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
