<template>
  <!--
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand"
        >KnowledgeBase
      </router-link>

      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link :to="{ name: 'home' }" class="btn btn-sm btn-success"
              >Home
            </router-link>
          </li>
          <li class="nav-item mx-1">
            <router-link
              :to="{ name: 'subject-editor' }"
              class="btn btn-sm btn-danger"
            >
              Add Knowledge
            </router-link>
          </li>
          <li class="nav-item">
            <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/"
              >Logout
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
-->

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand"
        >KnowledgeBase
      </router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active m-1">
            <router-link :to="{ name: 'home' }" class="btn btn-sm btn-success"
              >Home
            </router-link>
          </li>
          <li class="nav-item m-1">
            <router-link
              :to="{ name: 'subject-editor' }"
              class="btn btn-sm btn-danger"
            >
              Add Knowledge
            </router-link>
          </li>
          <li class="nav-item m-1">
            <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/"
              >Logout
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent"
};
</script>

<style>
.my-navbar {
  border-bottom: 1px solid #ddd;
}

.navbar-brand {
  font-weight: bold;
  font-size: 130%;
}

.navbar-brand:hover {
  color: #dc3545 !important;
}
</style>
