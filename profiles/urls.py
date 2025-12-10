from django.urls import path

from .views import (
    ProfileDetailView,
    ProfileUpdateView,
    ProfileSkillCreateView,
    CertificationCreateView,
    CertificationListView,
    ProfileSkillManageView,
    toggle_profile_skill,

)

app_name = "profiles"

urlpatterns = [
    path("detalhe/", ProfileDetailView.as_view(), name="detail"),
    path("editar/", ProfileUpdateView.as_view(), name="edit"),
    path("skills/adicionar/", ProfileSkillCreateView.as_view(), name="skill_add"),
    path(
        "certificados/",
        CertificationListView.as_view(),
        name="certification_list",
    ),
    path(
        "certificados/adicionar/",
        CertificationCreateView.as_view(),
        name="certification_add",
    ),

    path(
        "skills/",
        ProfileSkillManageView.as_view(),
        name="skills-manage",
    ),
    path(
        "skills/toggle/",
        toggle_profile_skill,
        name="skills-toggle",
    ),


]
