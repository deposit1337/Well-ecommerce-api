from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer


class ItemView(viewsets.ViewSet):
    # Class based viewset to all items

    queryset = Item.objects.all()

    def list(self, request):
        serializer = ItemSerializer(self.queryset, many=True)
        return Response(serializer.data)
