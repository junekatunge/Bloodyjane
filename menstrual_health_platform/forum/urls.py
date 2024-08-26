from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_list, name='forum_list'),
    path('<int:forum_id>/', views.forum_detail, name='forum_detail'),
    path('<int:forum_id>/create/', views.post_create, name='post_create'),
    path('<int:post_id>/comment/', views.comment_create, name='comment_create'),
    path('<int:post_id>/', views.post_detail, name='post_detail')
    # Add path for post_detail view if you implement it
]