from django.shortcuts import render
from promociones.models import Promocion

# Create your views here.
def index (request):
    promociones = Promocion.objects.all()
    return render(request, 'index.html', {'promociones': promociones})

