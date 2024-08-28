from django.urls import path
from . import views

urlpatterns = [
    path('symptom-log/',views.symptom_log, name ='symptom_log'),
    path('symptom-log-success/',views.symptom_log_success, name = 'symptom_log_success')
]
