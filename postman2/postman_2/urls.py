from django.urls import path
from .views import index, request_list, create_request

urlpatterns = [
    path('', index, name="index"),
    path('requests/', request_list, name="requests-list"),
    path('create-request/', create_request, name="create-request")
]
