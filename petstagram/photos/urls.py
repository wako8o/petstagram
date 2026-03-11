from django.contrib.admin import views
from django.urls import path

urlpatterns = [
    path('photos/', views.photos_log, name='photos'),
]