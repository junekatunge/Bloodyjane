from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SymptomLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    MOOD_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good','Good'),
        ('Neutral','Neutral'),
        ('Bad','Bad')
    ]
    mood = models.CharField(max_length=20,choices=MOOD_CHOICES)  # mood choices replaces charfielld
    
    SLEEP_CHOICES = [
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
        ('Very Poor', 'Very Poor'),
    ]
    sleep = models.CharField(max_length=20, choices= SLEEP_CHOICES)  # Choices (good, poor, etc.)
    other_symptoms = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.date}"