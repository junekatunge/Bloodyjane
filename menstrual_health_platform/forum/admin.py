from django.contrib import admin
from .models import Category, Foruma, Post, Comment
# Register your models here.

admin.site.register(Category)
admin.site.register(Foruma)
admin.site.register(Comment)
admin.site.register(Post)