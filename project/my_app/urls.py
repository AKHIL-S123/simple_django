from django.contrib import admin
from django.urls import path
from my_app import views



urlpatterns = [
    path('b/',views.home,name='home'),
    path('create_group/', views.create_group, name='create_group'),
    path('list_groups/', views.list_groups, name='list_groups'),
    
]