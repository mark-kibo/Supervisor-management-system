from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('form/', views.aform, name='form'),
    path('admin_panel/', views.query, name='admin'),
    path('', views.home, name="home"),
    path('csv', views.csvfile, name="csv"),
    path('login', views.logging , name="login"),
    path('register', views.register, name="register"),
    path('logout', views.log_out, name="logout"),
    path('update/<str:pk>', views.updating, name="updating"),
    path('delete/<int:pk>', views.delete, name='delete-data'),
    ]