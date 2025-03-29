from django.contrib import admin
from.models import foods

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display = ("Food_name", "price")

admin.site.register(foods, FoodAdmin)