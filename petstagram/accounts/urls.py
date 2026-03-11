from django.urls import path

from petstagram.accounts import views

urlpatterns = [
    path('accounts/', views.accounts_log, name='accounts'),

]