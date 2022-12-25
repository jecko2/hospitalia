from django.urls import path
from . import views


app_name="checkout"
urlpatterns = [
path("checkout/<slug>/", views.product_checkout_view, name="checkout"),
path("payment-success/", views.mpesa_callback, name="mpesa_stk_push_callback"),
]
