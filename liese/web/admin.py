from django.contrib import admin
from .models import Article, Member, Role, Project, OpportunityRequest, News, Event

@admin.register(OpportunityRequest)
class OpportunityRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'opportunity_type', 'verified', 'created_at')
    list_filter = ('opportunity_type', 'verified')
    search_fields = ('full_name', 'email')
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'publication_date')  # Fields to display in the list view
    list_filter = ('published', 'publication_date')  # Filter options
    search_fields = ('title', 'author__first_name', 'author__last_name')  # Searchable fields
    ordering = ('-publication_date',)  # Ordering by date (descending)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'category', 'created_by')
    list_filter = ('description', 'location', 'image', 'published', 'created_at')
    search_fields = ('title', 'category', 'created_by')
    ordering = ('-created_at',)

admin.site.register(Member)
admin.site.register(Role)
admin.site.register(Project)
admin.site.register(News)