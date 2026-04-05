# orders/urls.py
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Order listing with status filters
    path('', views.order_list, name='order_list'),
    path('queue/', views.order_queue, name='queue'),  # New orders (pending)
    path('processing/', views.processing_orders, name='processing'),
    path('out-for-delivery/', views.out_for_delivery, name='out_for_delivery'),
    path('delivered/', views.delivered_orders, name='delivered'),
    path('cancelled/', views.cancelled_orders, name='cancelled'),
    
    # Order management
    path('create/', views.create_order, name='create_order'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('<int:order_id>/update-status/', views.update_order_status, name='update_order_status'),
    path('<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    
    # Order tracking (public)
    path('track/<str:order_number>/', views.track_order_public, name='track_order_public'),
    
    # API for status updates (AJAX)
    path('api/update-status/', views.api_update_status, name='api_update_status'),
]