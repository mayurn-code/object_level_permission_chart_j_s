from django.contrib import admin
from .models import Customer
from guardian.admin import GuardedModelAdmin
# from django.contrib.auth.models import User

@admin.register(Customer)
class CustomerModelAdmin(GuardedModelAdmin):
    list_display = ['id','name','address','mobile']

# @admin.register(User)
# class UserModelAdmin(GuardedModelAdmin):
#     list_display = ['id','name','address','mobile']