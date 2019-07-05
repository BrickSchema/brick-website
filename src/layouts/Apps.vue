<template>
    <div class="inline-flex">
        <a :href="app.node.url" target="_blank" class="card" v-for="app in (category? category : $static.apps.edges)"
           :key="app.id">
            <g-image :src="app.node.thumbnail.src" alt="Avatar" style="width:100%"/>
            <div class="container">
                <h4><b>{{app.node.title}}</b></h4>
                <p>{{app.node.summary}}</p>
            </div>
        </a>
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
        props: {
            category: {
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
        width: 240px;
        height: 320px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        border-radius: 5px; /* 5px rounded corners */
        overflow: scroll;
    }

    .card:hover {
        box-shadow: 0px 11px 9px 1px rgba(0, 0, 0, 0.2);
        transition: 0.3s;
    }

    /* Add rounded corners to the top left and the top right corner of the image */
    img {
        width: 240px;
        height: 240px;
        border-radius: 5px 5px 0 0;
    }

    .inline-flex {
        float: right;
        flex-flow: wrap;
    }

    a {
        color: #000;
        font-family: "Noto Sans";
        font-weight: lighter;
    }

    h4 {
        font-weight: bold;
        padding: 2px;
    }
</style>