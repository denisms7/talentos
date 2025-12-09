from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class UserAddView(CreateView):
    template_name = 'accounts/user.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
