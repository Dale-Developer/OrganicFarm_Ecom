# dashboard/urls.py
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Dashboard redirect based on role
    path('', views.dashboard_redirect, name='redirect'),
    
    # Admin Dashboard
    path('admin/', views.admin_dashboard, name='admin'),
    path('admin/orders/', views.admin_orders, name='admin_orders'),
    path('admin/orders/queue/', views.order_queue, name='order_queue'),  # New orders queue
    path('admin/orders/out-for-delivery/', views.out_for_delivery, name='out_for_delivery'),
    path('admin/orders/delivered/', views.delivered_orders, name='delivered_orders'),
    path('admin/orders/<int:order_id>/update-status/', views.update_order_status, name='update_order_status'),
    
    # Customer Dashboard
    path('customer/', views.customer_dashboard, name='customer'),
    path('customer/orders/', views.customer_orders, name='customer_orders'),
    path('customer/orders/<int:order_id>/track/', views.track_order, name='track_order'),  # Track order status
    path('customer/orders/<int:order_id>/', views.customer_order_detail, name='customer_order_detail'),
]