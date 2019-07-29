<template>
    <div :id="classNode.name">
        <div class="text-3xl m-4">
            <g-link class="leading-tight mt-16 mb-8 mr-2 font-normal text-gray-700 hover:text-primary-700" :to="`${classNode.namespace.path}#${classNode.name}`">{{ classNode.namespace.value }}</g-link>:
            <span class="font-bold leading-tight mt-16 mb-8 mr-4">{{ classNode.generatedLabel }}</span>
            <span class="text-xs font-bold bg-primary-700 text-white my-auto mx-2 p-1 px-2 rounded font-left my-auto align-middle">{{ classNode.type.toUpperCase() }}</span>
            <span class="text-xs bg-primary-700 text-white my-auto mx-2 p-1 px-2 rounded my-auto align-middle">{{ `v${classNode.version}` }}</span>
        </div>


        <div class="block sm:flex text-gray-600">
            <div class="l-auto h-auto sm:w-1/6 h-12 bg-gray-100 rounded-lg  px-4 py-2 mt-4 ml-4">IRI</div>
            <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                <div class="rounded-lg px-4 py-2 mt-4 ml-4 iri">
                    <a class="font-normal text-gray-600 border-b" :href="'http://www.linked.data.gov.au/def/pylode/brick.html#'+classNode.id.split('#').pop().toLowerCase()" target="_blank">{{ classNode.id.split('^').pop() }}</a>
                </div>
            </div>
        </div>


        <div class="block sm:flex text-gray-600" v-if="classNode.types.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Type</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="type in classNode.types"
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


        <div class="block sm:flex text-gray-600" v-if="classNode.equivalentClasses.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Equivalent Classes</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="equivalentClass in classNode.equivalentClasses"
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


        <div class="block sm:flex text-gray-600" v-if="classNode.definitions.length && classNode.definitions[0].length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Definitions</div>
            <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                <div class="rounded-lg px-4 py-2 mt-4 ml-4 definition" :key="definition" v-for="definition in classNode.definitions">
                    {{definition}}
                </div>
            </div>
        </div>


        <div class="block sm:flex text-gray-600" v-if="classNode.superclasses.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Parent Classes</div>
            <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4" >
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="superclass in classNode.superclasses"
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


        <div class="block sm:flex text-gray-600" v-if="classNode.subclasses.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Subclasses</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="subclass in classNode.subclasses"
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


        <div class="block sm:flex text-gray-600" v-if="classNode.inDomainOf.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">InDomainOf</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="property in classNode.inDomainOf"
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


        <div class="block sm:flex text-gray-600" v-if="classNode.inRangeOf.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">InRangeOf</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="property in classNode.inRangeOf"
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
</template>

<script>
    export default {
        name: "ClassNode",
        props:{
            classNode: Object
        }
    }
</script>

<style scoped>

    .l-auto{
        width: -webkit-fill-available | max-content;
    }
    .b-auto{
        max-width: fit-content;
    }
</style>