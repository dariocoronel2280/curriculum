from django.shortcuts import render

# Create your views here.

from .models import product
# Create your views here.
def products(request):
    products = product.objects.all()      
    return render(request, "products/product.html",{"products":products})