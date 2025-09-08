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

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'email', 'is_leader', 'active', 'date_joined')
    list_filter = ('is_leader', 'active', 'admin', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'position')
    ordering = ('-date_joined',)
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'country')
        }),
        ('Información del Laboratorio', {
            'fields': ('position', 'description', 'date_joined', 'roles', 'is_leader', 'active')
        }),
        ('Enlaces y Media', {
            'fields': ('image', 'linkedin_url'),
            'classes': ('collapse',)
        }),
        ('Configuración Avanzada', {
            'fields': ('admin', 'created_by', 'username', 'password'),
            'classes': ('collapse',)
        }),
    )
    
    filter_horizontal = ('roles',)
    readonly_fields = ('full_name',)
    
    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = 'Nombre Completo'

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name', 'description')
    filter_horizontal = ('members',)
    ordering = ('-start_date',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'publication_date')
    list_filter = ('published', 'publication_date')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    ordering = ('-publication_date',)