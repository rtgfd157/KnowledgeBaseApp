import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Subject from "./views/Subject.vue";
import SubjectEditor from "./views/SubjectEditor.vue";
import CommentEditor from "./views/CommentEditor.vue";
import UrlinkEditor from "./views/UrlinkEditor.vue";
import CodeBlockEditor from "./views/CodeBlockEditor.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/subject/:slug",
      name: "subject",
      component: Subject,
      props: true
    },
    {
      // optional slug field , for create or for updating
      path: "/add/:slug?",
      name: "subject-editor",
      component: SubjectEditor,
      props: true
    },
    {
      path: "/comment/:id",
      name: "comment-editor",
      component: CommentEditor,
      props: true
    },
    {
      path: "/urlink/:id",
      name: "urlink-editor",
      component: UrlinkEditor,
      props: true
    },
    {
      path: "/codeblock/:id",
      name: "codeblock-editor",
      component: CodeBlockEditor,
      props: true
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound
    }
  ]
});
