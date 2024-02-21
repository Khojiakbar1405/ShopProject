from django.urls import path
from . import views


urlpatterns = [
   path('product-list/', views.list_products),
   path('product-detail/<str:slug>/', views.product_detail),
   path('product-list-create/', views.list_create_products),

   path('category-list/', views.list_category),
   path('category-detail/<str:slug>/', views.category_detail),

   path('product-image-list/', views.list_product_image),
  
   path('wish-list/', views.list_wish_list),
   path('wish-list-create/', views.create_wish_list),
   path('wishl-list-delete/<int:id>/', views.delete_wish_list),
  
   path('product-review-list/', views.list_product_review),
   path('review-create/', views.create_review),
   path('review-update/<int:id>/', views.update_review),
   path('review-delete/<int:id>/', views.delete_review),

   path('cart-list/', views.list_cart),
   path('cart-in-active/', views.cart_in_active),
   path('cart-active/', views.cart_active),
   path('cart-delete/<int:id>/', views.delete_cart),
   path('cart-update/<int:id>/', views.update_cart),

   path('cart-product-list/', views.list_cart_product),
   path('cart-product-create/', views.create_cart_product),
   path('cart-product-update/<int:id>/', views.update_cart_product),
   path('cart-product-delete/<int:id>/', views.delete_cart_product),

   path('enter-product-list/', views.list_enter_product),

   path('login/', views.log_in),
   path('register/', views.register),
]