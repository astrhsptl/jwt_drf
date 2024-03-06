from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'username', 'email']
    list_editable = []
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'avatar', 'is_active', 'is_staff', 'is_superuser')
        }),
    )


admin.site.register(User, UserAdmin)