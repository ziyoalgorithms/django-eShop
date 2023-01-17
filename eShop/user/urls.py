from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from user import views
from .forms import PwdResetForm, PwdResetConfirmForm

app_name = 'user'


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('activate/<slug:uidb64>/<slug:token>/',
         views.account_activate, name='activate'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('edit/', views.edit_user, name='edit'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='user/password_reset_form.html',
        success_url=reverse_lazy('user:password_reset_done'),
        email_template_name='user/password_reset_email.html',
        form_class=PwdResetForm,
    ), name='pwd_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html',
        success_url=reverse_lazy('user:password_reset_complete'),
        form_class=PwdResetConfirmForm,
    ), name='password_reset_confirm'),
    path('password_reset_email_confirm/', TemplateView.as_view(
        template_name='user/reset_status.html'
    ), name='password_reset_done'),
    path('password_reset_complete/', TemplateView.as_view(
        template_name='user/reset_status.html'
    ), name='password_reset_complete'),
    path('user_delete/', views.user_delete, name='user_delete'),
]
