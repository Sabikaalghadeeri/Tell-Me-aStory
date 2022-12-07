from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allstories/', views.allstories, name='allstories'),
    path('favorite/', views.favorite_index, name='favorite'),
    path('ownstory/', views.ownstory_index, name='ownstory'),
    path('ownstory/<int:ownstory_id>/', views.ownstory_detail,name='detail'),
    path('ownstory/create/', views.OwnStoryCreate.as_view(), name= 'ownstory_create'),
    path('ownstory/<int:pk>/update/', views.OwnStoryUpdate.as_view(), name= 'ownstory_update'),
    path('ownstory/<int:pk>/delete/', views.OwnStoryDelete.as_view(), name= 'ownstory_delete'),
    path('listen/<str:story_title>/', views.listen, name='listen_story')
]