from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('/team-assignment/', views.assignment, name='assignment'),
    path('/team-member/', views.members, name='members'),
    path('/team-score/', views.score, name='score'),
    path('/team-topic/', views.topic, name='topic'),

]
