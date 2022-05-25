from django.urls import path
from . import views



urlpatterns = [
    path('form/', views.aform, name='form'),
    path('query/', views.query, name='query'),
    path('', views.home, name="home"),
    path('csv', views.csvfile, name="csv")
    ]