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
    path("perfil/", ProfileUpdateView.as_view(), name="perfil_edit"),
    path("perfis/publicos/", PublicProfileListView.as_view(), name="perfis_publicos"),
    path("perfis/publicos/<int:pk>/", ProfilePublicDetailView.as_view(), name="perfis_publicos_det"),

    # Certificados
    path("certificados/", CertificationListView.as_view(), name="certificados_list"),
    path("certificados/<int:pk>/", CertificationDetailView.as_view(), name="certificados_det"),
    path("certificados/add/", CertificationCreateView.as_view(), name="certificados_add"),
    path("certificados/<int:pk>/edit/", CertificationUpdateView.as_view(), name="certificados_edit"),
    path("certificados/<int:pk>/delete/", CertificationDeleteView.as_view(), name="certificados_delete"),

    # Habilidades
    path("habilidades/", ProfileSkillListView.as_view(), name="habilidades_list"),
    path("habilidades/novo/", ProfileSkillCreateView.as_view(), name="habilidades_create"),
    path("habilidades/<int:pk>/", ProfileSkillDetailView.as_view(), name="habilidades_detail"),
    path("habilidades/<int:pk>/editar/", ProfileSkillUpdateView.as_view(), name="habilidades_update"),
    path("habilidades/<int:pk>/excluir/", ProfileSkillDeleteView.as_view(), name="habilidades_delete"),

    # Sistemas
    path("sistemas/", ProfileSystemListView.as_view(), name="sistemas_list"),
    path("sistemas/novo/", ProfileSystemCreateView.as_view(), name="sistemas_create"),
    path("sistemas/<int:pk>/", ProfileSystemDetailView.as_view(), name="sistemas_detail"),
    path("sistemas/<int:pk>/editar/", ProfileSystemUpdateView.as_view(), name="sistemas_update"),
    path("sistemas/<int:pk>/excluir/", ProfileSystemDeleteView.as_view(), name="sistemas_delete"),
]
