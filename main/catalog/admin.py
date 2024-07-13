from django.contrib import admin
from .models import Item, AdditionalPicture, Brand, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('brand', 'full_name', 'vendor', 'description', 'main_picture',)
    # search_fields = ('name', 'brand1_name', 'brand2_name')
    # list_filter = ('brand1_name', 'brand2_name')


@admin.register(AdditionalPicture)
class AdditionalPictureAdmin(admin.ModelAdmin):
    list_display = ('picture',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'broad_name')
