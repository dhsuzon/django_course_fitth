
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.ShowItem ,name='ShowItem' ),
    
]