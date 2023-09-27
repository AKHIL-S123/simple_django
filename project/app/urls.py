from django.contrib import admin
from django.urls import path
from app import views



urlpatterns = [
    path('1',views.home,name='home'),
    path('', views.home, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>', views.student_update, name='student_update'),
    path('delete/<int:pk>', views.student_delete, name='student_delete'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
]

