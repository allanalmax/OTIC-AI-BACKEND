from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.TextField()
    course= models.TextField()
    phone_number = models.TextField()
   
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    whatsapp = models.BooleanField(null=True,default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'

class SchoolDocuments(models.Model):
    name = models.TextField()
    content = models.TextField()
    response = models.ForeignKey(Chat, on_delete=models.CASCADE)

class Document(models.Model):
    
    file = models.FileField(upload_to='documents/')