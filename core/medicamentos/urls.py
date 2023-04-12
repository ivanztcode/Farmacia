from django.urls import path, include
from medicamentos import views
from . import views



urlpatterns = [
    path("", views.medicamentosHome, name="homeMedicamentos" ),
    path("search/", views.search, name="search" ),
    path("medicamentos/", views.medicamentos, name="medicamentos")

    ]