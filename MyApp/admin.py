from django.contrib import admin

# Register your models here.

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("user_name", "email")
    search_fields = ("user_name", "email")


admin.site.register(Employee, EmployeeAdmin)
