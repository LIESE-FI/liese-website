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
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    date_joined = models.DateField()
    active = models.BooleanField()
    # Nullable image field
    image = models.ImageField(upload_to='members/', null=True, blank=True)
    # Roles are defined in the Role model
    roles = models.ManyToManyField('Role')
    # The admin field is used to determine if the user is an admin
    admin = models.BooleanField()
    # Who created the user
    created_by = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    
    # Authentication fields
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    members = models.ManyToManyField('Member')
    
    def __str__(self):
        return self.name
    
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