<template>
    <Layout>

        <div class="container xs:flex-col sm:flex mx-auto my-16 overflow-x-hidden text-normal">

            <div class="l-auto pb-4 mx-4 w-80">
                <ontology-search-input :version="version" />

                <div class="h-auto">
                    <div v-if="false" class="flex">
                    <span @click="expanded=!expanded" v-if="tree && tree.length"
                          class="text-normal px-2 cursor-pointer">{{expanded ? '▾' : '▸'}}</span>
                        <span v-else class="type">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                        <div>{{getName(tree.name)}}</div>
                    </div>

                    <g-link v-if="expanded" v-for="branch in tree" :key="branch.name" class="flex" :to="branch.name">
                        <hierarchy-tree :tree="branch" :hierarchy="[`/ontology/${version}/#Classes`,`/ontology/${version}/#Relationships`,`/ontology/${version}/#EntityProperties`,`/ontology/${version}/#Shapes`, ``]"></hierarchy-tree>
                    </g-link>
                </div>
            </div>
            <div class=" l-auto w-full sm:border-l p-4 mx-4 z-5">
                <ul id="breadcrumbs" class="flex overflow-hidden overflow-x-auto">
                    <li>
                        <div class="h-100"></div>
                        <g-link
                                class="my-1 breadcrumb font-normal"
                                to="/ontology">
                            Brick
                        </g-link>
                        <div></div>
                    </li>
                </ul>

                <ul class="text-xl container-inner mx-auto my-16">
                    <div class="text-4xl font-bold mb-12">Brick Ontology</div>
                    <div class="text-3xl font-bold mb-8 w-full border-b-2 pb-4">Versions</div>
                    <div class="text-2xl font-bold">
                        <li class="mb-6">
                            <g-link to="/ontology/nightly">Nightly</g-link>
                        </li>
                        <li class="mb-6">
                            <g-link to="/ontology/1.2">v1.2</g-link>
                        </li>
                        <li class="mb-6">
                            <g-link to="/ontology/1.1">v1.1</g-link>
                        </li>
                        <li>
                            <g-link to="/ontology/1.0.3">v1.0.3</g-link>&nbsp;(no longer supported)
                        </li>
                    </div>
                </ul>

            </div>
        </div>
    </Layout>
</template>

<page-query>
    query{

    metadata{
    pathPrefix
    cacheVersion
    }

    }
</page-query>

<script>
    import axios from 'axios'
    import HierarchyTree from '../components/HierarchyTree'
    import OntologySearchInput from '../components/OntologySearchInput'
    export default {
        components: {
            OntologySearchInput,
            HierarchyTree
        },
        data(){
            return{
                tree: Object,
                expanded: true,
                version: '1.2'
            }
        },
        metaInfo() {
            return {
                title: 'Ontology'
            }
        },
        created() {
            axios(`${this.$page.metadata.pathPrefix}/ontology/${this.version}/tree.json?version=${this.$page.metadata.cacheVersion}`).then(response => {
                this.tree = response.data;
            })
                .catch(error => {
                    console.log(error);
                })
        },
    }
</script>

<style scoped>

    .list{

        display: flex;
        flex-flow: wrap;
        flex-direction: row;
    }

    .iri{
        word-break: break-all;;
    }

    .definition{
        word-break: break-word;;
    }

    .l-auto{
        width: -webkit-fill-available | max-content;
    }

    .breadcrumb{
        width: max-content;
    }


    #breadcrumbs{
        width: 100%;
        flex-flow: wrap;
    }

    #breadcrumbs li{
        float: left;
        margin: 0 .5em 0 1em;
    }

    #breadcrumbs a{
        background: #edf2f7;
        padding: .3em 1em;
        float: left;
        text-decoration: none;
        /*color: #444;*/
        /*color: #edf2f7;*/
        text-shadow: 0 1px 0 rgba(255,255,255,.5);
        position: relative;
    }

    #breadcrumbs a:hover{
        /*background: #99db76;*/
    }

    #breadcrumbs a::before{
        content: "";
        position: absolute;
        top: 50%;
        margin-top: -1.05em;
        border-width: 1.05em 0 1.05em 1em;
        border-style: solid;
        border-color: #edf2f7 #edf2f7 #edf2f7 transparent;
        left: -1em;
    }

    #breadcrumbs a:hover::before{
        /*border-color: #99db76 #99db76 #99db76 transparent;*/
    }

    #breadcrumbs a::after{
        content: "";
        position: absolute;
        top: 50%;
        margin-top: -1.05em;
        border-top: 1.05em solid transparent;
        border-bottom: 1.05em solid transparent;
        border-left: 1em solid #edf2f7;
        right: -1em;
    }

    #breadcrumbs a:hover::after{
        /*border-left-color: #99db76;*/
    }

    #breadcrumbs .current,
    #breadcrumbs .current:hover{
        font-weight: bold;
        background: none;
    }

    #breadcrumbs .current::after,
    #breadcrumbs .current::before{
        content: normal;
    }
    div{
        text-align: left;
    }

</style>
