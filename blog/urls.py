# urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name="index"),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>', views.PostUpdate.as_view()),
]