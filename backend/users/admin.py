from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

# Register your models here.

class ManageruserUser(UserAdmin):
    model = Users

    list_display = ('email', 'is_teacher', 'is_student', 'is_active', 'is_superuser', 'is_staff')
    # list_filter = ('is_superuser', 'is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ( 'name',)}),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser',),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    # filter_horizontal = ()

admin.site.register(Users, ManageruserUser)