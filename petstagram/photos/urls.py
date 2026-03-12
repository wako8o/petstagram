from django.urls import path, include

from petstagram.photos import views

urlpatterns = [
    path('add/', views.add_photo, name='add photos'),
    path('', include([
        path('<int:pk>/', views.detail_photo, name='detail photo'),
        path('<int:pk>/edit/', views.edit_photo, name='edit photo'),
    ]))

]