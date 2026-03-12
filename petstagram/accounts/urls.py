from django.urls import path, include

from petstagram.accounts import views

urlpatterns = [
    path('login/', views.log_accounts, name='login'),
    path('register/', views.register_accounts, name='register'),
    path('profile/<int:pk>/', include([
        path('', views.details_accounts, name='details accounts'),
        path('edit/', views.edit_accounts, name='edit accounts'),
        path('delete/', views.delete_accounts, name='delete accounts'),
    ]))


]