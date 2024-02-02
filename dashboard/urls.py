from . import views
from django.urls import path

app_name = 'dashboard'

urlpatterns = [
    # dashboard
    path('', views.dashboard, name='dashboard'),
    # categorys
    path('dashboard/category/create/', views.create_category, name='create_category'),
    path('dashboard/category/list/', views.category_list, name='category'),
    path('dashboard/category/update/<int:id>/', views.category_update, name='category_update'),
    path('dashboard/category/delete/<int:id>/', views.category_delete, name='category_delete'),
    # itms
    path('dashboard/product/create/', views.product_create, name='product_create'),
    path('dashboard/product/list/', views.product, name='product'),
    path('dashboard/product/update/<int:id>/', views.product_update, name='product_update'),
    path('dashboard/product/delete/<int:id>/', views.product_delete, name='product_delete'),
]