<template>
    <div class="relative">
        <div class="flex border-l border-b hover:bg-gray-100 pt-1"  v-bind:class="current ? 'bg-gray-200' : 'bg-white'" >
        <span @click="expanded=!expanded"
              v-if="!leaf"
              class="text-sm cursor-pointer"
        >{{expanded ? '&nbsp;➖' : '&nbsp;➕'}}</span>
        <g-link :to="`/tagsets/${id}`" class="px-2 rounded w-full font-thin text-sm flex">
            <span class="type" v-if="leaf">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <div class="w-auto text-left">{{ [...id.split('#')].pop().split('_').join(' ') }}</div>
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

