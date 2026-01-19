from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("<H2> Welcome, this is the Home Page</H2>")
    return render(request, 'home.html')