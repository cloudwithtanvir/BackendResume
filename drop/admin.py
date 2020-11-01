from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Drop

admin.site.site_header = 'TagLog Official'


class DropAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email', 'phone_number','tech_expert','position', 'heard','upload','created_at']
    # ordering = ['email']
    search_fields = ['name', 'email', 'phone_number','tech_expert','heard']


admin.site.register(Drop, DropAdmin)
admin.site.unregister(Group)
