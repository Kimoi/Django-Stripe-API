from django.conf import settings
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from rest_framework.decorators import api_view
from django.http import JsonResponse
from . import services
from .models import Item, Order


@api_view()
def create_checkout_session(request, pk):
    checkout_session = services.create_checkout_session(request, pk)
    return JsonResponse(checkout_session, status=200)


@require_GET
def get_item(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'payments/item.html', {
        'item': item,
        'stripe_key': settings.STRIPE_PUBLISHABLE_KEY,
    })


def create_order_checkout_session(request, pk):
    checkout_session = services.create_order_checkout_session(request, pk)
    return JsonResponse(checkout_session, status=200)


@require_GET
def get_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    items = order.items.all()
    total_price = sum(item.price for item in items)
    return render(request, 'payments/order.html', {
        'order': order,
        'items': items,
        'price': total_price,
        'stripe_key': settings.STRIPE_PUBLISHABLE_KEY,
    })


class SuccessView(View):
    def get(self, request):
        return render(request, 'payments/success.html', status=200)
