from django.db import models
# from machina.core.models import AbstractForum, AbstractTopic, AbstractPost
from machina.apps import forum
 
class MyForum(apps.forum):
    description = models.TextField()