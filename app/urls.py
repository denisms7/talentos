from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import ProfileDetailView


urlpatterns = [

    # Pagina principal
    path("", ProfileDetailView.as_view(), name="home"),

    # Admin
    path('admin/', admin.site.urls),

    # Perfil
    path("profiles/", include("profiles.urls")),

    # auth / accounts
    path("accounts/", include("user.urls")),
    path("accounts/", include("creation.urls")),

    # habilidades
    path("skills/", include("skills.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
