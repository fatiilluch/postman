from django.db import models

# Create your models here.

class APIRequest(models.Model):
    """
        A model for storiing information about the API requests made. 
        :params:
            method: HTTP method that will be used to make API requests (GET, POST, PUT, DELETE)
                type: CharField
            url: request url 
                type: CharField
            headers: Request Headers
                type: JsonField
            body: Request body
                type: JsonField
            timestamp: Date and time of the request
                type: DateTimeField          
                
            Ejemplo de creacion de una APIrequest    
            new_request = APIRequest.objects.create(
                # Otros campos...
                headers={"Content-Type": "application/json", "Authorization": "Bearer <token>"},
                body={"key": "value"}
            )
    """
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'

    METHOD_CHOICES = [
        (GET, 'GET'),
        (POST, 'POST'),
        (PUT, 'PUT'),
        (DELETE, 'DELETE'),
    ]

    method = models.CharField(max_length=6, choices=METHOD_CHOICES)
    url = models.CharField(max_length=300)      
    headers = models.JSONField(default=dict) # establece un diccionario vacío como valor predeterminado para este campo.
    body = models.JSONField(default=dict, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) # establece automáticamente el valor del campo timestamp en la fecha y hora en que se crea la instancia de APIRequest
    
    def __str__(self):
        """ 
            Defines how an APIResponse object is represented as a string. 
            In this case, it shows basic information about the response.
        """
        return self.url
    

class APIResponse(models.Model):
    """
        A model for storiing information about the API requests made. 
        :params:
            request: A Foreign key that establish a relationship with the API request model, indicating that this response is associated with qn specific request.
                type: ForeignKey
            status_code: A field that stores the HTTP status code of the API request.
                type: IntegerField
            headers: A field to store the response headers in JSON format
                type: JsonField
            body: An optional field to store the body of the response in JSON format
                type: JsonField
            timestamp: Date and time of the request
                type: DateTimeField          
    """

    request  = models.ForeignKey('APIRequest', on_delete=models.CASCADE) # on_delete=models.CASCADE indica que si la solicitud asociada se elimina, también se eliminará esta respuesta.
    status_code = models.IntegerField()
    headers = models.JSONField(default=dict) # establece un diccionario vacío como valor predeterminado para este campo.
    body = models.JSONField(default=dict, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True) # establece automáticamente el valor del campo timestamp en la fecha y hora en que se crea la instancia de APIRequest
    
    def __str__(self):
        """ 
            Defines how an APIResponse object is represented as a string. 
            In this case, it shows basic information about the response.
        """
        return f"Response for {self.request} - Status: {self.status_code}"


"""

3. APIEnvironment:

Un modelo para representar diferentes entornos de API, como desarrollo, pruebas, producción, etc. Podría contener campos como:

    name: Nombre del entorno.
    base_url: URL base del entorno.

4. APICollection:

Un modelo para agrupar solicitudes relacionadas, por ejemplo, todas las solicitudes para una API específica o una función en tu aplicación. Podría contener campos como:

    name: Nombre de la colección.
    description: Descripción de la colección.
    requests: Una relación que enlaza con las solicitudes asociadas a esta colección.

Estos son solo ejemplos de modelos que podrían formar la base de una herramienta similar a Postman en Django. Puedes ajustar y expandir estos modelos según las características específicas que desees implementar en tu aplicación. Recuerda que la clave es diseñar los modelos de acuerdo a las funcionalidades y relaciones que quieras representar en tu herramienta.
ChatGPT can make mistakes. Consider checking important information.
"""
