from rest_framework import serializers
from .models import Brand, Category, Item, AdditionalPicture


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdditionalPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalPicture
        fields = '__all__'
