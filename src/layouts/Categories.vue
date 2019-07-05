<template>
    <div>
        <ul>
            <g-link to="/apps" class="flex">
                <div class="title">
                    all
                </div>
                <div class="count">
                    {{$static.apps.total}}
                </div>
            </g-link>
            <g-link :to="category.node.path" class="flex" v-for="category in $static.categories.edges"
                    :key="category.node.id">
                <div class="title">
                    {{category.node.title}}
                </div>
                <div class="count">
                    {{category.node.belongsTo.totalCount}}
                </div>
            </g-link>
        </ul>

    </div>
</template>

<static-query>
    query getCategories{
    categories: allCategory (order: ASC){
    edges{
    node{
    title
    path
    belongsTo{
    totalCount
    }
    }
    }
    }
    apps: allApp{
    total:totalCount
    }
    }

</static-query>

<script>
    import SearchInput from '../components/SearchInput'
    import ThemeSwitcher from '../components/ThemeSwitcher'

    export default {
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
    .flex {
        font-size: 18px;
        padding: 8px;
        color: black
    }

    .title:hover {
        color: #4185f4;
    }

    .title {
        font-family: "Noto Sans";
        font-weight: lighter;
        width: 100%;
    }

    .count {
        margin-left: auto;
        padding: .15rem .4rem;
        border-radius: .3em;
        font-size: .6em;
        padding: 6px;
        text-align: center;
        background: rgb(218, 219, 219);
        width: 28px;
    }
</style>