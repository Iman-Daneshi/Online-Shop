from django.urls import path

from .views import cart_view, checkout_view, update_item, store_view

app_name = "store"

urlpatterns = [
    path('', store_view, name='store'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('update_item/', update_item, name='update_item'),
]
