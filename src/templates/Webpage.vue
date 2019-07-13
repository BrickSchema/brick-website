<template>
    <Layout>
        <div class="container-inner mx-auto my-16">
            <h1 class="text-4xl font-bold leading-tight">{{ $page.webpage.title }}</h1>
            <div class="markdown-body my-16 " v-html="$page.webpage.content" />
        </div>
    </Layout>
</template>

<page-query>
    query Webpage ($path: String!) {
        webpage: webpage (path: $path) {
            title
            content
        }
    }
</page-query>

<script>
    export default {
        metaInfo() {
            return {
                title: this.$page.webpage.title
            }
        }
    }
</script>

<style src="../md.css" />
