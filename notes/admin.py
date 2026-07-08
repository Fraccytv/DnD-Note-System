from django.contrib import admin
from .models import Campaign, Note

# Register your models here.


class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by")
    search_fields = ("name", "created_by")


admin.site.register(Campaign, CampaignAdmin)

class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "campaign", "created_by", "visibility")
    search_fields = ("title", "campaign__name", "created_by__username")
    
admin.site.register(Note, NoteAdmin)