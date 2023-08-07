from django.contrib import admin

from .models import Product, Client
 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock']
    ordering = ['id']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'firts_name', 'last_name', 'email']
