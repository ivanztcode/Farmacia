from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
# from django.core.mail import EmailMessage
# Create your views here.

""" def contactoHome(request):
    #Instanciar el formulario para que django lo pueda utilizar
    #print ('tipo de peticion:{}'.format(request.method))
    contact_form =ContactForm()
    if request.method == "POST":
        #ESTOY ENVIANDO EL FORMULARIO 
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            message = request.POST.get('message','')

            #ENVIAR EL CORREO ELECTRONICO 
            email = EmailMessage(
                'Mensaje de Contacto Recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                'email',
                ['2a413732936da0@inbox.mailtrap.io'],
                reply_to=[email],
            )
            try:
                email.send()
                #esta todo ok
                return redirect(reverse('homeContacto')+'?ok')
            except:
                return redirect(reverse('homeContacto')+'?error')

    return render(request,"contactoHome.html",{"form":contact_form}) """

def Contact(request):
    contact_form =ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            #tengo que avisar esta todo ok 
            return redirect(reverse('homeContacto')+'?ok')
        else:
            #tengo que generar un error
            return redirect(reverse('homeContacto')+'?error')

    return render(request, 'contactoHome.html',{'form':contact_form})

