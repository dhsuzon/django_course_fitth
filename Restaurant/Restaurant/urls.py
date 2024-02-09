
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include("About.urls")),
    path('ShowItem/', include("Meals.urls")),
    path('about/',views.Details, name="about"),
    path('',views.mainpage),
]
