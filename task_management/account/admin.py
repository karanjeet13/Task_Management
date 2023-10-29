from django.contrib import admin
from account.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "user_type"]

admin.site.register(Employee, EmployeeAdmin)
