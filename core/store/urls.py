from django.urls import path

from .views import cart_view, checkout_view, StoreView

app_name = "store"

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
]
