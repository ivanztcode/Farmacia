from django.shortcuts import render
from django.utils import timezone
from .models import Medicamento, Categoria
# Create your views here.

from django.shortcuts import render
from django.utils import timezone
from .models import Medicamento
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import Http404



def medicamentosHome(request):
    # listamedicamentos = Medicamento.objects.all()
    #listamedicamentos = Medicamento.objects.order_by('nombre')
    listamedicamentos = Medicamento.objects.filter(stock__gt=1).order_by('stock')
  # obtiene los medicamentos de la página actual
    page = request.GET.get("page",1)
    try:
        paginator = Paginator(listamedicamentos,3)
        listamedicamentos = paginator.page(page)
    except:
        raise Http404
    

    fecha_actual = timezone.now().date()
    fecha_limite_1 = fecha_actual + timezone.timedelta(days=30)  # medicamentos que caducan en menos de un mes
    fecha_limite_2 = fecha_actual + timezone.timedelta(days=90)  # medicamentos que caducan en menos de tres meses
    fecha_limite_3 = fecha_actual + timezone.timedelta(days=180)  # medicamentos que caducan en menos de seis meses
    medicamentos_rojos = Medicamento.objects.filter(fecha_caducidad__gte=fecha_actual, fecha_caducidad__lte=fecha_limite_1).order_by('fecha_caducidad')
    medicamentos_naranjas = Medicamento.objects.filter(fecha_caducidad__gt=fecha_limite_1, fecha_caducidad__lte=fecha_limite_2).order_by('fecha_caducidad')
    medicamentos_amarillos = Medicamento.objects.filter(fecha_caducidad__gt=fecha_limite_2, fecha_caducidad__lte=fecha_limite_3).order_by('fecha_caducidad')
    medicamentos_muy_bajos = Medicamento.objects.filter(stock__lt=3).order_by('stock')
    medicamentos_bajos = Medicamento.objects.filter(stock__gte=3, stock__lte=7).order_by('stock')
    medicamentos_bajo_medio = Medicamento.objects.filter(stock__gt=7, stock__lte=10).order_by('stock')

    categorias = Categoria.objects.all()
    medicamentos_por_categoria={}
    for categoria in categorias:
        medicamentos = Medicamento.objects.filter(categoria=categoria).order_by('nombre')
        medicamentos_por_categoria[categoria] = medicamentos

    context ={
        'medicamentos_rojos': medicamentos_rojos,
        'medicamentos_naranjas':medicamentos_naranjas,
        'medicamentos_amarillos':medicamentos_amarillos,
        'medicamentos_muy_bajos': medicamentos_muy_bajos,
        'medicamentos_bajos':medicamentos_bajos,
        'medicamentos_bajo_medio':medicamentos_bajo_medio,
        'medicamentos_por_categoria':medicamentos_por_categoria,
        'listamedicamentos':listamedicamentos,
        'paginator':paginator,
    }
    return render(request, 'medicamentosHome.html', context)



def medicamentos(request):
    medicamentos = Medicamento.objects.order_by('nombre')
    nombres_medicamentos = list(medicamentos.values_list('nombre', flat=True))
    query = request.GET.get('search')
    if query:
        medicamentos = medicamentos.filter(Q(nombre__icontains=query))

    context = {
        'medicamentos': medicamentos,
        'nombres_medicamentos': nombres_medicamentos
    }
    return render(request, 'medicamentos.html', context)

def search(request):
    buscador=request.GET["buscador"]
    listamedicamentos = Medicamento.objects.filter(nombre__icontains=buscador)
    context = {'listamedicamentos':listamedicamentos}
    return render(request, 'medicamentosHome.html', context)

