from django.contrib import admin
from .models import Tag_C8738A28CFF7
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Tag_C8738A28CFF7)
class Tag_C8738A28CFF7Admin(admin.ModelAdmin):
        list_display = ['assets','date_time','location','temperature','humidity']
        list_per_page = 100