from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def home(request):
    context = {
        'ai_result': 00,
    }
    return render(request, 'home.html', context)
