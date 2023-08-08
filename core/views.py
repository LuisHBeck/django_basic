from django.shortcuts import render, get_object_or_404, HttpResponse
from django.template import loader
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
    # prod = Product.objects.get(id=pk)
    
    prod = get_object_or_404(Product, id=pk)
    
    context = {
        'product': prod
    }
    return render(request, 'product.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
