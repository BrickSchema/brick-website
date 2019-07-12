<template>
    <div>
        <ul>
            <g-link to="/tools" class="flex bg-gray-200 my-4 rounded-sm">
                <div class="title font-thin text-sm text-md w-full mx-4">
                    ALL
                </div>
                <div class="count mr-2 bg-gray-300 text-xs rounded font-light align-middle px-2 mx-4">
                    {{$static.apps.total}}
                </div>
            </g-link>
            <g-link :to="category.node.path" class="flex bg-gray-200 my-4 rounded-sm" v-for="category in $static.categories.edges" :key="category.node.id">
                <div class="title font-thin text-sm text-md w-full mx-4">
                    {{category.node.title.toUpperCase()}}
                </div>
                <div class="count mr-2 bg-gray-300 text-xs rounded font-light align-middle px-2 mx-4">
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

    export default {
        components: {
            SearchInput
        },
        data() {
            return {
                isOpen: false
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
    .flex{
        /*font-size: 18px;*/
        padding: 8px;
        color: black
    }

    .title:hover{
        color: #4185f4;
    }
</style>