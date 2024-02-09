
from django.http import HttpResponse

def home(request):
    return HttpResponse("this is home page2")


def contact(request):
    return HttpResponse("this is contact page1")