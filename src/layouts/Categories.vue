<template>
    <div>
        <ul>
            <g-link to="/tools" class="flex my-2">
                <div class="title font-thin text-sm text-md w-full mx-2">
                    ALL
                </div>
                <div class="count mr-2 bg-gray-200 text-xs rounded font-light align-middle px-2 mx-4">
                    {{$static.apps.total}}
                </div>
            </g-link>
            <g-link :to="category.node.path" class="flex my-2" v-for="category in $static.categories.edges" :key="category.node.id">
                <div class="title font-thin text-sm text-md w-full mx-2">
                    {{category.node.title.toUpperCase()}}
                </div>
                <div class="count mr-2 bg-gray-200 text-xs rounded font-light align-middle px-2 mx-4">
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