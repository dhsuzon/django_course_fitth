from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("this is coureses76677 page")
def about(request):
    return HttpResponse("this is about page")
def home(request):
    return HttpResponse("this is home page")