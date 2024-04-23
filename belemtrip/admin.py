from django.contrib import admin
from .models import *

admin.site.site_header = 'Admin CopNews'
admin.site.site_title = 'Administração'
admin.site.index_title = 'Administração CopNews'

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "active")
    search_fields = ("title", "content")
    list_filter = ("created_at", "active")

@admin.register(TouristSpotCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "active")
    search_fields = ("name",)
    list_filter = ("created_at", "active")
    
@admin.register(RestaurantCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "active")
    search_fields = ("name",)
    list_filter = ("created_at", "active")
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "active")
    search_fields = ("title", "description")
    list_filter = ("date", "active")
    
@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "active")
    search_fields = ("name",)
    list_filter = ("category",)

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "active")
    search_fields = ("name",)

@admin.register(TouristSpot)
class TouristSpotAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "active")
    search_fields = ("name",)
    list_filter = ("category",)