from rest_framework.serializers import ModelSerializer
from main import models 

class ListProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
        # fields = ['id', 'name']
        # exclude = ['id',]


class ListCategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class ListProductImageSerializer(ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'


class ListWishListSerializer(ModelSerializer):
    class Meta:
        model = models.WishList
        fields = '__all__'


class ListProductReviewSerializer(ModelSerializer):
    class Meta:
        model = models.ProductReview
        fields = '__all__'


class ListCartSerializer(ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'


class ListCartProductSerializer(ModelSerializer):
    class Meta:
        model = models.CartProduct
        fields = '__all__'


class ListEnterProductSerializer(ModelSerializer):
    class Meta:
        model = models.EnterProduct
        fields = '__all__'