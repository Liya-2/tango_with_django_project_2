from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    # return HttpResponse("Rango says hey there partner!")

    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("Rango says here is the about page.")
