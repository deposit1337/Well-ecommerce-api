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
    return render(request, 'catalog/index.html', {'categories': categories})

