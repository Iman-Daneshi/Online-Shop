from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (ListView, DetailView)

from .models import Customer, Product, Order, OrderItem, ShippingAddress
# Create your views here.


class StoreView(ListView):
  queryset = Product.objects.all()
  context_object_name = 'products_list'
  template_name = 'store/store.html'

def cart_view(request):
  if request.user.is_authenticated:
    customer =request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    items = order.orderitem_set.all()
  else:
    items = []
    order = {'get_cart_total':0,'get_cart_items':0}
  context = {
    'items':items,
    'order':order,
  }
  
  return render(request, 'store/cart.html',context)



def checkout_view(request):
  if request.user.is_authenticated:
    customer =request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    items = order.orderitem_set.all()
  else:
    items = []
    order = {'get_cart_total':0,'get_cart_items':0}
  context = {
    'items':items,
    'order':order,
  }
  
  return render(request, 'store/checkout.html',context)