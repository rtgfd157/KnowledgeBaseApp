<template>
  <div class="single-subject mt-2">
    <div v-if="subject" class="container">
      <div class="container">
        <!-- --{{slug}}--
            ##1 {{ subject }} 1##
            -->
        <h1>{{ subject.title }}</h1>
        <SubjectActions :slug="subject.slug" />
        <!--<p class="mb-0">
        Updated at:
        <span>{{ subject.updated_at }}</span>
      </p> -->

        <p>{{ subject.description }}</p>

        <h4>
          Add:
          <span>
            <input type="radio" v-model="x" value="comment" /> Comment
            <input type="radio" v-model="x" value="urlink" /> Url Link
            <input type="radio" v-model="x" value="codeblock" /> Code Block
            <input type="radio" v-model="x" value="none" /> None
          </span>
        </h4>

        <div v-if="x === 'comment'">
          <form class="card" @submit.prevent="onSubmitComment">
            <div class="card-header px-3">
              Add Comment
            </div>
            <div class="card-block">
              <input
                v-model="title"
                class="form-control"
                placeholder="Comment Title"
              />
              <br />
              <textarea
                v-model="description"
                class="form-control"
                placeholder="Comment description"
                rows="5"
              ></textarea>
            </div>
            <div class="card-footer px-3">
              <button type="submit" class="btn btn-sm btn-success">
                Submit Your Comment
              </button>
            </div>
          </form>
          <p v-if="error" class="error mt-2">{{ error }}</p>
        </div>
        <div v-else-if="x === 'urlink'">
          <form class="card" @submit.prevent="onSubmitUrlink">
            <div class="card-header px-3">
              Add url Link
            </div>
            <div class="card-block">
              <input
                v-model="title"
                class="form-control"
                placeholder="Comment Title"
              />
              <br />
              <textarea
                v-model="description"
                class="form-control"
                placeholder="Comment description"
                rows="5"
              ></textarea>
              <br />
              <input
                v-model="url_link"
                class="form-control"
                placeholder="e.g https:// ..."
              />
            </div>
            <div class="card-footer px-3">
              <button type="submit" class="btn btn-sm btn-success">
                Submit Your URL link
              </button>
            </div>
          </form>
          <p v-if="error" class="error mt-2">{{ error }}</p>
        </div>
        <div v-else-if="x === 'codeblock'">
          <form class="card" @submit.prevent="onSubmitCodeBlock">
            <div class="card-header px-3">
              Add Code Block
            </div>
            <div class="card-block">
              <input
                v-model="title"
                class="form-control"
                placeholder="Code Block Title"
              />
              <br />
              <textarea
                v-model="description"
                class="form-control"
                placeholder="Code Block description"
                rows="5"
              ></textarea>
              <br />
              <textarea
                v-model="code"
                class="form-control"
                placeholder="Code Block description"
                rows="10"
              ></textarea>
            </div>
            <div class="card-footer px-3">
              <button type="submit" class="btn btn-sm btn-success">
                Submit Your Code Block
              </button>
            </div>
          </form>
          <p v-if="error" class="error mt-2">{{ error }}</p>
        </div>
        <div v-else></div>
      </div>
      <hr />
      <div class="container">
        <KnowledgeBlockComponent
          v-bind:knowledgeblock="knowledgeblock"
          @delete-comment="delcomment"
          @delete-urlink="delurlink"
          @delete-codeblock="delcodeblock"
        />
      </div>
    </div>

    <div v-if="!subject" class="container">
      <h1 class="error text-center">404 - Question Not Found</h1>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import KnowledgeBlockComponent from "@/components/KnowledgeBlock.vue";
import SubjectActions from "@/components/SubjectActions.vue";

export default {
  name: "Subject",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    KnowledgeBlockComponent,
    SubjectActions
  },
  data() {
    return {
      subject: {},
      knowledgeblock: {},
      title: null,
      description: null,
      url_link: null,
      code: null,
      error: null,
      x: null
    };
  },
  methods: {
    setPageTitle(title) {
      // set a given title string as the webpage title
      document.title = title;
    },
    getSubjectData() {
      let endpoint = `/api/subjects/${this.slug}/`;
      //   apiService(endpoint).then(data => {
      //     this.subject = data;
      //     this.setPageTitle(data.title);
      //   });
      apiService(endpoint).then(data => {
        if (data) {
          //alert("sssssssss");
          this.subject = data;
          this.setPageTitle(data.title);
        } else {
          //alert("eeee");
          this.subject = null;
          this.setPageTitle("404 - Page Not Found");
        }
      });
    },
    getKnowledgeBlock() {
      let endpoint = `/api/subjects/${this.slug}/textapi/`;
      apiService(endpoint).then(data => {
        //this.knowledgeblock.push(...data.results);
        this.knowledgeblock = data.results;
        //alert(this.knowledgeblock);
        console.log(this.knowledgeblock);
        // alert(" data.results : " + data.results);
      });
    },
    onSubmitComment() {
      // Tell the REST API to create a new comment for this question based on the user input, then update some data properties
      if (this.title && this.description) {
        let endpoint = `/api/subjects/${this.slug}/comments/`;
        apiService(endpoint, "POST", {
          comment_title: this.title,
          comment_description: this.description
        }).then(
          // this.knowledgeblock.unshift(data);
          this.getKnowledgeBlock()
        );
        this.title = null;
        this.description = null;
        this.x = null;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty comment!";
      }
    },
    onSubmitUrlink() {
      // Tell the REST API to create a new url link for this question based on the user input, then update some data properties
      if (this.title && this.description && this.url_link) {
        let endpoint = `/api/subjects/${this.slug}/urlink/`;
        apiService(endpoint, "POST", {
          title: this.title,
          description: this.description,
          url_link: this.url_link
        }).then(
          // this.knowledgeblock.unshift(data); will be good on array
          this.getKnowledgeBlock()
        );
        this.title = null;
        this.description = null;
        this.url_link = null;
        this.x = null;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty URL Link !";
      }
    },
    onSubmitCodeBlock() {
      // Tell the REST API to create a new Code Block for this question based on the user input, then update some data properties
      if (this.title && this.description && this.code) {
        let endpoint = `/api/subjects/${this.slug}/codeblock/`;
        apiService(endpoint, "POST", {
          title: this.title,
          description: this.description,
          code: this.code
        }).then(this.getKnowledgeBlock());
        this.title = null;
        this.description = null;
        this.code = null;
        this.x = null;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "You can't send an empty Code Block!";
      }
    },
    async delcomment(val) {
      // delete a given answer from the answers array and make a delete request to the REST API
      let endpoint = `/api/subjects/comment/${val}/`;
      // path("subjects/comment/<int:pk>/",

      try {
        await apiService(endpoint, "DELETE");
        this.getKnowledgeBlock();
        //this.$delete(this.answers, this.answers.indexOf(answer)) remove from array
      } catch (err) {
        console.log(err);
      }
    },
    async delurlink(val) {
      // delete a given urlink from the answers array and make a delete request to the REST API
      let endpoint = `/api/subjects/urlink/${val}/`;

      try {
        await apiService(endpoint, "DELETE");
        this.getKnowledgeBlock();
      } catch (err) {
        console.log(err);
      }
    },
    async delcodeblock(val) {
      // delete a given urlink from the answers array and make a delete request to the REST API
      let endpoint = `/api/subjects/codeblock/${val}/`;
      //alert(val);
      try {
        await apiService(endpoint, "DELETE");
        this.getKnowledgeBlock();
      } catch (err) {
        console.log(err);
      }
    }
  },
  created() {
    this.getSubjectData();
    this.getKnowledgeBlock();
  }
};
</script>

<style scoped>
.error {
  font-weight: bold;
  color: red;
}
</style>
