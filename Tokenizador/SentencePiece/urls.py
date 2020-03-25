from django.urls import path
from . import views

urlpatterns = [
    path('', views.catch_index),
    path('form/', views.catch_form, name="form"),
]