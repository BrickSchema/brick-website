<template>
    <Layout>
        <div class="container-inner mx-auto py-16">
            <h1 class="text-4xl font-bold mb-16">Get Started</h1>
            <div class="overflow-x-hidden">
                <div class="container-inner mx-auto text-xl border-t border-gray-500 border-b py-16 relative">
                    <h2 class="text-3xl font-bold mb-16">Learning Materials</h2>

                    <div class="absolute right-0" style="top: 50px; transform: translate(100%) rotate(180deg)">
                        <svg width="170px" height="170px">
                            <use xlink:href="#dots-triangle"/>
                        </svg>
                    </div>

                    <ul class="text-lg sm:text-xl">
                        <li class=" mb-6">
                            <a href="https://brickschema.org/docs/Brick-Leaflet.pdf">Brick Whitepaper</a>
                            <div class="text-lg text-gray-600">Figure out Brick at a glance.</div>
                        </li>
                        <li class=" mb-6">
                            <a href="https://docs.google.com/presentation/d/1wgT5S8fgo13cqDPx7DbygWuqAhIp4uxAenP4oDsMaVI/edit?usp=sharing">Tutorial
                                Slides</a>
                            <div class="text-lg text-gray-600">You can add comments to ask questions or discuss
                                anything.
                            </div>
                        </li>
                        <li class=" mb-6">
                            <a href="https://github.com/BuildSysUniformMetadata/brick-tutorial-buildsys2017">Jupyter
                                Notebooks</a>
                            <div class="text-lg text-gray-600">For those who are more hands-on.</div>
                        </li>

                    </ul>
                </div>

                <div class="container-inner mx-auto text-xl border-gray-500 border-b py-16 relative">
                    <h2 class="text-3xl font-bold mb-16">Community</h2>

                    <div class="absolute right-0" style="top: 50px; transform: translate(100%) rotate(180deg)">
                        <svg width="170px" height="170px">
                            <use xlink:href="#dots-triangle"/>
                        </svg>
                    </div>

                    <ul class="text-lg sm:text-xl">
                        <li class=" mb-6">
                            <a href="https://groups.google.com/d/forum/brickschema">Developer Forum</a>
                            <div class="text-lg text-gray-600">We will actively respond to any concerns or questions.
                            </div>
                        </li>
                        <li class=" mb-6">
                            <a href="https://github.com/BuildSysUniformMetadata/GroundTruth/issues">GitHub Issues</a>
                            <div class="text-lg text-gray-600">Any technical features can be discussed. We welcome any
                                proposals including new Tagsets and feature.
                            </div>
                        </li>
                    </ul>
                </div>

            </div>
        </div>

    </Layout>
</template>

<script>
    export default {
        metaInfo: {
            title: 'Get Started'
        }
    }
</script>

