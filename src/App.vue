<template>
  <div id="app">
    <NavbarComponent />
    <!--  <SidebarComponent/> -->
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "@/components/Navbar.vue";
// import SidebarComponent from "@/components/Sidebar.vue";

export default {
  name: "App",
  components: {
    NavbarComponent
    /*SidebarComponent  */
  }
};
</script>

<style>
html,
body {
  height: 100%;
  font-family: "Playfair Display", serif;
}
.btn:focus {
  box-shadow: none !important;
}
</style>
