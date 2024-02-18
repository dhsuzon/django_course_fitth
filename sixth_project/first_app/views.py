from django.shortcuts import render,redirect
from. import models

student =  models.Student.objects.all()

# Create your views here.

def home(request):
    return render(request, 'home.html',{'student': student})


def detete_student(request,Roll):
    
    std = models.Student.objects.get(pk = Roll).delete()
    return redirect("homepage")
   