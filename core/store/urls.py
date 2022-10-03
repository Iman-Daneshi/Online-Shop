from django.urls import path

from.views import CartView, CheckoutView, StoreView

app_name = "store"

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
