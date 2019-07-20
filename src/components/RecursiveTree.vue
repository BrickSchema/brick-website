<template>
    <div class="relative">
        <div class="flex">
        <span @click="expanded=!expanded"
              v-if="!leaf"
              class="text-sm"
        >{{expanded ? '&#9660;' : '&#9658;'}}</span>
        <span class="type" v-else>&nbsp;</span>
        <g-link :to="`/tagsets/${id}`" v-bind:class="current ? 'bg-gray-200' : 'bg-white'" class="px-2 rounded w-full hover:bg-gray-100">
            <div class="w-auto">&nbsp;{{ [...id.split('#')].pop() }}</div>
        </g-link>
    </div>
        <div v-if="expanded" :style="`margin-left: 20px`" v-for="tagset in hierarchy.subclasses" :key="tagset">
            <recursive-tree :id="[...tagset.split('#')].pop()" :hierarchyPath="hierarchyPath"></recursive-tree>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import RecursiveTree from '../components/RecursiveTree'

    export default {
        name: 'RecursiveTree',
        props:{
            id:{
                default: 'TagSet'
            },
            hierarchyPath:{
                default: ''
            }
        },
        watch:{
            hierarchyPath: function () {
                this.expanded = this.hierarchyPath.includes([...this.id.split('#')].pop());
                this.current = ([...this.hierarchyPath].pop()===([...this.id.split('#')].pop()))
            }
        },
        components:{
          RecursiveTree
        },
        data() {
            return {
                loaded: false,
                hierarchy: {subclasses:[]},
                leaf: false,
                expanded:true,
                current: ([...this.hierarchyPath].pop()===([...this.id.split('#')].pop()))
            }
        },
        created() {
            axios(`/hierarchy/${this.id.split('#').pop()}.json`).then(response => {
            this.hierarchy = response.data;
            this.loaded = true;
            this.expanded = this.hierarchyPath.includes(this.id.split('#').pop());
            if(!response.data.subclasses.length){
                this.leaf = true;
            }
        })
            .catch(error => {
                console.log(error);
            })
        }
    }
</script>

