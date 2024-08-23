from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=[
        ('menstrual_cycle', 'Menstrual Cycle'),
        ('period_problems', 'Period Problems'),
        ('menstrual_health', 'Menstrual Health'),
        ('other', 'Other'),
    ], default='menstrual_cycle')


    def __str__(self):
        return self.title
