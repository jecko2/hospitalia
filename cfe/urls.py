from django.urls import path

from . import views

app_name="cfe"
urlpatterns = [
    path("", views.home_landing_view, name="home"),
    path("product/<slug>/", views.product_detail_view, name="item_detail"),
    path("category/<name>/", views.category_detail_view, name="category_detail"),
]