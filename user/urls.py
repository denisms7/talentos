from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AcessoNegadoView, CustomPasswordResetCompleteView, UsuarioEdit

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # Enviar e-mail
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/password_reset.html'
        ),
        name='password_reset'
    ),

    # E-mail enviado
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/password_reset_sent.html'
        ),
        name='password_reset_done'
    ),

    # Link do e-mail
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='accounts/password_reset_form.html'
        ),
        name='password_reset_confirm'
    ),

    # Finalizado
    path(
        'reset/done/',
        CustomPasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),

    path(
        'access-denied/',
        AcessoNegadoView.as_view(),
        name='acesso-negado'
    ),

    path('password/update/', UsuarioEdit.as_view(), name='alterar_senha'),
]
