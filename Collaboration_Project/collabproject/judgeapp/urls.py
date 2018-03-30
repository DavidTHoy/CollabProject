from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
    url(r'^$',views.index, name='judge-home'),
    path('judge-score/', views.score, name='judge-score'),
    path('judge-timeslot/', views.timeslot, name='judge-timeslot'),
    path('judge-timeslot/results', views.results, name='judge-results'),
    path('register', views.register_view, name='judge-register'),
    path('login', views.login_view, name='judge-login'),
    path('logout', views.logout_view, name='judge-logout'),


]