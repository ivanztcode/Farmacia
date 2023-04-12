from django.contrib import admin
from django.utils.html import format_html
from django.templatetags.static import static
from django.utils import timezone



from .models import Proveedor,Medicamento, Categoria
# Register your models here.

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock','categoria','proveedor','imagen_tag','fecha_caducidad')
    readonly_fields = ('imagen_tag',)
    list_filter = ('categoria', 'proveedor', 'fecha_caducidad')
    search_fields = ("nombre", "descripcion")
    list_per_page = 5


    def imagen_tag(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" height="150" />'.format(static(obj.imagen.url)))
        else:
            return '(No imagen)'


admin.site.register(Proveedor)
admin.site.register(Medicamento,MedicamentoAdmin)
admin.site.register(Categoria)
