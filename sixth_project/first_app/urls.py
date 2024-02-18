from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('Delete/<int:Roll>', views.detete_student,name="detete_student"),
]
