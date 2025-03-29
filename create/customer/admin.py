from django.contrib import admin
from .models import Profile
admin.site.register(Profile)
from django.contrib import admin
from .models import Order, Location

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'item', 'status', 'created_at')  # Columns displayed
    search_fields = ('customer__username', 'item')  # Searchable fields
    list_filter = ('status', 'created_at')  # Filters in sidebar

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'latitude', 'longitude', 'timestamp')
    search_fields = ('customer__username',)
