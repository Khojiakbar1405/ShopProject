from django.db import models
from django.contrib.auth.models import User
from functools import reduce
import slug
from unidecode import unidecode

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slug.slug(unidecode(self.name, 'UTC-8'))
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.SmallIntegerField(
        choices=(
            (1,'Dollar'), 
            (2, 'So`m')
            )
    ) 
    discount_price = models.DecimalField(
        decimal_places=2, 
        max_digits=10, 
        blank=True, 
        null=True
        )
    baner_image = models.ImageField(upload_to='baner/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slug.slug(unidecode(self.name, 'UTC-8'))
        super(Product, self).save(*args, **kwargs)


    @property
    def review(self):
        reviews = ProductReview.objects.filter(product_id=self.id)
        result = reduce(lambda result, x: result +x, reviews, 0)
        try:
            result = result / reviews.count()
        except ZeroDivisionError:
            result = 0
        return result
    
    @property 
    def is_discount(self):
        if self.discount_price is None:
            return 0
        return self.discount_price > 0
    
    @property 
    def is_active(self):
        return self.quantity > 0
    

    def increment_quantity(self, amount):
        self.quantity += amount
        self.save()

    @property 
    def images(self):
        images = ProductImage.objects.filter(product_id=self.id)
        return images

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,) # releted_name='images'



class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        object = WishList.objects.filter(
            user=self.user,
            product=self.product
            )
        if object.count() == 0:
            super(WishList, self).save(*args, **kwargs)
        else:
            raise ValueError
        
        # if self.pk:
        #     print(222)
        # else:
        #     print(111)

        super(WishList, self).save(*args, **kwargs)
    
    def delete(self, *args, **kargs):
        ...
        super(WishList, self).delete(*args, **kargs)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    mark = models.SmallIntegerField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    @property
    def quantity(self):
        quantity = 0
        products = CartProduct.objects.filter(product_id = self.id)
        for i in products:
            quantity +=i.quantity
        return quantity

    @property
    def total_price(self):
        result = 0
        for i in CartProduct.objects.filter(card_id=self.id):
            result +=(i.product.price)*i.quantity
        return result


class CartProduct(models.Model):
    card = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    @property
    def total_price(self):
        if self.product.is_discount:
            result = self.product.discount_price * self.quantity
        else:
            result = self.product.price * self.quantity
        return result


class EnterProduct(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity}"
    
    def save(self, *args, **kwargs):
        self.product_name = self.product.name
        if self.pk:
            enter = EnterProduct.objects.get(pk=self.pk)
            product = enter.product # None/Product
            product.quantity -= enter.quantity
            product.quantity += self.quantity
            product.save()
        else:
            self.product.quantity += self.quantity
            self.product.save()
        super(EnterProduct, self).save(*args, **kwargs)