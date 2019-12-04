<template>
  <div class="home">
    <div class="container">
      <div v-if="subjects">
        <div v-for="subject in subjects" :key="subject.pk">
          <!--
                  <p class="mb-0">
                      Posted by:
                         <span class="subject-author">{{ subject.author }}</span>
                  </p>
                   -->
          <router-link
            class="subject-link"
            :to="{ name: 'subject', params: { slug: subject.slug } }"
          >
            {{ subject.title }}
          </router-link>

          <p>{{ subject.description }}</p>
          <hr />
        </div>
        <div class="my-4">
          <p v-show="loadingSubjects">...loading...</p>
          <button
            v-show="next"
            @click="getsubjects"
            class="btn btn-sm btn-outline-success"
          >
            Load More
          </button>
        </div>
      </div>
      <div v-else>
        <p>Empty</p>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "home",
  data() {
    return {
      subjects: [],
      next: null,
      loadingSubjects: false
    };
  },
  methods: {
    getsubjects() {
      let endpoint = "api/subjects/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingSubjects = true;
      apiService(endpoint).then(data => {
        this.subjects.push(...data.results);
        this.loadingSubjects = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    }
  },
  created() {
    this.getsubjects();
    document.title = "MyKnowledgeBase";

    console.log(this.subjects);
    //Console.log("Hello world!");
  }
};
</script>

<style scoped>
.subject-author {
  font-weight: bold;
  color: rgb(206, 193, 194);
}
.subject-link {
  font-weight: bold;
  color: black;
}
.subject-link:hover {
  color: #343a40;
  text-decoration: none;
}
</style>
