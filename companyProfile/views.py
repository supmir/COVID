from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Product
from .models import Content


def index(request):
    return render(request, 'companyProfile/index.html')


def product_index(request):
    products = Product.objects.order_by("product_name")
    context = {'products': products}
    return render(request, 'companyProfile/product_index.html', context)


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    # content = product.content_set.all().order_by('sequence')
    contents = Content.objects.filter(product_id=int(product_id)).order_by('sequence')
    context = {'product': product, 'contents': contents}
    return render(request, 'companyProfile/product_template.html', context)


def contact(request):
    return render(request, 'companyProfile/contact.html')
