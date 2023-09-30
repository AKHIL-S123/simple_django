from django.contrib import admin
from django.urls import path
from app import views
from django.conf.urls import handler403
from app.views import custom_permission_denied

handler403 = custom_permission_denied




urlpatterns = [
    path('', views.home, name='student_list'),
    path('error/', views.custom_permission_denied,name='error'),
    path('create/', views.student_create, name='student_create'),
    path('update/<int:pk>', views.student_update, name='student_update'),
    path('delete/<int:pk>', views.student_delete, name='student_delete'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
]

