from django.contrib import admin
from .models import User, Specialization, Skill

admin.site.register(User)

@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', )