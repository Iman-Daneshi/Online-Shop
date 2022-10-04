from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
  empty_value_display = '-empty-'
  list_display = ('user', 'name', 'email')
  list_filter  = ('email','name')
  ordering = ['-name',]
  search_fields = ['name', 'email']

class ProductAdmin(admin.ModelAdmin):
  empty_value_display = '-empty-'
  list_display = ('name', 'price')
  list_filter  = ('digital',)
  ordering = ['-name',]
  search_fields = ['name', 'price']

class OrderAdmin(admin.ModelAdmin):
  date_hierarchy = 'date_ordered'
  empty_value_display = '-empty-'
  list_display = ('customer', 'date_ordered', 'complete', 'transaction_id')
  list_filter  = ('customer', 'date_ordered', 'complete', )
  ordering = ['date_ordered',]
  search_fields = ['customer', 'complete']
  
class OrderItemAdmin(admin.ModelAdmin):
  date_hierarchy = 'date_added'
  empty_value_display = '-empty-'
  list_display = ('product', 'order', 'quantity')
  list_filter  = ('order', 'quantity',)
  ordering = ['date_added',]
  search_fields = ['date_added','product']

class ShippingAdressAdmin(admin.ModelAdmin):
  date_hierarchy = 'date_added'
  empty_value_display = '-empty-'
  list_display = ('customer', 'order', 'address', 'zipcode')
  list_filter  = ('state', 'city',)
  ordering = ['-date_added',]
  search_fields = ['customer', 'address']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAdressAdmin)
