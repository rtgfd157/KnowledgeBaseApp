<template>
  <div class="container mt-2">
    <h1 class="mb-3">Add a Subject</h1>

    <form @submit.prevent="onSubmit">
      <h2>title:</h2>
      <input
        v-model="title"
        class="form-control"
        placeholder="Knowledge Title"
      />
      <br />
      <h2>description:</h2>
      <textarea
        v-model="description"
        class="form-control"
        placeholder="What description you want to add?"
        rows="4"
      ></textarea>
      <br />

      <button type="submit" class="btn btn-success">Publish</button>
    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "SubjectEditor",
  props: {
    slug: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      // subject_body: null,
      //subject: {},
      title: null,
      description: null,
      error: null
    };
  },
  methods: {
    onSubmit() {
      //alert(" 0 this.title " + this.title)
      // Tell the REST API to create or update a Question Instance
      if (!this.title || !this.description) {
        this.error = "You can't send an empty title or description!";
      } else if (this.title.length > 160) {
        this.error = "Ensure this field has no more than 160 characters!";
      } else {
        let endpoint = "/api/subjects/";
        let method = "POST";
        if (this.slug !== undefined) {
          endpoint += `${this.slug}/`;
          method = "PUT";
        }
        // alert(" this.title " + this.title)
        // alert(" this.description ", this.description)
        apiService(endpoint, method, {
          description: this.description,
          title: this.title
        }).then(subject => {
          this.$router.push({
            name: "subject",
            params: { slug: subject.slug }
          });
        });
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.slug !== undefined) {
      let endpoint = `/api/subjects/${to.params.slug}/`;
      let data = await apiService(endpoint);
      return next(
        vm => ((vm.description = data.description), (vm.title = data.title))
      );
    } else {
      return next();
    }
  },
  created() {
    document.title = "Editor - MyKnowledgeBase";
  }
};
</script>
