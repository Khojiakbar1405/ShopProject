from django.contrib.auth import login, authenticate
from django.contrib .auth.models import User
from . import serializers
from main import models

from rest_framework.permissions import IsAuthenticated
from rest_framework import authentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token

# product list, detail va create +
@api_view(['GET'])
def list_products(request):
    products = models.Product.objects.all()
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def product_detail(request,slug):
    product = models.Product.objects.get(slug=slug)
    product_ser = serializers.DetailProductSerilaizer(product)
    return Response(product_ser.data)

@api_view(['GET', 'POST'])
def list_create_products(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        serializer = serializers.ListProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# category list va detail +
@api_view(['GET'])
def list_category(request):
    categorys = models.Category.objects.all()
    serializer = serializers.ListCategorySerializer(categorys, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
def category_detail(request, slug):
    products = models.Product.objects.filter(category__slug=slug)
    serializer = serializers.ListProductSerializer(products, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def list_product_image(request):
    product_images = models.ProductImage.objects.all()
    serializer = serializers.ListProductImageSerializer(product_images, many=True)
    return Response(serializer.data)


# WishList list, create va delete +++
@api_view(['GET'])
def list_wish_list(request):
    wish_lists = models.WishList.objects.all()
    serializer = serializers.ListWishListSerializer(wish_lists, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_wish_list(request):
    serializer = serializers.ListWishListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_wish_list(request, id):
    try:
        wish_list = models.WishList.objects.get(id=id)
    except models.WishList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    wish_list.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# Product Review list, create, updete, delete +++
@api_view(['GET'])
def list_product_review(request):
    product_reviews = models.ProductReview.objects.all()
    serializer = serializers.ListProductReviewSerializer(product_reviews, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_review(request):
    serializer = serializers.ListProductReviewSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_review(request, id):
    try:
        review = models.ProductReview.objects.get(id=id)
    except models.ProductReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = serializers.ListProductReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_review(request, id):
    try:
        review = models.ProductReview.objects.get(id=id)
    except models.ProductReview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# Cart get/in_active, get/active, delete, detail ---  
@api_view(['GET'])
def list_cart(request):
    carts = models.Cart.objects.all()
    serializer = serializers.ListCartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cart_in_active(request):
    carts = models.Cart.objects.filter(is_active=False)
    serializer = serializers.ListCartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cart_active(request):
    carts = models.Cart.objects.filter(is_active=True)
    serializer = serializers.ListCartSerializer(carts, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_cart(request, id):
    try:
        review = models.Cart.objects.get(id=id)
    except models.Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_cart(request, id):
    try:
        cart = models.Cart.objects.get(id=id)
    except models.Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = serializers.ListCartSerializer(cart, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# CartProduct 
@api_view(['GET'])
def list_cart_product(request):
    cart_products = models.CartProduct.objects.all()
    serializer = serializers.ListCartProductSerializer(cart_products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_cart_product(request):
    serializer = serializers.ListCartProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_cart_product(request, id):
    try:
        review = models.CartProduct.objects.get(id=id)
    except models.CartProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    review.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_cart_product(request, id):
    try:
        cart = models.CartProduct.objects.get(id=id)
    except models.CartProduct.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = serializers.ListCartProductSerializer(cart, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# EnterProduct
@api_view(['GET'])
def list_enter_product(request):
    enter_products = models.EnterProduct.objects.all()
    serializer = serializers.ListEnterProductSerializer(enter_products, many=True)
    return Response(serializer.data)


# account
@api_view(['GET'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        data = {
            'token':token.key,
            'status':status.HTTP_200_OK
        }
    else:
        data = {'status':status.HTTP_404_NOT_FOUND}
    return Response(data)


@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.create_user(
        username=username,
        password=password
    )
    token = Token.objects.create(user=user)
    return Response({'username':user.username,
                     'token':token.key})