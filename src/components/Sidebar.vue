<template>
  <div id="wrapper">
    <div class="overlay">
      <!-- Sidebar -->
      <nav
        class="navbar navbar-inverse fixed-top"
        id="sidebar-wrapper"
        role="navigation"
      >
        <ul class="nav sidebar-nav">
          <div class="sidebar-header">
            <div class="sidebar-brand">
              <a href="#">Dashboard </a>
            </div>
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#event">Event</a></li>
            <li class="dropdown">
              <a href="#works" class="dropdown-toggle" data-toggle="dropdown"
                >Carriers <span class="caret"></span
              ></a>
              <ul class="dropdown-menu animated dadeInLeft" role="menu">
                <div class="dropdown-header">Dropdown Heading</div>
                <li><a href="#pictures">Pictures</a></li>
                <li><a href="#videos">Videos</a></li>
              </ul>
            </li>
            <li><a href="#services">Services</a></li>
          </div>
        </ul>
      </nav>
      <!-- Sidebar Wrapper -->
    </div>
  </div>
</template>

<script>
export default {
  name: "SidebarComponent"
};
</script>

<style scoped>
.sidebar {
  background-color: #fee;
  height: 100%;
  width: 150px;
  max-width: 1024px;
  opacity: 0.8;
  position: fixed;
  z-index: 1;
  top: 100px;
  left: 0;
  overflow-x: hidden;
  box-sizing: border-box;
}

h1 {
  display: inline;
  height: 29px;
  width: 156px;
}

ul,
#sublist {
  list-style: none;
  margin: 0;
  padding: 0;
}

a {
  height: 20px;
  width: 200px;
  text-decoration: none;
  display: block;
}

.container-grid {
  background-color: #eef;
  margin-left: 180px;
}
</style>
