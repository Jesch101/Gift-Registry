from django.contrib import admin
from gift_registry.models import Group

class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ['event_name', 'event_date', 'pub_date']
    prepopulated_fields = {"slug": ("event_name",)}
    list_filter = ['pub_date']

admin.site.register(Group, GroupAdmin)