<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Comment</h1>
    <form @submit.prevent="onSubmit">
      <input v-model="title" class="form-control" />
      <br />
      <textarea v-model="description" class="form-control" rows="3"></textarea>
      <br />
      <button type="submit" class="btn btn-success">
        Publish your Comment
      </button>
    </form>
    <p v-if="error" class="muted mt-2 error">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "CommentEditor",
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      title: null,
      subjectsSlug: null,
      description: null,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (this.title && this.description) {
        //const num = parseInt(this.id, 10);

        let endpoint = `/api/subjects/comment/${this.id}/`;
        apiService(endpoint, "PUT", {
          comment_description: this.description,
          comment_title: this.title
        }).then(() => {
          this.$router.push({
            name: "subject",
            params: { slug: this.subjectsSlug }
          });
        });
      } else {
        this.error = "You can't submit an empty Comment!";
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    //alert(" --" + to.params.id);
    // get the answer's data from the REST API and set two data properties for the component
    let endpoint = `/api/subjects/comment/${to.params.id}/`;
    let data = await apiService(endpoint);
    // to.params.previousCommentTitle = data.title;
    // to.params.previousCommentDescription = data.description;
    // to.params.subjectSlug = data.subject_Slug;
    //return next();
    return next(
      vm => (
        (vm.title = data.comment_title),
        (vm.description = data.comment_description),
        (vm.subjectsSlug = data.subject_slug)
      )
    );
  }
};
</script>

<style scoped>
.error {
  font-weight: bold;
  color: red;
}
</style>
