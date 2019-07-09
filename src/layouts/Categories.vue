<template>
    <div>
        <ul>
            <g-link to="/apps" class="flex font-light">
                <div class="title mx-4 mt-4 font-thin w-full">
                    all
                </div>
                <div class="count mt-4 mr-2 bg-gray-300 text-xs rounded font-light pt-1 align-middle px-2">
                    {{$static.apps.total}}
                </div>
            </g-link>
            <g-link :to="category.node.path" class="flex" v-for="category in $static.categories.edges" :key="category.node.id">
                <div class="title mx-4 font-thin text-md w-full">
                    {{category.node.title}}
                </div>
                <div class="count mr-2 bg-gray-300 text-xs rounded font-light pt-1 align-middle px-2">
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
    .flex{
        /*font-size: 18px;*/
        padding: 8px;
        color: black
    }

    .title:hover{
        color: #4185f4;
    }
</style>