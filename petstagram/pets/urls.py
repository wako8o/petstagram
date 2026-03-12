from django.urls import path

from petstagram.pets import views

urlpatterns = [
    path('add/', views.add_pet, name='add pet'),
    path('delete/', views.delete_pet, name='delete pet'),
    path('details/', views.details_pet, name='details pet'),
    path('edit/', views.edit_pet, name='edit pet'),
]