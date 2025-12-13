from django.urls import path
from .views import SystemListView, SkillListView, FunctionListView

app_name = "skills"

urlpatterns = [
    path("systems/all/", SystemListView.as_view(), name="all_sistemas"),
    path("skills/all/", SkillListView.as_view(), name="all_habilidades"),
    path("positions/all/", FunctionListView.as_view(), name="all_cargos"),
]
