from django.urls import path, include
from promociones import views


urlpatterns = [
    path("", views.promocion, name="promocion" ),
    path("<int:promocion_id>/", views.promocion1, name="promocion1"),
    path("<int:promocion_id>/", views.promocion2, name="promocion2"),
    path("<int:promocion_id>/", views.promocion3, name="promocion3"),
    path("<int:promocion_id>/", views.promocion4, name="promocion4"),
    path("<int:promocion_id>/", views.promocion5, name="promocion5"),
] 

