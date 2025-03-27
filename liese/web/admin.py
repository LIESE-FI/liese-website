from django.contrib import admin
from .models import Article, Member, Role, Project, OpportunityRequest, News

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

admin.site.register(Member)
admin.site.register(Role)
admin.site.register(Project)
admin.site.register(News)