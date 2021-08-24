from django.shortcuts import render
from django.http import HttpResponse

def greetings(request):
    return HttpResponse("<h1>Khuram Shehzad</h1>")

def hello(request):
    return HttpResponse("<h1>Django is fun</h1>")

def welcome(request):
    return render(request,"welcome.html")