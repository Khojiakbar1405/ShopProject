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
    # product
    path('dashboard/product/create/', views.product_create, name='product_create'),
    path('dashboard/product/list/', views.product, name='product'),
    path('dashboard/product/update/<int:id>/', views.product_update, name='product_update'),
    path('dashboard/product/delete/<int:id>/', views.product_delete, name='product_delete'),
    path('dashboard/product_detail/list/<int:id>/', views.product_detail, name='product_detail'),
    # enter
    # path('dashboard/enter/create/', views.create_enter, name='enter_product'),
    # path('dashboard/enter/list/', views.list_enter, name='enter'),
    # path('dashboard/enter/update/<int:id>/', views.update_enter, name='enter_update'),
    # path('dashboard/enter/delete/<int:id>/', views.delete_enter, name='enter_delete'),
    # enters
    path('enter-list/', views.list_enter, name='list_enter'),
    path('enter-create/', views.create_enter, name='create_enter'),
    path('enter-update/<int:id>/', views.update_enter, name='update_enter'),
    path('enter-delete/<int:id>/', views.delete_enter, name='delete_enter'),
    # print to excel
    path('print_to_excel/', views.print_to_excel, name='print_to_excel'),
    path('print_to_excel_project/', views.print_to_excel_project, name='print_to_excel_project'),
    path('upload_and_display/', views.upload_and_display, name='upload_and_display'),
]