from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pedidos/index.html')

def novo(request):
    return render(request, 'pedidos/novo.html')