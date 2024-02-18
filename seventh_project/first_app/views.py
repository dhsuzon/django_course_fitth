from django.shortcuts import render
from first_app.forms import StudentFrom

# Create your views here.

def home(request):
   if request.method == "POST":
       std = StudentFrom(request.POST)
       if std.is_valid():
           std.save()
           print(std.cleaned_data)
   else:
        std = StudentFrom()
   return render(request, 'home.html',{'form':std})
