from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('admin-topic/',views.topic, name='topic'),
    path('admin-team/',views.team, name='team'),
    path('admin-timeslot/',views.timeslot, name='timeslot'),
    path('admin-assignment/',views.assignment, name="assignment"),
    path('admin-team/create',views.createTeam, name="createTeam")

]