from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'photo')
    search_fields = ('name', 'category__name', 'description')
    list_filter = ('category',)
    list_editable = ('price', 'stock')
    ordering = ('category',)