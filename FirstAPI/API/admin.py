from django.contrib import admin
from API.models import Company, Employee


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "type")


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "position")


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
