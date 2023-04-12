from django.urls import path,include
from informacion import views


urlpatterns = [
    path("",views.Contact,name="homeContacto")
]
