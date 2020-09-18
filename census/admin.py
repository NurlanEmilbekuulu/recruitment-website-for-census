from django.contrib import admin

from census.models import Employee, District, Territory


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


class TerritoryAdmin(admin.TabularInline):
    model = Territory
    extra = 5


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    exclude = ('counter',)
    inlines = [TerritoryAdmin]
    list_filter = ('region',)
