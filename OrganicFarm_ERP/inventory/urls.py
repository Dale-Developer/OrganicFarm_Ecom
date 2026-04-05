# inventory/urls.py
from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    # Product management
    path('', views.product_list, name='product_list'),
    path('products/', views.product_management, name='product_management'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    
    # Stock management
    path('stock/', views.stock_management, name='stock_management'),
    path('stock/low/', views.low_stock_alert, name='low_stock'),
    path('stock/<int:product_id>/adjust/', views.adjust_stock, name='adjust_stock'),
    
    # Harvest records (for agricultural/raw products)
    path('harvest/', views.harvest_records, name='harvest_records'),
    path('harvest/add/', views.add_harvest_record, name='add_harvest_record'),
    path('harvest/<int:record_id>/edit/', views.edit_harvest_record, name='edit_harvest_record'),
    path('harvest/<int:record_id>/delete/', views.delete_harvest_record, name='delete_harvest_record'),
    
    # Categories
    path('categories/', views.category_management, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/<int:category_id>/edit/', views.edit_category, name='edit_category'),
    
    # Reports
    path('reports/', views.inventory_reports, name='reports'),
]