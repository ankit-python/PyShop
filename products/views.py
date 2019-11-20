from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# products = Call the index function
def index(request):
    products = Product.objects.all()
    # Product.objects.save()
    # Product.objects.filter()
    # Product.objects.get()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products ')

