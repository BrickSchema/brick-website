<template>
    <div class="border-l w-full" v-bind:class="current?'bg-gray-200':'bg-white'">
        <div v-if="tree.name" class="flex text-black font-thin">
            <span @click.prevent="expanded=!expanded" v-if="tree.children && tree.children.length"
                   class="text-normal px-2 cursor-pointer">{{expanded ? '▾' : '▸'}}</span>
            <span v-else class="type">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

            <div class="font-thin text-gray-700 hover:text-primary-700 text-left w-full">{{getName(tree.name)}}</div>
        </div>

        <g-link v-if="expanded" v-for="branch in tree.children" :key="branch.name" class="flex ml-6 border-t" :to="branch.name">
            <hierarchy-tree :tree="branch" :hierarchy="hierarchy"></hierarchy-tree>
        </g-link>
    </div>
</template>

<static-query>
    {
    metadata{
    pathPrefix
    }
    }
</static-query>

<script>
    import HierarchyTree from '../components/HierarchyTree'

    export default {
        name: 'HierarchyTree',
        props:{
            tree: Object,
            hierarchy: Array,
            bgDark: true
        },
        components:{
            HierarchyTree
        },
        data() {
            return {
                expanded: false,
                current: false
            }
        },
        watch:{
            hierarchy: function () {
                this.expanded = this.hierarchy.includes(this.tree.name);
                this.current = ([...this.hierarchy].pop()==this.tree.name)
            }
        },
        methods:{
            getName(str){
                return str ? str.split('/').pop().split('#').pop().split('_').join(' ') : ''
            }
        },
        created() {
            this.expanded = this.hierarchy.includes(this.tree.name);
            this.current = ([...this.hierarchy].pop()==this.tree.name)
            // console.log(([...this.hierarchy].pop(),this.tree.name))
        }
    }
</script>


