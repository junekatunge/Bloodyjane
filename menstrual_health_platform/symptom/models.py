from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SymptomLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    mood = models.CharField(max_length=20)  # You can use choices here
    sleep = models.CharField(max_length=20)  # Choices (good, poor, etc.)
    other_symptoms = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"