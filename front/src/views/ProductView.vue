<template>
  <div class="page-product">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6 ">
          <img v-bind:src="product.get_image" class="product_image">
        </figure>

        <h1 class="title">{{ product.name }}</h1>
        <p>{{ product.description}}</p>
      </div>
      <div class="column is-3">
        <h2 class="subtitle">Information</h2>
        <p><strong>Price: </strong>
          Rs.{{ product.price }}
        </p>
        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" class="input" min="1" v-model="quantity">
          </div>
          <div class="control">
            <a class="button is-dark">
              <i class="fa fa-cart"></i> Add to Cart
            </a>
          </div>
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
      product: {}
    }
  },
  mounted() {
    this.getProductDetail()
  },
  methods: {
    getProductDetail() {
      const category_slug = this.$route.params.category_slug
      const product_slug = this.$route.params.product_slug
      axios.get(`/product/${category_slug}/${product_slug}`).then(response => {
        this.product = response.data
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
.product_image{
  height: 500px;
  width: auto;
}

</style>