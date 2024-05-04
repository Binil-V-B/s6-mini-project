from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('video', views.vid, name='index'),
    path('video_feed', views.video_feed, name='video_feed'),
    ]
