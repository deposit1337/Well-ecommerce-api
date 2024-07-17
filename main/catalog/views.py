from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import sys
from .models import Item, Brand, AdditionalPicture, Category
from .serializers import ItemSerializer, CategorySerializer, BrandSerializer, AdditionalPictureSerializer

sys.path.append('D:/Well-ecommerce-api/main/')
from drf_spectacular.utils import extend_schema

from django.shortcuts import get_object_or_404


class ItemView(viewsets.ViewSet):
    # Class based viewset to all items

    queryset = Item.objects.all()

    @extend_schema(responses=ItemSerializer)
    def list(self, request):
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)


class CategoryView(viewsets.ViewSet):
    # Class based viewset to all categories

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


def home_page(request):
    categories = Category.objects.all()
    first_three_categories = categories[:3]
    next_three_categories = categories[3:6]
    return render(request, 'catalog/index.html',
                  {'first_three_categories': first_three_categories, 'next_three_categories': next_three_categories})



def catalog(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    items = Item.objects.filter(category_name=category)
    return render(request, 'catalog/catalog.html', {'category': category, 'items': items})

def item_detail(request, category_slug, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'catalog/item-of-category.html', {'category_slug': category_slug, 'item': item})


def cart(request):
    return render(request, 'catalog/cart.html')