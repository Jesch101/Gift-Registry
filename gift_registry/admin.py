from django.contrib import admin
from gift_registry.models import Group, Gift, Gifter

class GroupAdmin(admin.ModelAdmin):
    model = Group
    list_display = ['event_name', 'event_date', 'pub_date']
    prepopulated_fields = {"slug": ("event_name",)}
    list_filter = ['pub_date']

class GiftAdmin(admin.ModelAdmin):
    model = Gift
    list_display = ['group', 'title', 'reciever' , 'desc', 'url', 'only_one']
    list_filter = ['group']

class GifterAdmin(admin.ModelAdmin):
    model = Gifter
    list_display = ['group','gift',]

admin.site.register(Group, GroupAdmin)
admin.site.register(Gift, GiftAdmin)
