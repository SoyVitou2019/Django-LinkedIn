from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello, world!")

# render html
def home(request):
    return render(request, './home/index.html')

