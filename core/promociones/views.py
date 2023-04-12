from django.shortcuts import render, get_object_or_404
from .models import Promocion

# Create your views here.

def promocion(request):
    promociones = Promocion.objects.all().values('imagen','name')
    context = {'promociones':promociones}
    return render(request, "promocion.html",context)

def promocion1(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    return render(request, 'promocion1.html', {'promocion': promocion})

def promocion2(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    return render(request, 'promocion2.html', {'promocion': promocion})

def promocion3(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    return render(request, 'promocion3.html', {'promocion': promocion})

def promocion4(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    return render(request, 'promocion4.html', {'promocion': promocion})
def promocion5(request, promocion_id):
    promocion = get_object_or_404(Promocion, id=promocion_id)
    return render(request, 'promocion5.html', {'promocion': promocion})


