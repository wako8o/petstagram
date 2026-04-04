from petstagram.common import views
from petstagram.urls import path

urlpatterns = [
    path('', views.home_common, name='home common'),
    path('like/<int:photo_id>/', views.like_function, name='like photo'),
    path('share/<int:photo_id>/', views.share_function, name='share photo'),
]