from django.urls import path

from like import views


app_name = 'like'

urlpatterns = [
    path('', views.like_main, name="like_main"),
    path('add/', views.like_add, name="like_add"),
    path('delete/', views.like_delete, name='like_delete'),
    path('clear/', views.like_clear, name='like_clear')
]
