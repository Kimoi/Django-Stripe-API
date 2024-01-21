import stripe
from django.shortcuts import get_object_or_404
from django.conf import settings
from payments.models import Item, Order


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

    return checkout_session


def create_order_checkout_session(request, pk):
    order = get_object_or_404(Order, id=pk)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        success_url=request.build_absolute_uri('/success'),
        cancel_url=request.build_absolute_uri(order.get_absolute_url()),
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
            } for item in order.items.all()
        ])

    return checkout_session
