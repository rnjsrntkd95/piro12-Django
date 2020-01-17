from django.contrib import admin
from .models import Item

# 방법 1
# admin.site.register(Item)

# 방법 2
# class ItemAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Item, ItemAdmin)


# 방법 3
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'short_desc', 'price', 'is_publish']
    list_display_links = ['title']
    list_filter = ['is_publish', 'updated_at']
    search_fields = ['title']

    def short_desc(self, item):
        item.desc[:20]