<template>
    <Layout>

        <div class="container xs:flex-col sm:flex mx-auto my-16 overflow-x-hidden text-normal">

            <div class="l-auto pb-4 mx-4 w-80">
                <tag-set-search-input/>
                <recursive-tree
                    :hierarchyPath="$page.tagSet.hierarchy.map(c=>c.path.substring(9))" class="bg-gray-200"
                >
                </recursive-tree>
            </div>
            <div class=" l-auto w-full sm:border-l p-4 mx-4 z-5">
                <ul id="breadcrumbs" class="flex overflow-hidden overflow-x-auto">
                    <li
                            v-for="className in $page.tagSet.hierarchy"
                            :key="className.id">
                        <div class="h-100"></div>
                        <g-link
                                class="my-1 breadcrumb font-normal"
                                :to="className.path">
                            {{ className.generatedLabel }}
                        </g-link>
                        <div></div>
                    </li>
                </ul>

                <div class="font-bold leading-tight mt-16 mb-8 ml-4 text-3xl">
                    {{ $page.tagSet.generatedLabel }}
                </div>


                <div class="block sm:flex text-gray-600">
                    <div class="l-auto h-auto sm:w-1/6 h-12 bg-gray-100 rounded-lg  px-4 py-2 mt-4 ml-4">IRI</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                        <div class="rounded-lg px-4 py-2 mt-4 ml-4 iri">
                            <a class="font-normal text-gray-600 border-b" :href="'http://www.linked.data.gov.au/def/pylode/brick.html#'+$page.tagSet.id.split('#').pop().toLowerCase()" target="_blank">{{ $page.tagSet.id }}</a>
                        </div>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.tagSet.equivalentClasses.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Equivalent Classes</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                        <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="equivalentClass in $page.tagSet.equivalentClasses"
                                :key="equivalentClass.id">
                                <g-link
                                        :to="equivalentClass.path"
                                        class="block mr-4 text-gray-700 font-normal">
                                    {{ equivalentClass.generatedLabel }}
                                </g-link>
                            </li>
                        </ul>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.tagSet.definitions.length && $page.tagSet.definitions[0].length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Definitions</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                        <div class="rounded-lg px-4 py-2 mt-4 ml-4 definition" :key="definition" v-for="definition in $page.tagSet.definitions">
                            {{definition}}
                        </div>
                    </div>
                </div>


                <div class="block sm:flex text-gray-600" v-if="$page.tagSet.superclasses.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Parent Classes</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto mt-2">
                        <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4" >
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="superclass in $page.tagSet.superclasses"
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


                <div class="block sm:flex text-gray-600" v-if="$page.tagSet.subclasses.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Subclasses</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                        <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                            <li class="text-l text-gray-600 mt-4 ml-4"
                                v-for="subclass in $page.tagSet.subclasses"
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

            </div>
        </div>
    </Layout>
</template>

<page-query>
    query TagSet ($path: String!) {
    tagSet: tagSet (path: $path) {
    id
    labels
    generatedLabel
    definitions
    superclasses(sortBy:"generatedLabel", order:ASC){
    generatedLabel
    path
    }
    subclasses(sortBy:"generatedLabel", order:ASC){
    generatedLabel
    path
    }
    equivalentClasses(sortBy:"generatedLabel", order:ASC){
    generatedLabel
    path
    }
    hierarchy{
    generatedLabel
    path
    }
    }
    }
</page-query>

<script>

    import RecursiveTree from '../components/RecursiveTree'
    import TagSetSearchInput from '../components/TagSetSearchInput'
    export default {
        components: {
            TagSetSearchInput,
            RecursiveTree
        },
        metaInfo() {
            return {
                title: this.$page.tagSet.generatedLabel
            }
        }
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

