from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework import serializers
from main import models 


#  Product uchun
class ListProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'name']
        # exclude = ['id',]


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['name', 'description', 'price', 'quantity', 'currency', 'discount_price', 'baner_image', 'category']


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ['image', ]


class DetailProductSerilaizer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    images = ImagesSerializer(many=True, read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = models.Product
        depth = 1
        fields = ['name', 'description', 'price',
                   'quantity', 'currency', 'discount_price',
                    'baner_image', 'category', 'review',
                    'is_discount', 'is_active', 'images']





class ListProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'


# Category uchun
class ListCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'




class ListWishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'


class CreateWishListView(CreateAPIView):
    serializer_class = ListWishListSerializer


class DeleteWishListView(DestroyAPIView):
    queryset = models.WishList.objects.all()
    serializer_class = ListWishListSerializer


class ListProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductReview
        fields = '__all__'


class CreateReviewView(CreateAPIView):
    serializer_class = ListProductReviewSerializer


class DeleteReviewView(DestroyAPIView):
    queryset = models.ProductReview.objects.all()
    serializer_class = ListProductReviewSerializer


class ListCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'


class ListCartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'


class ListEnterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EnterProduct
        fields = '__all__'