from django.urls import path

from .views import (
    ProfileDetailView,
    ProfileUpdateView,
)

app_name = "profiles"

urlpatterns = [
    # ===== PERFIL =====
    path("", ProfileDetailView.as_view(), name="home"),
    path("editar/", ProfileUpdateView.as_view(), name="edit"),

]
