<template>
    <Layout>

        <div class="mx-auto w-9/12">
            <div class="font-bold leading-tight mt-16 mb-8 ml-4 text-4xl" id="Relationships">Relationships</div>
            <div v-if="Object.keys(relationshipNode.node).length" v-for="relationshipNode in $page.namespace.belongsTo.relationships" class="border-t mb-8 pt-8">
                <relationship-node :relationship-node="relationshipNode.node" class="mt-0"></relationship-node>
            </div>
            <div class="font-bold leading-tight mt-16 mb-8 ml-4 text-4xl" id="Classes">Classes</div>
            <div v-if="Object.keys(classNode.node).length"  v-for="classNode in $page.namespace.belongsTo.classes" class="border-t mb-8 pt-8">
                <class-node :class-node="classNode.node" class="mt-0"></class-node>
            </div>
            <div v-for="usageDetail in $page.namespace.usageDetails">
                <div class="markdown-body mt-16 ml-4" v-html="usageDetail.content" />
            </div>
        </div>
    </Layout>
</template>

<page-query>

    query Namespace ($path: String!) {
    namespace: namespace (path: $path) {

    value
    id
    belongsTo{
    classes: edges{
    node{
    ...on Class{
    id
    name
    usageDetails{
    content
    }
    labels
    version
    generatedLabel
    definitions
    namespace{
    path
    value
    }
    type
    types
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
    hierarchy
    inDomainOf{
    generatedLabel
    path
    }
    inRangeOf{
    generatedLabel
    path
    }
    }
    }
    },
    relationships: edges{
    node{
    ...on Relationship{
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
    }
    }
    }
    }
    }
</page-query>

<script>
    import ClassNode from '../components/ClassNode'
    import RelationshipNode from '../components/RelationshipNode'
    export default {
        name: "Namespace",
        components:{
            ClassNode,
            RelationshipNode
        }
    }
</script>

<style scoped>

</style>