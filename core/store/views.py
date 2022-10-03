from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class StoreView(TemplateView):
  template_name = 'store/store.html'

class CartView(TemplateView):
  template_name = 'store/cart.html'

class CheckoutView(TemplateView):
  template_name = 'store/checkout.html'