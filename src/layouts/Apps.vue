<template>
    <div class="inline-flex w-full">

        <g-link :to="app.node.path" class="card w-full flex overflow-hidden bg-white mx-auto border-primary-200 border mb-4" v-for="app in (category? category : $static.apps.edges)" :key="app.id" >
            <g-image class="my-auto h-full w-full" :src="app.node.thumbnail.src" alt="Avatar"/>
            <div class="border-t md:border-t-0 md:border-l px-2 py-1 mx-auto details">
                <div class="font-bold text-lg p-1">{{app.node.title}}</div>
                <div class="font-thin text-sm p-1">{{app.node.summary}}</div>
            </div>
        </g-link>
    </div>
</template>

<static-query>
    query Apps {
    apps: allApp{
    totalCount
    edges {
    node {
    id
    title
    summary
    path
    thumbnail
    url
    }
    }
    }
    }
</static-query>

<script>
    import SearchInput from '../components/SearchInput'

    export default {
        props:{
            category:{
                default: false
            }
        },
        components: {
            SearchInput
        },
        data() {
            return {
                isOpen: false,
            }
        },
        methods: {
            toggle() {
                this.isOpen = !this.isOpen
            }
        }
    }
</script>

<style scoped>
    .card {
        max-height: 340px;
        box-shadow: 0 4px 8px 0 rgba(255, 255, 255,0.25);
        transition: 0.3s;
        border-radius: 5px; /* 5px rounded corners */
    }

    .card:hover{
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.0625);
        transition: 0.1s;
    }

    /* Add rounded corners to the top left and the top right corner of the image */
    img {
        width: 120px;
        height: 120px;
        border-radius: 5px 5px 0 0;
    }

    .inline-flex{
        float: left;
        flex-flow: wrap;
    }
    a{
        color: #000;
        font-weight: lighter;
    }

    .details{
        width: inherit;
        height: auto;
    }
</style>