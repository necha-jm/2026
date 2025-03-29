from django.contrib import admin
from.models import Loginmodel
# Register your models here.
class adminlogin(admin.ModelAdmin):
    list_display = ("Firstname", "Lastname", "phoneNumber", "username")

admin.site.register(Loginmodel, adminlogin)