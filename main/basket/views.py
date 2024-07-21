from django.shortcuts import render, get_object_or_404
import sys

sys.path.append('D:/Well-ecommerce-api/main/')
from catalog.models import Item
from .basket import Basket
from django.http import JsonResponse


# Create your views here.


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'catalog/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('itemid'))
        item_qty = int(request.POST.get('itemqty'))
        item = get_object_or_404(Item, id=item_id)

        basket.add(item, qty=item_qty)
        basketqty = basket.__len__()

        response = JsonResponse({
            'qty': basketqty
        })

        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'delete':
        item_id = int(request.POST.get('itemid'))
        basket.delete(item=item_id)
        baskettotal = basket.get_total_price()
        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})

        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'update':
        item_id = int(request.POST.get('itemid'))
        item_qty = int(request.POST.get('itemqty'))
        basket.update(item=item_id, qty=item_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()


        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
