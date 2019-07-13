<template>
  <div>
    <div class="m-8 font-thin text-gray-700">Select a persona that will help up show you more relevant information.</div>
    <ul>
      <li v-for="thisPersona in this.$static.personas.edges" @click.prevent="updatePersona(thisPersona.node.id)" :class="thisPersona.node.id === persona ? 'bg-gray-200' : 'bg-white'">
        <div class="mx-8 my-4 p-2 hover:text-primary-700">
            <div class="text-l">{{ thisPersona.node.label }}</div>
            <div class="text-sm text-gray-600">{{ thisPersona.node.description }}</div>
        </div>
      </li>
    </ul>

  </div>
</template>

<static-query>
  query {

    personas: allPersona(order: ASC){
    edges{
    node{
    id
    label
    description
    thumbnail
    }
    }
    }

  }
</static-query>

<script>



export default {
  props: {
    persona: {
      type: String,
      required: true,
    }
  },
  methods: {
    updatePersona(newPersona) {
      localStorage.setItem('persona', newPersona)
      this.$emit('personaUpdated', newPersona)
    }
  }
}
</script>