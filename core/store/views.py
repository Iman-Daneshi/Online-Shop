from email.headerregistry import Address
from multiprocessing import context
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import (ListView, DetailView)
from django.http import JsonResponse
import json
import datetime

from .models import Customer, Product, Order, OrderItem, ShippingAddress
# Create your views here.


def store_view(request):
  if request.user.is_authenticated:
    customer =request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  products = Product.objects.all()
  context = {'products':products, 'cartItems':cartItems}
  return render(request, 'store/store.html', context)

def cart_view(request):
  if request.user.is_authenticated:
    customer =request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
  else:
    items = []
    order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

  context = {
    'items':items,
    'order':order,
    'cartItems':cartItems,
  }
  
  return render(request, 'store/cart.html',context)



def checkout_view(request):
  if request.user.is_authenticated:
    customer =request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items

  else:
    items = []
    order = {'get_cart_total':0,'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']


  context = {
    'items':items,
    'order':order,
    'cartItems':cartItems,

  }
  
  
  return render(request, 'store/checkout.html',context)


def update_item(request):
  data = json.loads(request.body)
  productId = int(data['productId'])
  action = data['action']
  print(productId, action)

  customer = request.user.customer
  product = Product.objects.get(id=productId)
  order, created= Order.objects.get_or_create(customer=customer, complete=False)
  orderItem, created= OrderItem.objects.get_or_create(order=order, product=product)

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
  print(request.user)

  if request.user.is_authenticated:
    customer = request.user.customer
    order, created= Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    
    if total == order.get_cart_total :
      order.complete = True
    order.save()

    if order.shipping == True:
      ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address = data['shipping']['address'],
        city = data['shipping']['city'],
        state = data['shipping']['state'],
        zipcode = data['shipping']['zipcode'],
      )


  else:
    print('user is not logged in')
  return JsonResponse('payment done', safe=False)