from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/compare/', views.price_comparison, name='price_comparison'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_price/', views.add_price, name='add_price'),
]
