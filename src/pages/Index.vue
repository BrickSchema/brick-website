<template>
  <Layout>
    <div class="hero container-inner mx-auto flex flex-col sm:flex-row justify-between py-16">
      <div class="text-4xl font-bold w-full sm:w-3/5 text-center sm:text-left">
        <div class="leading-tight">Brick</div>
        <div class="text-primary-700 leading-tight">A uniform metadata schema for buildings</div>
      </div>
      <div class="w-1/2 mt-8 sm:mt-0">
        <g-image src="../../static/mind_map.svg" alt="hero" class="mx-auto sm:mx-0"/>
      </div>
    </div> <!-- end hero -->


    <div class="container-inner mx-auto">
      <p class="text-lg sm:text.-xl">Commercial buildings have long since been a primary target for applications
        from a number of areas: from cyber-physical systems to building energy use to improved human
        interactions in built environments. While technological advances have been made in these areas, such
        solutions rarely experience widespread adoption due to the lack of a common descriptive schema reducing
        the now-prohibitive cost of porting these applications and systems to different buildings</p>

      <div class="flex justify-between items-center py-6">
        <div class="w-1/2 sm:w-1/2 px-8 py-8 sm:py-0">
          <g-image src="../../static/developer.svg" alt="browser"/>
        </div>
        <div class="w-1/2 px-8 hidden sm:flex justify-end">
          <g-image src="../../static/building_blocks.svg" alt="mobile"/>
        </div>
      </div>
    </div>

    <div class="overflow-x-hidden">
      <div class="projects container-inner mx-auto text-xl border-t border-gray-500 border-b py-16 mb-16 relative">
        <h2 class="font-bold mb-6" id="features">Features:</h2>

        <div class="absolute right-0" style="top: 50px; transform: translate(100%) rotate(180deg)">
          <svg width="170px" height="170px"><use xlink:href="#dots-triangle" /></svg>
        </div>

        <ul class="text-lg sm:text-xl">
          <li class="checkmark mb-6">
            <div>Usability</div>
            <div class="text-lg text-secondary-600">All the standard tools for ontologies, such as RDF and SPARQL
              technologies, can beleveraged to support storage, querying, composition and visualization of
              Brick models.
            </div>
          </li>
          <li class="checkmark mb-6">
            <div>High Coverage</div>
            <div class="text-lg text-secondary-600">The schema was validated with 6 buildings across different
              parts of the world showing 98%coverage of the entities and all the relationships required by
              numerous applications in the literature.
            </div>
          </li>
          <li class="checkmark mb-6">
            <div>Flexible</div>
            <div class="text-lg text-secondary-600">Because classes are hierarchically defined, applications
              developers and building managerscan express their data requirements and model their building
              components at different levels ofabstraction, ensuring proper functionality.
            </div>
          </li>
          <li class="checkmark mb-6">
            <div>Expressive</div>
            <div class="text-lg text-secondary-600">Canonical relationships allow Brick to express those required
              by various applicationcategories such as fault diagnostics and occupancy-based controls.
            </div>
          </li>
          <li class="checkmark mb-6">
            <div>Consistent</div>
            <div class="text-lg text-secondary-600">Brick classes guarantee maximum interoperability by
              preventing inconsistent usages,such as different groupings of tags expressing the same
              concept.
            </div>
          </li>
          <li class="checkmark mb-6">
            <div>Extensible</div>
            <div class="text-lg text-secondary-600">Semantic reasoning of new classes is possible.</div>
          </li>

        </ul>
      </div> <!-- end projects -->
    </div>


    <div class="overflow-x-hidden">
      <div class="contact-me bg-background-secondary pt-16">
        <div class="container-inner mx-auto text-xl pb-4 relative">
          <h2 class="font-bold mb-6" id="contact">Contact Us:</h2>

          <div class="absolute right-0 top-0" style="transform: translate(100%) rotate(180deg)">
            <svg width="170px" height="170px"><use xlink:href="#dots-triangle" /></svg>
          </div>

          <!--          <p class="mb-12">Static sites cannot submit forms on their own. However, services like <a href="https://www.netlify.com/docs/form-handling">Netlify Forms</a> or <a href="https://formspree.io">FormSpree</a> can help you do this without a backend.</p>-->

          <div class="text-lg sm:text-lg mb-16">
            <form action="mailto:snagare@andrew.cmu.edu?subject=Brick" class="mb-12">
              <div class="flex flex-wrap mb-6 -mx-4">
                <div class="w-full md:w-1/2 mb-6 md:mb-0 px-4">
                  <label class="block mb-2 text-copy-primary" for="name">
                    Name
                  </label>

                  <input type="text" name="name" id="name" placeholder="Jon Snow"
                         class="block w-full bg-background-form border border-border-color-primary shadow rounded outline-none focus:border-primary-700 mb-2 p-4"
                         required>
                </div>

                <div class="w-full px-4 md:w-1/2">
                  <label class="block text-copy-primary mb-2" for="email">
                    Email Address
                  </label>

                  <input type="email" name="email" id="email" placeholder="email@example.com"
                         class="block w-full bg-background-form border border-border-color-primary shadow rounded outline-none focus:border-primary-700 mb-2 p-4"
                         required>
                </div>
              </div>

              <div class="w-full mb-12">
                <label class="block text-copy-primary mb-2" for="message">
                  Message
                </label>

                <textarea id="message" rows="5" name="message"
                          class="block w-full bg-background-form border border-border-color-primary shadow rounded outline-none appearance-none focus:border-primary-700 mb-2 px-4 py-4"
                          placeholder="Enter your message here." required></textarea>
              </div>

              <div class="flex justify-end w-full">
                <input type="submit" value="Submit"
                       class="block bg-primary-700 hover:bg-primary-800 text-white text-sm font-semibold tracking-wide uppercase shadow rounded cursor-pointer px-6 py-3">
              </div>
            </form>
          </div>
        </div>
      </div> <!-- end contact-me -->
    </div>

  </Layout>
</template>

<script>
  export default {
    metaInfo: {
      title: 'Home'
    }
  }
</script>

