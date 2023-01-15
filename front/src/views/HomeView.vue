<template>
  <div class="home">
    <div class="p-5 text-center bg-light">
      <h1 class="mb-3">Welcome to Ecommerce</h1>
      <h4 class="mb-3">The best jacket store online</h4>
    </div>

    <div class="row mt-5">
      <div class="col-12">
        <h2 class="fs-4 text-center mb-5">Latest Products</h2>
      </div>
      <div
        class="col-lg-3 col-md-4 col-sm-12 me-2"
        v-for="product in latestProducts"
        v-bind:key="product.id"
      >
        <div class="card" style="width: 18rem">
          <img :src="product.get_thumbnail" class="card-img-top" />
          <div class="card-body">
            <h5 class="card-title">{{ product.name }}</h5>
            <p class="card-text">Rs.{{ product.price }}</p>
            <router-link
              v-bind:to="product.get_absolute_url"
              class="btn btn-dark"
            >
              View details
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    getLatestProducts() {
      axios
        .get("/latest-products/")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
</style>
