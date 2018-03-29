from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^$',views.index, name='index'),
    path('/judge-score/', views.score, name='score'),
    path('/judge-timeslot/', views.timeslot, name='timeslot'),
    path('/judge-timeslot/results', views.results, name='results'),
    path('/register', views.register_view, name='register'),
    path('/login', views.login_view, name='login'),
    path('/logout', views.logout_view, name='logout'),


]