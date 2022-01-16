import os

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


def get_image_path(instance, filename):
    return os.path.join('uploads', filename)


class Product(models.Model):
    # basic info，基本屬性
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(blank=False, max_digits=65, decimal_places=0)
    img = models.ImageField(upload_to=get_image_path, default=get_image_path(instance=0, filename='product-1.jpg'))

    # discount，跟折扣相關的屬性
    on_sale = models.BooleanField(blank=True, null=True)
    tag = models.CharField(max_length=20, blank=True, null=True)
    percent_off = models.DecimalField(blank=True, null=True, max_digits=30, decimal_places=1)
    sale_price = models.DecimalField(blank=True, null=True, max_digits=30, decimal_places=0)

    # for analysis，網頁使用者看不到，但可事後分析的屬性
    bought_counter = models.DecimalField(default=0, max_digits=30, decimal_places=0)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
