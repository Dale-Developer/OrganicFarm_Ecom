# settings_app/urls.py
from django.urls import path
from . import views

app_name = 'settings_app'

urlpatterns = [
    path('', views.settings_dashboard, name='dashboard'),
    
    # General settings
    path('general/', views.general_settings, name='general'),
    
    # Business settings
    path('business/', views.business_settings, name='business'),
    path('shipping/', views.shipping_settings, name='shipping'),
    path('payment/', views.payment_settings, name='payment'),
    
    # Notification settings
    path('notifications/', views.notification_settings, name='notifications'),
    
    # User management (admin only)
    path('users/', views.user_management, name='users'),
    path('users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('users/<int:user_id>/toggle-role/', views.toggle_user_role, name='toggle_user_role'),
]