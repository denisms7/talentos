from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    ListView,
    TemplateView,
)

from .models import Profile, ProfileSkill, Certification, Skill
from .forms import (
    ProfileForm,
    ProfileSkillForm,
    CertificationForm,
)







class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profiles/profile_form.html"
    success_url = reverse_lazy("profiles:detail")

    def get_object(self):
        return self.request.user.profile


