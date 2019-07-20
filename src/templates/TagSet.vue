<template>
    <Layout>

        <div class="container xs:flex-col sm:flex mx-auto my-16 overflow-x-hidden">

            <div class="l-auto pb-4 mx-4">
                <tag-set-search-input/>
                <recursive-tree
                    :hierarchyPath="$page.tagSet.hierarchy.map(c=>c.path.substring(9))"
                >
                </recursive-tree>
            </div>
            <div class=" l-auto w-full bg-gray-100 p-4 rounded-lg mx-4 z-5">
                <ul id="breadcrumbs" class="flex overflow-hidden overflow-x-auto">
                    <li
                            v-for="className in $page.tagSet.hierarchy"
                            :key="className.id">
                        <div class="h-100"></div>
                        <g-link
                                class="my-1 bg-gray-200 breadcrumb"
                                :to="className.path">
                            {{ className.generatedLabel }}
                        </g-link>
                        <div></div>
                    </li>
                </ul>

                <h1 class="text-4xl font-bold leading-tight m-8">
                    {{ $page.tagSet.generatedLabel }}
                </h1>


                <div class="block sm:flex text-xl text-gray-600">
                    <div class="l-auto h-auto sm:w-1/6 h-12 bg-gray-300 rounded-lg  px-4 py-2 m-8">IRI</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                        <div class="bg-gray-200 rounded-lg px-4 py-2 m-8 iri">
                            <a :href="'http://www.linked.data.gov.au/def/pylode/brick.html#'+$page.tagSet.id.split('#').pop().toLowerCase()" target="_blank">{{ $page.tagSet.id }}</a>
                        </div>
                    </div>
                </div>


                <div class="block sm:flex text-xl text-gray-600" v-if="$page.tagSet.equivalentClasses.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-300 h-12 rounded-lg  px-4 py-2 m-8">Equivalent Classes</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto">
                        <ul class="list mb-8 text-sm text-xl text-gray-200 m-4">
                            <li class="text-l text-gray-600 m-4"
                                v-for="equivalentClass in $page.tagSet.equivalentClasses"
                                :key="equivalentClass.id">
                                <g-link
                                        :to="equivalentClass.path"
                                        class="block bg-gray-200 rounded-full px-4 py-2 mr-4 hover:bg-primary-200">
                                    {{ equivalentClass.generatedLabel }}
                                </g-link>
                            </li>
                        </ul>
                    </div>
                </div>


                <div class="block sm:flex text-xl text-gray-600" v-if="$page.tagSet.definitions.length && $page.tagSet.definitions[0].length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-300 h-12 bg-gray-200 rounded-lg  px-4 py-2 m-8">Definitions</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                        <div class="bg-gray-200 rounded-lg px-4 py-2 m-8 definition" :key="definition" v-for="definition in $page.tagSet.definitions">
                            {{definition}}
                        </div>
                    </div>
                </div>


                <div class="block sm:flex text-xl text-gray-600" v-if="$page.tagSet.superclasses.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-300 h-12 rounded-lg  px-4 py-2 m-8">Parent Classes</div>
                    <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                        <ul class="list mb-8 text-sm text-xl text-gray-200 m-4" >
                            <li class="text-l text-gray-600 m-4"
                                v-for="superclass in $page.tagSet.superclasses"
                                :key="superclass.id">
                                <g-link
                                        :to="superclass.path"
                                        class="block bg-gray-200 rounded-full px-4 py-2 mr-4 hover:bg-primary-200">
                                    {{ superclass.generatedLabel }}
                                </g-link>
                            </li>

                        </ul>
                    </div>
                </div>


                <div class="block sm:flex text-xl text-gray-600" v-if="$page.tagSet.subclasses.length">
                    <div class="l-auto h-auto sm:w-1/6 bg-gray-300 h-12 rounded-lg  px-4 py-2 m-8">Subclasses</div>
                    <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto">
                        <ul class="list mb-8 text-sm text-xl text-gray-200 m-4">
                            <li class="text-l text-gray-600 m-4"
                                v-for="subclass in $page.tagSet.subclasses"
                                :key="subclass.id">
                                <g-link
                                        :to="subclass.path"
                                        class="block bg-gray-200 rounded-full px-4 py-2 mr-4 hover:bg-primary-200">
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
    superclasses(sortBy:"totalChildren", order:DESC){
    generatedLabel
    path
    }
    subclasses(sortBy:"totalChildren", order:DESC){
    generatedLabel
    path
    }
    equivalentClasses(sortBy:"totalChildren", order:DESC){
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
        background: #e2e8f0;
        padding: .7em 1em;
        float: left;
        text-decoration: none;
        /*color: #444;*/
        /*color: #e2e8f0;*/
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
        margin-top: -1.45em;
        border-width: 1.4em 0 1.5em 1em;
        border-style: solid;
        border-color: #e2e8f0 #e2e8f0 #e2e8f0 transparent;
        left: -1em;
    }

    #breadcrumbs a:hover::before{
        /*border-color: #99db76 #99db76 #99db76 transparent;*/
    }

    #breadcrumbs a::after{
        content: "";
        position: absolute;
        top: 50%;
        margin-top: -1.45em;
        border-top: 1.4em solid transparent;
        border-bottom: 1.5em solid transparent;
        border-left: 1em solid #e2e8f0;
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

