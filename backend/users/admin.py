from django.contrib import admin
from .models import Role, UserProfile, User

admin.site.register(User)


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_roles')
    list_filter = ('roles',)
    search_fields = ('user__username', 'roles__name')

    def get_roles(self, obj):
        return ", ".join([role.name for role in obj.roles.all()])

    get_roles.short_description = 'Roles'


admin.site.register(Role, RoleAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
