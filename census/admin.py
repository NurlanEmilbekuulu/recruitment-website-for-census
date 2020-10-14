from django.contrib import admin

from census.models import Employee, District, Territory, SiteSettings


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    exclude = ('agreement',)
    # def has_add_permission(self, request, obj=None):
    #     return Employee.objects.all().count() == 0


class TerritoryAdmin(admin.TabularInline):
    model = Territory
    extra = 5


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    exclude = ('counter',)
    inlines = [TerritoryAdmin]
    list_filter = ('region',)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    # def __init__(self, model, admin_site):
    #     super().__init__(model, admin_site)
    #     try:
    #         # SiteSettings.load().save()
    #     except ProgrammingError:
    #         pass

    def has_add_permission(self, request, obj=None):
        return SiteSettings.objects.all().count() == 0

    def has_delete_permission(self, request, obj=None):
        return False
