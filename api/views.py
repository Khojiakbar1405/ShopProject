from . import serializers
from main import models

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def list_products(request):
    products = models.Product.objects.all()
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_category(request):
    categorys = models.Category.objects.all()
    serializer = serializers.ListCategorySerializer(categorys, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_product_image(request):
    product_images = models.ProductImage.objects.all()
    serializer = serializers.ListProductImageSerializer(product_images, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_wish_list(request):
    wish_lists = models.WishList.objects.all()
    serializer = serializers.ListWishListSerializer(wish_lists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_product_review(request):
    product_reviews = models.ProductReview.objects.all()
    serializer = serializers.ListProductReviewSerializer(product_reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_cart(request):
    carts = models.Cart.objects.all()
    serializer = serializers.ListCartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_cart_product(request):
    cart_products = models.CartProduct.objects.all()
    serializer = serializers.ListCartProductSerializer(cart_products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def list_enter_product(request):
    enter_products = models.EnterProduct.objects.all()
    serializer = serializers.ListEnterProductSerializer(enter_products, many=True)
    return Response(serializer.data)