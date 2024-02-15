from django.urls import path
from . import views


urlpatterns = [
   path('product-list/', views.list_products),
   path('category-list/', views.list_category),
   path('product-image-list/', views.list_product_image),
   path('wish-list/', views.list_wish_list),
   path('product-review-list/', views.list_product_review),
   path('cart-list/', views.list_cart),
   path('cart-product-list/', views.list_cart_product),
   path('enter-product-list/', views.list_enter_product),
]