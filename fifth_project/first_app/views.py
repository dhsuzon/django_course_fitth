from django.shortcuts import render
from .forms  import ContactForm,PasswordValidationProject,student_data

# Create your views here.
def home(request):
    return render(request,'./first_app/home.html')

def about(request):
    if request.method == 'POST':
       
        name = request.POST.get('username')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request,'./first_app/about.html',{'name':name, 'email':email,'select':select})

    else:
         return render(request,'./first_app/about.html')

def submit_form(request):
       return render(request,'./first_app/form.html')
def DjangoForm(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
          
    else:
        form = ContactForm()
    return render(request,'./first_app/djangoform.html',{'form':form})


def StudentForm(request):
    if request.method == 'POST': 
        form = student_data(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
          
    else:
        form = student_data()
    return render(request,'./first_app/djangoform.html',{'form':form})


def PasswordValidtion(request):
    if request.method == 'POST': 
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
          
    else:
        form = PasswordValidationProject()
    return render(request,'./first_app/djangoform.html',{'form':form})
