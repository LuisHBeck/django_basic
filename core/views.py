from django.shortcuts import render

def index(request):
    context = {
        'course': 'Web Programming with Django Framework',
        'language': 'Python',
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
