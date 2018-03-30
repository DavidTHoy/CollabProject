from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='team-menu'),
    path('team-assignment/', views.assignment, name='team-assignment'),
    path('team-member/', views.members, name='team-members'),
    path('team-score/', views.score, name='team-score'),
    path('team-topic/', views.topic, name='team-topic'),

]
