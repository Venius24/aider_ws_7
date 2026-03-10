from django.urls import path
from . import views

urlpatterns = [
    path('', views.loyalty_list, name='loyalty_list'),
]
