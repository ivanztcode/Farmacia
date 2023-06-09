"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from accounts.views import exit, register



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("promociones/",include("promociones.urls"),),
    path("medicamentos/",include("medicamentos.urls")),
    path("contacto/",include("informacion.urls")),
    path("doctores/",include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", exit, name='exit'),
    path("register/",register, name="register")


    
]
