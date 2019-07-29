<template>
    <div :id="relationshipNode.name">
        <div class="text-3xl m-4">
        <g-link class="leading-tight mt-16 mb-8 mr-2 font-normal text-gray-700 hover:text-primary-700" :to="`${relationshipNode.namespace.path}#${relationshipNode.name}`">{{ relationshipNode.namespace.value }}</g-link>:
        <span class="font-bold leading-tight mt-16 mb-8 mr-4">{{ relationshipNode.generatedLabel }}</span>
        <span class="text-xs font-bold bg-primary-700 text-white my-auto mx-2 p-1 px-2 rounded font-left my-auto align-middle">{{ relationshipNode.type.toUpperCase() }}</span>
        <span class="text-xs bg-primary-700 text-white my-auto mx-2 p-1 px-2 rounded my-auto align-middle">{{ `v${relationshipNode.version}` }}</span>
    </div>


        <div class="block sm:flex text-gray-600">
            <div class="l-auto h-auto sm:w-1/6 h-12 bg-gray-100 rounded-lg  px-4 py-2 mt-4 ml-4">IRI</div>
            <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                <div class="rounded-lg px-4 py-2 mt-4 ml-4 iri">
                    <a class="font-normal text-gray-600 border-b" :href="'http://www.linked.data.gov.au/def/pylode/brick.html#'+relationshipNode.id.split('#').pop().toLowerCase()" target="_blank">{{ relationshipNode.id.split('^').pop() }}</a>
                </div>
            </div>
        </div>


        <div class="block sm:flex text-gray-600" v-if="relationshipNode.definitions.length && relationshipNode.definitions[0].length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Definitions</div>
            <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto">
                <div class="rounded-lg px-4 py-2 mt-4 ml-4 definition" :key="definition" v-for="definition in relationshipNode.definitions">
                    {{definition}}
                </div>
            </div>
        </div>


        <div class="block sm:flex text-gray-600" v-if="relationshipNode.superProperties.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Parent Properties</div>
            <div class="l-auto h-auto sm:w-5/6  h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4" >
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="superclass in relationshipNode.superProperties"
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


        <div class="block sm:flex text-gray-600" v-if="relationshipNode.subProperties.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">SubProperties</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="subclass in relationshipNode.subProperties"
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


        <div class="block sm:flex text-gray-600" v-if="relationshipNode.inverseProperties.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Inverse</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="property in relationshipNode.inverseProperties"
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


        <div class="block sm:flex text-gray-600" v-if="relationshipNode.domain.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Domain</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="property in relationshipNode.domain"
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


        <div class="block sm:flex text-gray-600" v-if="relationshipNode.range.length">
            <div class="l-auto h-auto sm:w-1/6 bg-gray-100 h-12 rounded-lg  px-4 py-2 mt-4 ml-4">Range</div>
            <div class="l-auto h-auto sm:w-5/6 h-12 overflow-auto mt-2">
                <ul class="mb-8 text-normal text-gray-200 mt-4 ml-4">
                    <li class="text-l text-gray-600 mt-4 ml-4"
                        v-for="property in relationshipNode.range"
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
        name: "RelationshipNode",
        props:{
            relationshipNode: Object
        }
    }
</script>

<style scoped>

</style>