from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_profile(request):
    if request.method =='POST':
      author_profile = forms.ProfileForm(request.POST)
      if  author_profile.is_valid():
          author_profile.save()
          return redirect('add_profile')
   
    else:
       author_profile = forms.ProfileForm()
    return render(request, 'add_profile.html',{'form': author_profile})

