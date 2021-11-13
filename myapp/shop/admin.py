from django.contrib import admin

# Register your models here.
from .models import Product,Introduction
admin.site.register(Product)
admin.site.register(Introduction)