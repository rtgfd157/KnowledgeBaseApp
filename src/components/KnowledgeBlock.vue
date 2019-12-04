<template>
  <div>
    <!--
    <p>-{{ knowledgeblock }}-</p>

    
    <li v-for="(item, index) in knowledgeblock" v-bind:key="item">
      item = {{ item }} -------- index = {{ index }}
      <p v-for="(i, x) in item" v-bind:key="i">
        i= {{ i }} $$$$$$$$ x= {{ x }}
      </p>
    </li>
        -->
    <div
      class="container"
      v-for="(item, index) in knowledgeblock"
      v-bind:key="item.id"
    >
      <div v-for="i in item" v-bind:key="(pass_id = i.id)">
        <div v-if="index == 'Comment'">
          <h3 class="header-color">
            Comment: {{ i.comment_title }}

            <router-link
              :to="{ name: 'comment-editor', params: { id: i.id } }"
              class="btn btn-sm btn-outline-secondary mr-1"
            >
              Edit</router-link
            >
            <button
              class="btn btn-sm btn-outline-danger"
              @click="triggerDeleteComment(i.id)"
            >
              Delete
            </button>
          </h3>
          <p>{{ i.comment_description }}</p>
          <hr />
        </div>
        <div v-else-if="index == 'Url_Link'">
          <h3 class="header-color">
            Url Link: {{ i.title }}
            <router-link
              :to="{ name: 'urlink-editor', params: { id: i.id } }"
              class="btn btn-sm btn-outline-secondary mr-1"
            >
              Edit</router-link
            >
            <button
              class="btn btn-sm btn-outline-danger"
              @click="triggerDeleteUrlLink(i.id)"
            >
              Delete
            </button>
          </h3>
          <p>{{ i.description }}</p>
          <a :href="i.url_link">{{ i.url_link }}</a>
          <hr />
        </div>
        <div v-else-if="index == 'CodeBlock'">
          <h3 class="header-color">
            Code: {{ i.title }}

            <router-link
              :to="{ name: 'codeblock-editor', params: { id: i.id } }"
              class="btn btn-sm btn-outline-secondary mr-1"
            >
              Edit</router-link
            >
            <button
              class="btn btn-sm btn-outline-danger"
              @click="triggerDeleteCodeBlock(i.id)"
            >
              Delete
            </button>
          </h3>

          <p>{{ i.description }}</p>
          <pre><code  class="prettyprint">{{i.code}}</code> 
          </pre>
          <hr />
        </div>

        <div v-else>
          <h2>No match {{ index }}</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "KnowledgeBlockComponent",

  props: ["knowledgeblock"],
  //   prop: {
  //     knowledgeblock: {
  //       type: Object,
  //       required: true
  //     }
  //}
  //   data() {
  //     return {
  //       knowledgeblock: {}
  //     };
  //   }

  methods: {
    triggerDeleteComment(val) {
      // emit an event to delete an comment instance
      this.$emit("delete-comment", val);
    },
    triggerDeleteUrlLink(val) {
      this.$emit("delete-urlink", val);
    },
    triggerDeleteCodeBlock(val) {
      this.$emit("delete-codeblock", val);
    }
  }
};
</script>

<style scoped>
.header-color {
  color: #0080ff;
}
p {
  color: #ac7339;
}
.error {
  font-weight: bold;
  color: red;
}
</style>
