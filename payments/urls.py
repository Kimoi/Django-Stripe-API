from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:pk>/', views.create_checkout_session, name='create_checkout_session'),
    path('item/<int:pk>/', views.get_item, name='get_item'),
    path('success/', views.SuccessView.as_view()),
]
