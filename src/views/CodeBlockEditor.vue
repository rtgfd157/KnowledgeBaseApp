<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Code</h1>
    <form @submit.prevent="onSubmit">
      <input v-model="title" class="form-control" />
      <br />
      <textarea v-model="description" class="form-control" rows="3"></textarea>
      <br />
      <textarea v-model="code" class="form-control" rows="8"></textarea>
      <br />
      <button type="submit" class="btn btn-success">
        Publish your Code
      </button>
    </form>
    <p v-if="error" class="muted mt-2 error">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "CodeBlockEditor",
  props: {
    id: {
      type: Number,
      required: true
    },
    prevCode: {
      type: String,
      required: true
    },
    prevtitle: {
      type: String,
      required: true
    },
    prevDescription: {
      type: String,
      required: true
    },
    subject_slug: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      title: this.prevtitle,
      subjectsSlug: this.subject_slug,
      description: this.prevDescription,
      code: this.prevCode,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (this.title && this.description && this.code) {
        let endpoint = `/api/subjects/codeblock/${this.id}/`;
        apiService(endpoint, "PUT", {
          description: this.description,
          title: this.title,
          code: this.code
        }).then(() => {
          this.$router.push({
            name: "subject",
            params: { slug: this.subjectsSlug }
          });
        });
      } else {
        this.error = "You can't submit an empty URL!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    //alert(typeof to.params.id);

    const s = parseInt(to.params.id, 10);
    //alert(typeof s);
    to.params.id = s;
    //this.id = to.params.id;
    //alert("to.params.id " + to.params.id);
    //alert("this.id " + this.id);

    //alert(to.params.id);
    // get the answer's data from the REST API and set two data properties for the component
    let endpoint = `/api/subjects/codeblock/${to.params.id}/`;
    let data = await apiService(endpoint);
    to.params.prevtitle = data.title;
    to.params.prevDescription = data.description;
    //alert(data.subject_Slug);
    to.params.subject_slug = data.subject_slug;
    to.params.prevCode = data.code;

    return next();
  }
};
</script>
<style scoped>
.error {
  font-weight: bold;
  color: red;
}
</style>
