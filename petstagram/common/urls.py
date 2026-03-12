from petstagram.common import views
from petstagram.urls import path

urlpatterns = [
    path('', views.home_common, name='home common'),
]