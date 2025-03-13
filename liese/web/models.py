from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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
    # Roles are defined in the Role model
    roles = models.ManyToManyField('Role')
    # The admin field is used to determine if the user is an admin
    admin = models.BooleanField()
    # Who created the user
    created_by = models.ForeignKey('self', on_delete=models.CASCADE)
    
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
    
    def __str__(self):
        return self.title