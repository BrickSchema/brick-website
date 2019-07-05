<template>
    <Layout>
        <div class="container-inner mx-auto py-16">
            <div class="apps flex">
                <div>
                    <categories class="list"/>

                </div>
                <apps class="flex-grow"/>
            </div>
        </div>
    </Layout>
</template>

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

<style scoped>
    .container-inner {
        margin: auto;
        display: contents;
        width: auto;
    }

    .flex-grow {
        /*margin-left: 124px;*/
        width: 70%;
    }

    .list {
        width: 256px;
        /*max-width: 100%;*/
    }

    .apps {
        float: left;
        margin: 64px;
        padding: 20px;
        margin-top: 64px;
        flex-flow: wrap;
        display: inline-box;
    }
</style>
