from django.contrib import admin

from .models import (
    Skill,
    Talent,
    TalentSkill,
    Certification,
)


# ----------------------------------------------------------------------
# INLINES
# ----------------------------------------------------------------------

class TalentSkillInline(admin.TabularInline):
    model = TalentSkill
    extra = 1
    autocomplete_fields = ("skill",)
    fields = ("skill", "level")
    ordering = ("skill__name",)


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1
    fields = (
        "name",
        "institution",
        "issue_date",
        "expiration_date",
        "file",
        "link",
    )


# ----------------------------------------------------------------------
# SKILL
# ----------------------------------------------------------------------

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "skill_type")
    list_filter = ("skill_type",)
    search_fields = ("name",)
    ordering = ("name",)


# ----------------------------------------------------------------------
# TALENT (PRINCIPAL)
# ----------------------------------------------------------------------

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "job_title",
        "department",
        "created_at",
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__username",
        "job_title",
    )
    list_filter = ("department", "created_at")
    ordering = ("user__first_name",)

    autocomplete_fields = ("user",)
    readonly_fields = ("created_at",)

    inlines = (
        TalentSkillInline,
        CertificationInline,
    )

    fieldsets = (
        (
            "Informações do Servidor",
            {
                "fields": (
                    "user",
                    "job_title",
                    "department",
                )
            },
        ),
        (
            "Datas",
            {
                "fields": ("created_at",)
            },
        ),
    )


# ----------------------------------------------------------------------
# TALENT ↔ SKILL (RELAÇÃO)
# ----------------------------------------------------------------------

@admin.register(TalentSkill)
class TalentSkillAdmin(admin.ModelAdmin):
    list_display = ("talent", "skill", "level")
    list_filter = ("level", "skill__skill_type")
    search_fields = (
        "talent__user__first_name",
        "talent__user__last_name",
        "skill__name",
    )
    autocomplete_fields = ("talent", "skill")
    ordering = ("talent__user__first_name", "skill__name")


# ----------------------------------------------------------------------
# CERTIFICATION
# ----------------------------------------------------------------------

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "institution",
        "issue_date",
        "expiration_date",
        "talent",
    )
    list_filter = ("institution", "issue_date", "expiration_date")
    search_fields = (
        "name",
        "institution",
        "talent__user__first_name",
        "talent__user__last_name",
    )
    autocomplete_fields = ("talent",)

    fields = (
        "talent",
        "name",
        "institution",
        "issue_date",
        "expiration_date",
        "file",
        "link",
    )
