<template>
    <div class="relative">
        <div class="flex hover:bg-gray-100 border-gray-100"
             v-bind:class="[(current ? 'bg-gray-200' : 'bg-white') , (expanded ? 'border-b-4' : 'border-b-0')]" >
        <span @click="expanded=!expanded"
              v-if="!leaf"
              class="text-normal     cursor-pointer" v-bind:class="!darkerBg? 'bg-gray-100' : ''"
        >{{expanded ? '&nbsp;➖' : '&nbsp;➕'}}</span>
        <g-link :to="`/tagsets/${id}`" class="rounded w-full font-thin text-normal flex">
            <span class="type" v-if="leaf"  v-bind:class="[(current ? 'bg-gray-200' : 'bg-white') , (!darkerBg? 'bg-gray-100' : 'bg-white')]">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <div class="w-auto text-left ml-1">{{ [...id.split('#')].pop().split('_').join(' ') }}</div>
        </g-link>
    </div>
        <div v-if="expanded" class="ml-6" v-for="tagset in hierarchy.subclasses" :key="tagset" v-bind:class="darkerBg? 'bg-gray-100' : 'bg-white'">
            <recursive-tree :id="[...tagset.split('#')].pop()" :hierarchyPath="hierarchyPath" :darker-bg="!darkerBg"></recursive-tree>
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
            },
            darkerBg:{
                default: false
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

