from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerializer


class LatestProductList(APIView):
    def get(self, request):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetails(APIView):

    def get(self, request, category_slug, product_slug):
        product = self.get_object(category_slug=category_slug, product_slug=product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            return Http404
