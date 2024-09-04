from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:product_id>/compare/', views.price_comparison, name='price_comparison'),
]
