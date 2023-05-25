from django.urls import path, include
from . import views

app_name='inout'

urlpatterns = [
    #path('',index),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]