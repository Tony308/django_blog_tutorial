from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('', views.home, name='blog-home'),
]