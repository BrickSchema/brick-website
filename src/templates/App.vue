<template>
    <Layout>

        <div class="container-inner mx-auto my-16">

            <div class="mb-8">
                <g-link to="/tools" class="font-bold uppercase">Back to Tools</g-link>
            </div>
            <h1 class="text-4xl font-bold leading-tight">{{ $page.app.title }}</h1>
            <a :href="$page.app.url" target="_blank" class="text-xl my-4">🔗 Website</a>
            <div class="flex my-8 text-sm overflow-hidden overflow-x-auto">
                <g-link
                        :to="category.path"
                        v-for="category in $page.app.categories"
                        :key="category.id"
                        class="bg-gray-300 rounded-full px-4 py-2 mr-4 hover:bg-primary-300">
                    {{ category.title }}
                </g-link>
            </div>
            <div class="markdown-body mb-8" v-html="$page.app.content"/>
            <div class="mb-8">
                <g-link to="/apps" class="font-bold uppercase">Back to Apps</g-link>
            </div>
        </div>
    </Layout>
</template>

<page-query>
    query App ($path: String!) {
        app: app (path: $path) {
            title
            url
            date (format: "MMMM D, Y")
            content
            categories {
                title
                path
            }
        }
    }
</page-query>

<script>
    export default {
        metaInfo() {
            return {
                title: this.$page.app.title
            }
        }
    }
</script>

<style src="../md.css" />
