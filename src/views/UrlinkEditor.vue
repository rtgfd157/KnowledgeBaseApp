<template>
  <div class="container mt-2">
    <h1 class="mb-3">Edit Your Url Link</h1>
    <form @submit.prevent="onSubmit">
      <input v-model="title" class="form-control" />
      <br />
      <textarea v-model="description" class="form-control" rows="3"></textarea>
      <br />
      <input v-model="urlink" class="form-control" />
      <br />
      <button type="submit" class="btn btn-success">
        Publish your URL
      </button>
    </form>
    <p v-if="error" class="muted mt-2 error">{{ error }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "UrlinkEditor",
  props: {
    id: {
      type: Number,
      required: true
    },
    prevUrlink: {
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
      urlink: this.prevUrlink,
      error: null
    };
  },
  methods: {
    onSubmit() {
      if (this.title && this.description && this.urlink) {
        let endpoint = `/api/subjects/urlink/${this.id}/`;
        apiService(endpoint, "PUT", {
          description: this.description,
          title: this.title,
          url_link: this.urlink
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
    let endpoint = `/api/subjects/urlink/${to.params.id}/`;
    let data = await apiService(endpoint);
    to.params.prevtitle = data.title;
    to.params.prevDescription = data.description;
    //alert(data.subject_Slug);
    to.params.subject_slug = data.subject_slug;
    to.params.prevUrlink = data.url_link;

    return next();
    // alert(data.comment_title);
    // return next(
    //   vm => (
    //     (vm.title = data.comment_title),
    //     (vm.description = data.comment_description),
    //     (vm.subjectsSlug = data.subject_slug)
    //   )
    // );
  }
};
</script>

<style scoped>
.error {
  font-weight: bold;
  color: red;
}
</style>
