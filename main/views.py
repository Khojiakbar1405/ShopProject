from django.shortcuts import render, redirect
from . import models
from django.db.models import Q


def index(request):
    q = request.GET.get('q')
    if q:
        products = models.Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    else: 
        products = models.Product.objects.filter(quantity__gt=0)
    categorys = models.Category.objects.all()
    category_id = request.GET.get('category_id')
    if category_id:
        products.filter(category_id=category_id)
    context = {
        'products':products,
        'categorys':categorys
    }
    return render(request, 'index.html', context)




def product_detail(request, id):
    product = models.Product.objects.get(id=id)
    categorys = models.Category.objects.all()
    recomendation = models.Product.objects.filter(
        category_id=product.category.id).exclude(id=product.id)[:3]
    images = models.ProductImage.objects.filter(product_id=product.id)


    context = {
        'product':product,
        'categorys':categorys,
        'recomendation':recomendation,
        'images':images,
        'range':range(product.review)
    }
    return render(request, 'product/detail.html', context)


def carts(request):
    active = models.Cart.objects.filter(is_active=True, user=request.user)
    in_active = models.Cart.objects.filter(is_active=False, user=request.user)
    context = {
        'active':active,
        'in_active':in_active
    }
    return render(request, 'cart/carts.html', context)


def cart_detail(request, id):
    cart = models.Cart.objects.get(id=id)
    items = models.CartProduct.objects.filter(card=cart)
    context = {
        'cart':cart,
        'items':items
    }
    return render(request, 'cart/cart_detail.html', context)


def cart_detail_delete(request):
    item_id = request.GET['items_id']
    item = models.CartProduct.objects.get(id=item_id)
    cart_id = item.card.id
    item.delete()
    return redirect('main:cart_detail', cart_id)

def create_cart(request, id):           #agar foydalanuvchida Cart bo'lmasa yoki u aktiv bo'lmasa yangi Cart yaratadi
    product = models.Product.objects.get(id = id)
    if models.Cart.objects.filter(user = request.user, is_active = True):
        return redirect('main:add_to_cart', id_product = product.id, id_user = request.user.id)
    else:
        models.Cart.objects.create(
            user = request.user
        )
        return redirect ('main:add_to_cart', id_product = product.id, id_user = request.user)

def add_to_cart(request, id_product, id_user):
    product = models.Product.objects.get(id = id_product)
    cart = models.Cart.objects.get(user_id = id_user, is_active = True)
    previous_url = request.META.get('HTTP_REFERER')
    if models.CartProduct.objects.filter(product_id= id_product):
        data = models.CartProduct.objects.get(product_id = id_product)
        data.quantity +=1
        data.save()
        return redirect(previous_url)
    else:
        models.CartProduct.objects.create(
            product = product,
            card = cart,
            )
        return redirect(previous_url)




def edit_profile(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        user = request.user
        user.username = username
        user.first_name = first_name
        user.email = email
        user.save()
    return render(request, 'profile/edit.html')


def set_password(request):
    old = request.POST['old']
    new = request.POST['new']
    confirm = request.POST['confirm']
    user = request.user
    if user.check_password(old) and new == confirm:
        user.set_password(new)
        user.save()
    return redirect('main:edit_profile')

def create_wish_list(request):
    user = request.user
    product = models.Product.objects.get(id=request.POST['product_id'])
    models.WishList.objects.create(
        user=user,
        product=product # obj
    )
    # models.WishList.objects.create(
    #     user=request.user,
    #     product_id=request.GET['product_id'] # id
    # )
    # return redirect('main:index')


def list_wish_list(request):
    objects = models.WishList.objects.filter(user=request.user)
    return render(request, 'wish/list.html', {'objects':objects})


def delete_wish_list(request):
    models.WishList.objects.get(id=request.GET['id']).delete()
    return redirect('main:list_wish_list')

