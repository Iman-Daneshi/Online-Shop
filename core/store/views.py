from email.headerregistry import Address
from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (ListView, DetailView)
from django.http import JsonResponse
import json
import datetime

from .models import Customer, Product, Order, OrderItem, ShippingAddress
from .utils import cookieCart, cartData, guestOrder


def store_view(request):
  data = cartData(request)
  cartItems = data['cartItems']

  products = Product.objects.all()
  context = {'products': products, 'cartItems': cartItems}

  return render(request, 'store/store.html', context)


def cart_view(request):
  data = cartData(request)
  cartItems = data['cartItems']
  items = data['items']
  order = data['order']

  context = {
      'items': items,
      'order': order,
      'cartItems': cartItems,
  }

  return render(request, 'store/cart.html', context)


def checkout_view(request):  
  data = cartData(request)
  cartItems = data['cartItems']
  items = data['items']
  order = data['order']

  context = {
    'items': items,
    'order': order,
    'cartItems': cartItems,
  }

  return render(request, 'store/checkout.html', context)


def update_item(request):
  data = json.loads(request.body)
  productId = int(data['productId'])
  action = data['action']
  print(productId, action)

  customer = request.user.customer
  product = Product.objects.get(id=productId)
  order, created = Order.objects.get_or_create(
    customer=customer, complete=False)
  orderItem, created = OrderItem.objects.get_or_create(
    order=order, product=product)

  if action == 'add':
    orderItem.quantity += 1
  elif action == 'remove':
    orderItem.quantity -= 1
  orderItem.save()

  if orderItem.quantity <= 0:
    orderItem.delete()

  return JsonResponse('Item was added', safe=False)


def processOrder(request):
  transaction_id = datetime.datetime.now().timestamp()
  data = json.loads(request.body)

  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(
      customer=customer, complete=False)

  else:
    customer, order = guestOrder(request, data)

  total = float(data['form']['total'])
  order.transaction_id = transaction_id

  
  if total == float(order.get_cart_total):
    order.complete = True
  order.save()

  if order.shipping == True:
    ShippingAddress.objects.create(
      customer=customer,
      order=order,
      address=data['shipping']['address'],
      city=data['shipping']['city'],
      state=data['shipping']['state'],
      zipcode=data['shipping']['zipcode'],
    )

  return JsonResponse('payment done', safe=False)
