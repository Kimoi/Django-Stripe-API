import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.decorators.http import require_GET
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Item


@api_view()
def create_checkout_session(request, pk):
    item = get_object_or_404(Item, id=pk)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        success_url=request.build_absolute_uri('/success'),
        cancel_url=request.build_absolute_uri(item.get_absolute_url()),
        mode='payment',
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1
            }])

    return JsonResponse(checkout_session, status=200)


@require_GET
def get_item(request, pk):
    item = Item.objects.get(id=pk)
    return render(request, 'payments/item.html', {'item': item, 'stripe_key': settings.STRIPE_PUBLISHABLE_KEY})


class SuccessView(View):
    def get(self, request):
        return render(request, 'payments/success.html', status=200)
