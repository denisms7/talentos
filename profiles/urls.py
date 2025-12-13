from django.urls import path

from .views import (
    ProfileUpdateView,
    ProfilePublicDetailView,
    PublicProfileListView,

    # Certificados
    CertificationListView,
    CertificationCreateView,
    CertificationDetailView,
    CertificationUpdateView,
    CertificationDeleteView,

    # Habilidades
    ProfileSkillListView,
    ProfileSkillCreateView,
    ProfileSkillDetailView,
    ProfileSkillUpdateView,
    ProfileSkillDeleteView,

    # Sistemas
    ProfileSystemListView,
    ProfileSystemCreateView,
    ProfileSystemDetailView,
    ProfileSystemUpdateView,
    ProfileSystemDeleteView,
)

app_name = "profiles"

urlpatterns = [
    # Perfil
    path("edit/", ProfileUpdateView.as_view(), name="perfil_edit"),
    path("public/", PublicProfileListView.as_view(), name="perfis_publicos"),
    path("<int:pk>/public/", ProfilePublicDetailView.as_view(), name="perfis_publicos_det"),

    # Certificados
    path("certificates/", CertificationListView.as_view(), name="certificados_list"),
    path("certificates/add/", CertificationCreateView.as_view(), name="certificados_add"),
    path("certificates/<int:pk>/", CertificationDetailView.as_view(), name="certificados_det"),
    path("certificates/<int:pk>/edit/", CertificationUpdateView.as_view(), name="certificados_edit"),
    path("certificates/<int:pk>/delete/", CertificationDeleteView.as_view(), name="certificados_delete"),

    # Habilidades
    path("skills/", ProfileSkillListView.as_view(), name="habilidades_list"),
    path("skills/add/", ProfileSkillCreateView.as_view(), name="habilidades_create"),
    path("skills/<int:pk>/", ProfileSkillDetailView.as_view(), name="habilidades_detail"),
    path("skills/<int:pk>/edit/", ProfileSkillUpdateView.as_view(), name="habilidades_update"),
    path("skills/<int:pk>/delete/", ProfileSkillDeleteView.as_view(), name="habilidades_delete"),

    # Sistemas
    path("systems/", ProfileSystemListView.as_view(), name="sistemas_list"),
    path("systems/add/", ProfileSystemCreateView.as_view(), name="sistemas_create"),
    path("systems/<int:pk>/", ProfileSystemDetailView.as_view(), name="sistemas_detail"),
    path("systems/<int:pk>/edit/", ProfileSystemUpdateView.as_view(), name="sistemas_update"),
    path("systems/<int:pk>/delete/", ProfileSystemDeleteView.as_view(), name="sistemas_delete"),
]
