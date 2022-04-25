from django.contrib import admin
from .models import ClothInfo, ShopEvent

# Register your models here.

@admin.register(ClothInfo)
class ClothInfoAdmin(admin.ModelAdmin):
    list_display = ('GozLength', 'GiraLength', 'Rate')

@admin.register(ShopEvent)
class ShopEventsAdmin(admin.ModelAdmin):
    list_display = ("তারিখ", "পোশাক", "রেট", "পরিমান", "টাকা")