from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#a function  that takes a request and  and return a response
#reques handler


def say_hello(request):
    return render(request,     "index.html",{'name':"capiyo"})
#mapping urls to vies
