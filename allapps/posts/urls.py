from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:post>/', views.post_detail, name='post_detail'),
]
