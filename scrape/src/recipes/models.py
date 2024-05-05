from django.db import models
from django.utils import timezone
from phone_field import PhoneField

    
class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.author
