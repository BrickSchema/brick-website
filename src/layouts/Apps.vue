<template>
    <div class="inline-flex">

        <g-link :to="app.node.path" class="card overflow-hidden m-4 bg-white" v-for="app in (category? category : $static.apps.edges)" :key="app.id" >
            <g-image class="border-b" :src="app.node.thumbnail.src" alt="Avatar"/>
            <div class="px-2 py-1 mx-auto">
                <div class="font-bold h-4/6 text-lg p-1">{{app.node.title}}</div>
                <div class="font-thin h-2/6 text-sm p-1">{{app.node.summary}}</div>
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
        margin: 24px;
        width: min-content;
        height: 320px;
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
        max-width: 220px;
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
</style>