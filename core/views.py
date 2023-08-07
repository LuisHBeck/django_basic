from django.shortcuts import render
from .models import Product

def index(request):
    logged = "you'rent logged in" if request.user.is_anonymous else "you're logged in"  
    
    products = Product.objects.all() 
    
    context = {
        'course': 'Web Programming with Django Framework',
        'language': 'Python',
        'logged': logged,
        'products': products,
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request, pk):
    prod = Product.objects.get(id=pk)
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)
