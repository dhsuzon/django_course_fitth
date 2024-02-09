from django.shortcuts import render,HttpResponse

def Details(request):
    return render(request,'about.html')

def mainpage(request):
    return HttpResponse("Restaurant project sucessfully created")