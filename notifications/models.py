from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
                return self.message
        
        