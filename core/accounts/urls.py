from django.urls import path, include
from accounts import views

urlpatterns = [
    path("",views.doctoresHome,name="homeDoctores"),
    
]
