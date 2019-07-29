<template>
    <Layout>

        <div class="container xs:flex-col sm:flex mx-auto my-16 overflow-x-hidden text-normal">

            <div class="l-auto pb-4 mx-4 w-80">
                <ontology-search-input :version="$page.class.version" />
                <div>
                    <div v-if="false" class="flex">
                    <span @click="expanded=!expanded" v-if="tree.length"
                          class="text-normal px-2 cursor-pointer">{{expanded ? '▾' : '▸'}}</span>
                        <span v-else class="type">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

                        <div>{{getName(tree.name)}}</div>
                    </div>

                    <g-link v-if="expanded" v-for="branch in tree" :key="branch.name" class="flex" :to="branch.name">
                        <hierarchy-tree :tree="branch" :hierarchy="$page.class.hierarchy"></hierarchy-tree>
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
                            Ontology
                        </g-link>
                    </li>
                    <li>
                        <div class="h-100"></div>
                        <g-link
                                class="my-1 breadcrumb font-normal"
                                :to="`/ontology/${$page.class.version}`">
                            v{{ $page.class.version }}
                        </g-link>
                    </li>
                    <li
                            v-for="className in $page.class.hierarchy"
                            :key="className">
                        <div class="h-100"></div>
                        <g-link
                                class="my-1 breadcrumb font-normal"
                                :to="className">
                            {{ className.split('/').pop().split('#').pop().split('_').join(' ') }}
                        </g-link>
                    </li>
                </ul>
                <div class="text-3xl m-4">
                    <g-link class="leading-tight mt-16 mb-8 mr-2 font-normal text-gray-700 hover:text-primary-700" :to="`${$page.class.namespace.path}#${$page.class.name}`">{{ $page.class.namespace.value }}</g-link>:
                    <span class="font-bold leading-tight mt-16 mb-8 mr-4">{{ $page.class.generatedLabel }}</span>
                    <span class="text-xs font-bold bg-primary-700 text-white my-auto mx-2 p-1 px-2 rounded font-left my-auto align-middle">{{ $page.class.type.toUpperCase() }}</span>
                    <span class="text-xs bg-primary-700 text-white my-auto mx-2 p-1 px-2 rounded my-auto align-middle">{{ `v${$page.class.version}` }}</span>
                </div>


                <div class="block sm:flex text-gray-600">
                    <div class="l-auto h-auto sm:w-1/6 h-12 bg-gray-100 rounded-lg  px-4 py-2 mt-4 ml-4">IRI</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                        <div class="rounded-lg px-4 py-2 mt-4 ml-4 iri">
                            <a class="font-normal text-gray-600 border-b" :href="'http://www.linked.data.gov.au/def/pylode/brick.html#'+$page.class.id.split('#').pop().toLowerCase()" target="_blank">{{ $page.class.id.split('^').pop() }}</a>
                        </div>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.class.types.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Type</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                        <ul class="text-normal text-gray-200 mt-4 ml-4">
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="type in $page.class.types"
                                :key="type">
                                <a
                                        :href="type"
                                        class="block mr-4 text-gray-700 font-normal">
                                    {{ type.split('#').pop() }}
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.class.definitions.length && $page.class.definitions[0].length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Definitions</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                        <div class="rounded-lg px-4 py-2 mt-4 ml-4 definition" :key="definition" v-for="definition in $page.class.definitions">
                            {{definition}}
                        </div>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.class.superProperties.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Parent Properties</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto mt-2">
                        <ul class="text-normal text-gray-200 mt-4 ml-4" >
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="superclass in $page.class.superProperties"
                                :key="superclass.id">
                                <g-link
                                        :to="superclass.path"
                                        class="block mr-4 text-gray-700 font-normal">
                                    {{ superclass.generatedLabel }}
                                </g-link>
                            </li>

                        </ul>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.class.subProperties.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">SubProperties</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                        <ul class="text-normal text-gray-200 mt-4 ml-4">
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="subclass in $page.class.subProperties"
                                :key="subclass.id">
                                <g-link
                                        :to="subclass.path"
                                        class="block mr-4 text-gray-700 font-normal">
                                    {{ subclass.generatedLabel }}
                                </g-link>
                            </li>
                        </ul>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.class.inverseProperties.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Inverse</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                        <ul class="text-normal text-gray-200 mt-4 ml-4">
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="property in $page.class.inverseProperties"
                                :key="property.id">
                                <g-link
                                        :to="property.path"
                                        class="block mr-4 text-gray-700 font-normal">
                                    {{ property.generatedLabel }}
                                </g-link>
                            </li>
                        </ul>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.class.domain.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Domain</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                        <ul class="text-normal text-gray-200 mt-4 ml-4">
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="property in $page.class.domain"
                                :key="property.id">
                                <g-link
                                        :to="property.path"
                                        class="block mr-4 text-gray-700 font-normal">
                                    {{ property.generatedLabel }}
                                </g-link>
                            </li>
                        </ul>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.class.range.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Range</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                        <ul class="text-normal text-gray-200 mt-4 ml-4">
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="property in $page.class.range"
                                :key="property.id">
                                <g-link
                                        :to="property.path"
                                        class="block mr-4 text-gray-700 font-normal">
                                    {{ property.generatedLabel }}
                                </g-link>
                            </li>
                        </ul>
                    </div>
                </div>

            </div>
        </div>
    </Layout>
</template>

<page-query>
    query Relationship ($path: String!){
    class: relationship (path: $path) {
    id
    generatedLabel
    definitions
    name
    namespace{
    path
    value
    }
    version
    type
    types
    superProperties(sortBy:"generatedLabel", order:ASC){
    generatedLabel
    path
    }
    subProperties(sortBy:"generatedLabel", order:ASC){
    generatedLabel
    path
    }
    inverseProperties(sortBy:"generatedLabel", order:ASC){
    generatedLabel
    path
    }
    hierarchy
    domain{
    generatedLabel
    path
    }
    range{
    generatedLabel
    path
    }

    }
    metaData{
    pathPrefix
    }
    }
</page-query>

<script>
    import axios from 'axios'
    // import RecursiveTree from '../components/RecursiveTree'
    import HierarchyTree from '../components/HierarchyTree'
    import OntologySearchInput from '../components/OntologySearchInput'
    export default {
        components: {
            OntologySearchInput,
            // RecursiveTree,
            HierarchyTree
        },
        data(){
            return{
                tree: Object,
                expanded: true
            }
        },
        metaInfo() {
            return {
                title: this.$page.class.generatedLabel
            }
        },
        created() {
            axios(`${this.$page.metaData.pathPrefix}/ontology/${this.$page.class.version}/tree.json`).then(response => {
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

</style>

