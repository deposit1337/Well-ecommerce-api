from django.shortcuts import render, get_object_or_404
import sys

sys.path.append('D:/Well-ecommerce-api/main/')
from catalog.models import Item
from .basket import Basket
from django.http import JsonResponse


# Create your views here.


def basket_summary(request):
    return render(request, 'catalog/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('itemid'))
        item_qty = int(request.POST.get('itemqty'))
        item = get_object_or_404(Item, id=item_id)
        basket.add(item, qty=item_qty)

        response = {
            'qty': item_qty
        }

        return JsonResponse(response)
