# accounts/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # Authentication (these will work with your modal forms)
    path('login/', views.ajax_login, name='login'),  # AJAX login for modal
    path('signup/', views.ajax_signup, name='signup'),  # AJAX signup for modal
    path('logout/', views.logout_view, name='logout'),
    
    # Password reset (if needed)
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    
    # Profile
    path('profile/', views.profile, name='profile'),
]