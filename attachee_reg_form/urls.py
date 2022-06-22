from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('admin_panel/', views.query, name='admin'),
    path('home', views.aform, name="form"),
    path('', views.index, name="index"),
    path('csv', views.csvfile, name="csv"),
    path('login', views.logging , name="login"),
    path('register', views.register, name="register"),
    path('logout', views.log_out, name="logout"),
    path('update/<str:pk>', views.updating, name="updating"),
    path('delete/<int:pk>', views.delete, name='delete-data'),
    path('issue_page', views.issues, name="issue"),
    path('issue_table', views.issue_table, name='issue_table')
]