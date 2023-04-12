from django.contrib import admin

# Register your models here.

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','contact_type','created_at','subscription')
    search_fields =('name','email','message')
    list_filter = ('name','email')

admin.site.register(Contact, ContactAdmin)