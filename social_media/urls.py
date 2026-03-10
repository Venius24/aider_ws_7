from django.urls import path
from . import views

urlpatterns = [
    path('', views.social_media_list, name='social_media_list'),
]
