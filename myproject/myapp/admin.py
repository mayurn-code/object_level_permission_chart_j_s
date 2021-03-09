from django.contrib import admin
from. models import Car, Application
from guardian.admin import GuardedModelAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(Car)
class CarModelAdmin(GuardedModelAdmin):
    # list_fields = ['title','brand','model_no']
    list_display = ['title','brand','model_no']
    readonly_fields = ['purchase_date']
    list_filter = ['title','brand']
    search_fields = ['user']
    # filter_vertical = ['title']


@admin.register(Application)
class ApplicationAdmin(GuardedModelAdmin):
    readonly_fields = ['created_at','updated_at']
    fields = ['name','details']

admin.site.site_header= "Things Ally"
admin.site.site_title= "Things Ally"
admin.site.index_title= ""
