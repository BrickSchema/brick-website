<template>

    <Layout>
        <div class="container mx-auto">
            <iframe src="https://brick.andrew.cmu.edu/docs" width="0" height="0"></iframe>
            <!--        <search/>-->
        </div>
    </Layout>
</template>

<script>
    // import Search from '../components/Search.vue'
    // import BootstrapVue from 'bootstrap-vue'
    //
    // // import 'bootstrap/dist/css/bootstrap.css'
    // // import 'bootstrap-vue/dist/bootstrap-vue.css'
    // Vue.use(BootstrapVue)
    // import Vue from 'vue';
    // import BreathingColors from 'vue-breathing-colors';
    //
    // import VueTextareaAutosize from 'vue-textarea-autosize'
    // import VueProgressBar from 'vue-progressbar'
    //
    // Vue.use(VueProgressBar, {
    //   color: '#007bff',
    //   failedColor: 'red',
    //   height: '8px'
    // })
    // Vue.use(VueTextareaAutosize)
    // Vue.use(BreathingColors);
    //
    // export default {
    //     metaInfo: {
    //         title: 'Docs'
    //     },
    //   data() {
    //     return {
    //       sample: {
    //         colors: ['white'],
    //         interval: 3000,
    //         transition: {
    //           duration: 1000
    //         }
    //       }
    //     }
    //   },
    //   components: {
    //     Search
    //   }
    // }
</script>

<style scoped>
    /*.container {*/
    /*  margin: 0 auto;*/
    /*  !*min-height: 100vh;*!*/
    /*  display: unset;*/
    /*  justify-content: center;*/
    /*  align-items: center;*/
    /*  text-align: center;*/
    /*  height: 100%;*/
    /*  width:100%;*/
    /*}*/

    /*.title {*/
    /*  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,*/
    /*  'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;*/
    /*  display: block;*/
    /*  font-weight: 300;*/
    /*  font-size: 6em;*/
    /*  color: #35495e;*/
    /*  letter-spacing: 1px;*/
    /*  background: -webkit-linear-gradient(#57a2ff, #49b3b3);*/
    /*  -webkit-background-clip: text;*/
    /*  -webkit-text-fill-color: transparent;*/
    /*}*/

    /*.subtitle {*/
    /*  font-weight: 300;*/
    /*  font-size: 2em;*/
    /*  color: #526488;*/
    /*  !*word-spacing: 5px;*!*/
    /*  padding-bottom: 15px;*/
    /*  margin-bottom: 16px;*/
    /*}*/

    /*.links {*/
    /*  padding-top: 15px;*/
    /*}*/


    /*.v--modal-background-click{*/
    /*  background: #0579fc30;*/
    /*}*/

    /*div{*/
    /*  overflow-y: scroll;*/
    /*  overflow-x: hidden;*/
    /*  width: 100%;*/
    /*}*/

    /*search{*/
    /*  width: 100%;*/
    /*}*/

    iframe {
        width: -webkit-fill-available;
        height: -webkit-fill-available;
    }
</style>
