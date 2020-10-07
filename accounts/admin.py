import csv
import os

from django.contrib import admin
from django.http import HttpResponse

from accounts.models import Profile


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        file = open("credentials.txt", "w")

        for obj in queryset:
            if not obj.user.is_superuser:
                row = f'username : {obj.user.get_username()}, password : {obj.raw_password}'
                file.write(row)
                file.write("\n")

        file.close()

        file = open("credentials.txt", "r", newline='')
        file_content = file.read()
        file.close()
        os.remove("credentials.txt")

        response = HttpResponse(file_content, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename=credentials.txt'

        return response

    export_as_csv.short_description = "Export Selected"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin, ExportCsvMixin):
    change_list_template = "admin/profile_change_list.html"
    actions = ["export_as_csv"]
