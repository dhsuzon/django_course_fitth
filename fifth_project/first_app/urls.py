

from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="homepage"),
    path('about/',views.about,name="aboutpage"),
    path('form/',views.submit_form,name="submit_form"),
    path('Django_form/',views.PasswordValidtion,name="Django_form"),
]
