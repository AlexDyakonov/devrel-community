from django.contrib import admin
from .models import ReffLink


# Register your models here.
@admin.register(ReffLink)
class ReffLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'count', 'id']
    search_fields = ['name', 'link']
    list_filter = ['name', 'count']
