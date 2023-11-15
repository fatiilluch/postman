from django.shortcuts import render
from django.http import HttpResponse
from .models import APIRequest

def index(request):
    return HttpResponse("Index de la App imitando a postman")

def request_list(request):
    # Recuperar todas las solicitudes de la base de datos
    requests = APIRequest.objects.all()
    
    # Pasar los datos a un template HTML para mostrarlos
    return render(request, 'request_list.html', {'requests': requests})

def create_request(request):
    if request.method == 'POST':
        headers = request.POST.get('headers', '') # obtiene los headers
        body = request.POST.get('body', '') # obtiene el body
        method = request.POST.get('method', '')
        url = request.POST.get('url', '')
        
        new_request = APIRequest.objects.create(
            headers = headers,
            body = body,
            method = method,
            url = url            
        )
        
        # Redireccionar a una página de éxito o a donde desees después de crear la solicitud
        return render(request, 'success.html', {'request': new_request}) 

    # Si la solicitud no es POST o hay algún error, muestra el formulario
    return render(request, 'request_form.html')
        