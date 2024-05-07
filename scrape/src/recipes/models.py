from django.db import models
from django.utils import timezone
    

class Recipe(models.Model):
    title = models.CharField(max_length=255, null=False)
    ratings_count = models.CharField(max_length=255, null=False)
    description = models.TextField()
    prep_time = models.CharField(max_length=255, null=False)
    difficulty = models.CharField(max_length=255, null=False)
    url = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title
    
