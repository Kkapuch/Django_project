
from django.contrib import admin
from django.urls import path
from hello import views


urlpatterns = [
    path('', views.index, name='home'),
    path('content_1', views.content_1, name='content_1'),
    path('content_2', views.content_2, name='content_2'),
]
