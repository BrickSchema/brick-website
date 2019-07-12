<template>
    <div class="inline-flex p-4">

        <g-link :to="app.node.path" class="card md:flex overflow-hidden sm:m-4 bg-white mx-auto" v-for="app in (category? category : $static.apps.edges)" :key="app.id" >
            <g-image class="my-auto" :src="app.node.thumbnail.src" alt="Avatar"/>
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
    import ThemeSwitcher from '../components/ThemeSwitcher'

    export default {
        props:{
            category:{
                default: false
            }
        },
        components: {
            SearchInput,
            ThemeSwitcher
        },
        mounted() {
            this.theme = localStorage.getItem('theme') || 'theme-light'
        },
        data() {
            return {
                isOpen: false,
                theme: '',
            }
        },
        methods: {
            toggle() {
                this.isOpen = !this.isOpen
            },
            updateTheme(theme) {
                this.theme = theme
            }
        }
    }
</script>

<style scoped>
    .card {
        /*margin: auto;*/
        margin-bottom: 24px;
        /*width: -moz-available;*/
        max-height: 340px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        border-radius: 5px; /* 5px rounded corners */
    }

    .card:hover{
        box-shadow: 0px 11px 9px 1px rgba(0,0,0,0.2);
        transition: 0.3s;
    }

    /* Add rounded corners to the top left and the top right corner of the image */
    img {
        height: 240px;
        width: 240px;
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
        width: 240px;
        height: auto;
    }
</style>