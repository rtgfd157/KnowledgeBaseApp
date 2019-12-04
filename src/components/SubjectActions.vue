<template>
  <div class="subject-actions">
    <router-link
      :to="{ name: 'subject-editor', params: { slug: slug } }"
      class="btn btn-sm btn-outline-secondary mr-1"
      >Edit
    </router-link>
    <button class="btn btn-sm btn-outline-danger" @click="deleteSubject">
      Delete
    </button>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "SubjectActions",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  methods: {
    async deleteSubject() {
      let endpoint = `/api/subjects/${this.slug}/`;
      try {
        await apiService(endpoint, "DELETE");
        this.$router.push("/");
      } catch (err) {
        console.log(err);
      }
    }
  }
};
</script>
