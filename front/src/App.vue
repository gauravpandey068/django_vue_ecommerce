<template>
  <div id="wrapper" class="container">
    <!-- Navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <!-- Container wrapper -->
      <div class="container">
        <!-- Navbar brand -->
        <router-link to="/" class="navbar-item"
          ><strong>Ecommerce</strong></router-link
        >

        <!-- Toggle button -->
        <button
          class="navbar-toggler"
          type="button"
          data-mdb-toggle="collapse"
          data-mdb-target="#navbarButtonsExample"
          aria-controls="navbarButtonsExample"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <i class="fas fa-bars"></i>
        </button>

        <!-- Collapsible wrapper -->
        <div class="collapse navbar-collapse" id="navbarButtonsExample">
          <!-- Left links -->
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="#">Dashboard</a>
            </li>
          </ul>
          <!-- Left links -->

          <div class="d-flex align-items-center">
            <router-link to="/summer" class="navbar-link me-2"
              >Summer</router-link
            >
            <router-link to="/winter" class="navbar-link me-2"
              >Winter</router-link
            >
            <router-link to="/log-in" class="btn btn-primary px-3 me-2"
              >Log in</router-link
            >
            <router-link to="/cart" class="btn btn-success me-3">
              <span class="icon">
                <i class="fas fa-shopping-cart me-2"></i>
              </span>
              <span>Cart</span>
            </router-link>
          </div>
        </div>
        <!-- Collapsible wrapper -->
      </div>
      <!-- Container wrapper -->
    </nav>
    <!-- Navbar -->

    <section class="section">
      <router-view />
    </section>
  </div>
  <footer class="bg-light text-center text-lg-start">
    <!-- Copyright -->
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
      © 2020 Copyright:
      <span class="text-dark">Ecommerce</span>
    </div>
    <!-- Copyright -->
  </footer>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    };
  },
};
</script>

<style lang="scss">
</style>
