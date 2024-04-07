from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'pedidos/index.html')

def novo(requests):
    return render(requests, 'pedidos/novo.html')