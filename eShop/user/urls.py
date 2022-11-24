from django.urls import path

from user import views

app_name = 'user'


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.account_activate, name='activate')
]
