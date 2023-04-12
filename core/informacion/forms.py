from django import forms
from .models import Contact
#Importamos los fromularios muy parecidos a los modelos.

# class ContactForm(forms.Form):
#     name = forms.CharField(label="Nombre y Apellido", required=True, min_length=5, max_length=25,
#                            widget=forms.TextInput(attrs={'class':'form-control','placeholder':"Introduzca sus datos"}))
#     email = forms.EmailField(label='Correo Electrónico', required=True, max_length=100, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Introduzca su email'}))

#     message = forms.CharField(label='Mensaje', required=True, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escriba aquí su mensaje...','rows':5}))

#     #rows es igual a las lineas 
    
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = '__all__'
        fields = ['name','email','message','contact_type','subscription']