from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('favorite/', views.favorite_index, name='index'),
    path('ownstory/', views.ownstory_index, name='index'),
]