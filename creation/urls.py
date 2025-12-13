from django.urls import path
from .views import (AccessRequestCreateView,)

app_name = "creation"

urlpatterns = [
    # Certificados
    path("solicitar-acesso/", AccessRequestCreateView.as_view(), name="solicitar_acesso"),
]
