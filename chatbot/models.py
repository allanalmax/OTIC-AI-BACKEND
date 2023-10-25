from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone



# Create your models here.
class FlutterwaveDetails(models.Model):
    pub_key = models.TextField()
    secret_key = models.TextField()
    encryption_key = models.TextField(null=True)
    secret_hash = models.TextField(null=True)
class TransactionsDetails(models.Model):
    trans_id = models.TextField()
    complete = models.BooleanField(default=False)
    number_of_days = models.IntegerField()
    amount = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.TextField()
    course= models.TextField()
    phone_number = models.TextField()
    trial_days = models.IntegerField(default=5)
    subscription_end_date = models.DateTimeField(default=None,null=True)
   
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
    