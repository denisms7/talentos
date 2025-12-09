from django.contrib import admin
from .models import (
    Talent, Skill, SkillType, SkillLevel,
    Category, TalentSkill,
    Certification, SubCategory
)


# -------------------------------
# INLINES
# -------------------------------

class TalentSkillInline(admin.TabularInline):
    model = TalentSkill
    extra = 1
    autocomplete_fields = ["skill"]


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1


# -------------------------------
# MODELOS INDIVIDUAIS
# -------------------------------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [SubCategoryInline]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name", "category__name")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "skill_type")
    list_filter = ("skill_type",)
    search_fields = ("name",)
    ordering = ("name",)


# -------------------------------
# TALENT (PRINCIPAL)
# -------------------------------

@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ("user", "job_title", "department", "created_at")
    search_fields = ("user__first_name", "user__last_name", "user__username", "job_title")
    list_filter = ("categories", "department", "created_at")
    ordering = ("user__first_name",)

    autocomplete_fields = ["user", "categories"]

    inlines = [
        TalentSkillInline,
        CertificationInline,
    ]

    fieldsets = (
        ("Informações do Servidor", {
            "fields": ("user", "job_title", "department")
        }),
        ("Classificações", {
            "fields": ("categories",)
        }),
        ("Datas", {
            "fields": ("created_at",),
        }),
    )

    readonly_fields = ("created_at",)


# -------------------------------
# TALENT ↔ SKILL RELATION
# -------------------------------

@admin.register(TalentSkill)
class TalentSkillAdmin(admin.ModelAdmin):
    list_display = ("talent", "skill", "level")
    list_filter = ("level", "skill__skill_type")
    search_fields = ("talent__user__first_name", "skill__name")
    autocomplete_fields = ["talent", "skill"]


# -------------------------------
# CERTIFICATIONS & EXPERIENCE
# -------------------------------
class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1
    fields = ("name", "institution", "issue_date", "expiration_date", "file", "link")


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "institution", "issue_date", "expiration_date", "talent")
    fields = ("talent", "name", "institution", "issue_date", "expiration_date", "file", "link")
