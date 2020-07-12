from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Product

def index(request):
    return render(request, 'companyProfile/index.html')

def product_index(request):
    products = Product.objects.order_by("product_name")
    context = {'products': products}
    return render(request, 'companyProfile/product_index.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'companyProfile/product_template.html', context)

def contact(request, product_id):
    return render(request, 'companyProfile/contact.html')
