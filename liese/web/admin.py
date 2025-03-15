from django.contrib import admin
from .models import OpportunityRequest

@admin.register(OpportunityRequest)
class OpportunityRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'opportunity_type', 'verified', 'created_at')
    list_filter = ('opportunity_type', 'verified')
    search_fields = ('full_name', 'email')