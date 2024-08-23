from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.forum_home, name='forum_home'),
    path('', include('machina.urls')),
]