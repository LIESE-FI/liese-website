from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import secrets

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name

# Member is a user of the system
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    date_joined = models.DateField()
    active = models.BooleanField(default=True)
    # Nullable image field
    image = models.ImageField(upload_to='members/', null=True, blank=True)
    
    # Nuevos campos para la página de líderes
    description = models.TextField(blank=True, null=True, help_text="Descripción del miembro para mostrar en la página de líderes")
    linkedin_url = models.URLField(blank=True, null=True, help_text="URL del perfil de LinkedIn")
    is_leader = models.BooleanField(default=False, help_text="¿Es un líder de proyecto?")
    position = models.CharField(max_length=100, blank=True, null=True, help_text="Posición/título del miembro")
    
    # Roles are defined in the Role model
    roles = models.ManyToManyField('Role', blank=True)
    # The admin field is used to determine if the user is an admin
    admin = models.BooleanField(default=False)
    # Who created the user
    created_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    # Authentication fields (opcionales ahora)
    username = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @property
    def image_url(self):
        """Retorna la URL de la imagen o una imagen por defecto"""
        if self.image and hasattr(self.image, 'url'):
            try:
                return self.image.url
            except Exception:
                pass
        return '/static/web/images/default-avatar.png'
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    members = models.ManyToManyField('Member')
    # Nuevo campo para imagen del proyecto
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    # Campo para indicar si el proyecto está activo
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def get_image_url(self):
        """Retorna la URL de la imagen del proyecto o una imagen por defecto del espacio"""
        if self.image and hasattr(self.image, 'url'):
            try:
                return self.image.url
            except Exception:
                pass
        return '/static/web/images/default-article-space.png'
    
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.BooleanField()
    publication_date = models.DateField()
    author = models.ForeignKey('Member', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='articles/', null=True, blank=True)
    document = models.FileField(upload_to='articles/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_image_url(self):
        """Retorna la URL de la imagen del artículo o una imagen por defecto del espacio"""
        if self.picture:
            try:
                return self.picture.url
            except Exception:
                pass
        return '/static/web/images/default-article-space.png'
    
    @property
    def image_url(self):
        """Retorna la URL de la imagen del artículo o una imagen por defecto del espacio"""
        if self.picture and hasattr(self.picture, 'url'):
            try:
                return self.picture.url
            except Exception:
                pass
        return '/static/web/images/default-article-space.png'
    
    
class OpportunityRequest(models.Model):
    OPPORTUNITY_TYPES = [
        ('investigacion', 'Investigación'),
        ('tesis', 'Tesis'),
        ('maestria', 'Programas de Maestría'),
        ('servicio', 'Servicio Social'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    opportunity_type = models.CharField(max_length=50, choices=OPPORTUNITY_TYPES, null=True)
    verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    verification_token_expires = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_verification_token(self):
        self.verification_token = secrets.token_urlsafe(32)
        self.verification_token_expires = timezone.now() + timedelta(hours=24)
        self.save()


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.BooleanField()
    publication_date = models.DateField()
    author = models.ForeignKey('Member', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    CATEGORY_CHOICES = [
        ('conferencia', 'Conferencia'),
        ('taller', 'Taller'),
        ('reunion', 'Reunión'),
        ('otros', 'Otros'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('Member', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['start_date']

    
    def get_image_url(self):
        """Retorna la URL de la imagen del evento o una imagen por defecto"""
        if self.image:
            return self.image.url if self.image else '/media/events/images.png'
        return '/media/events/images.png'