from django.contrib import admin
from .models import Source, SourceUsers


# Register your models here.
@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'type']
    search_fields = ['title', 'url', 'type']
    list_filter = ['title', 'url', 'type']


@admin.register(SourceUsers)
class SourceUsersAdmin(admin.ModelAdmin):
    list_display = ['user', 'source', 'message_count']
    search_fields = ['user', 'source', 'message_count']
    list_filter = ['user', 'source', 'message_count']
