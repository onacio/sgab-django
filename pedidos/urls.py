from django.urls import path
from pedidos.views import index, novo

urlpatterns = [
    path('', index),
    path('novo/', novo),
]