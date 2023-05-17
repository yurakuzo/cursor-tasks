from django.contrib import admin
from .models import MenuItem, SliderItem


@admin.register(SliderItem)
class SliderItemAdmin(admin.ModelAdmin):
    list_display = ["title", "link"]


admin.site.register(MenuItem)
...
