<template>
  <div class="row">
    <div class="col-lg-8 col-md-6 col-sm-12">
      <figure class="figure mb-4">
        <img v-bind:src="product.get_image" class="img-fluid product_image" />
      </figure>

      <h1>{{ product.name }}</h1>
      <p>{{ product.description }}</p>
    </div>
    <div class="col-lg-4 col-md-6 col-sm-12">
      <h2>Information</h2>
      <p><strong>Price: </strong> Rs.{{ product.price }}</p>
      <div class="d-flex mt-5">
        <div class="form-group">
          <input
            type="number"
            class="form-control"
            min="1"
            v-model="quantity"
          />
        </div>
        <div class="form-group">
          <a class="btn btn-dark"
            ><i class="fas fa-cart-shopping me-2"></i> Add to Cart
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProductView",
  data() {
    return {
      quantity: 1,
      product: {},
    };
  },
  mounted() {
    this.getProductDetail();
  },
  methods: {
    getProductDetail() {
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;
      axios
        .get(`/product/${category_slug}/${product_slug}`)
        .then((response) => {
          this.product = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.product_image {
  height: 500px;
  width: auto;
}
</style>