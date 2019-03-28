from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # response = HttpResponse()
             # response.writelines("<h1>Xin chao</h1>")
    return render(request, 'pages/home.html')

def contact(request):
    return render(request, 'pages/contact.html')

def error(request):
    return render(request, 'pages/error.html')