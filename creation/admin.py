# accounts/admin.py
from django.contrib import admin
from django.contrib import messages

from .models import AccessRequest
from .services import create_user_from_request


@admin.register(AccessRequest)
class AccessRequestAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'role',
        'status',
        'created_at',
    )
    list_filter = ('status',)
    actions = ('approve_requests',)

    def approve_requests(self, request, queryset):
        for access_request in queryset.filter(status='pending'):
            create_user_from_request(access_request)
            access_request.status = 'approved'
            access_request.save()

        self.message_user(
            request,
            'Solicitações aprovadas com sucesso.',
            messages.SUCCESS,
        )

    approve_requests.short_description = 'Aprovar solicitações selecionadas'
