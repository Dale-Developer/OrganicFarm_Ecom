# finance/urls.py
from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    # Dashboard
    path('', views.finance_dashboard, name='dashboard'),
    
    # Sales management
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/<int:sale_id>/', views.sale_detail, name='sale_detail'),
    path('sales/daily/', views.daily_sales, name='daily_sales'),
    path('sales/weekly/', views.weekly_sales, name='weekly_sales'),
    path('sales/monthly/', views.monthly_sales, name='monthly_sales'),
    
    # Expenses management
    path('expenses/', views.expenses_list, name='expenses_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/categories/', views.expense_categories, name='expense_categories'),
    path('expenses/<int:expense_id>/edit/', views.edit_expense, name='edit_expense'),
    path('expenses/<int:expense_id>/delete/', views.delete_expense, name='delete_expense'),
    
    # Reports & Analytics
    path('reports/', views.financial_reports, name='reports'),
    path('reports/profit-loss/', views.profit_loss_report, name='profit_loss'),
    path('reports/export/', views.export_financial_data, name='export'),
    
    # API for charts (AJAX)
    path('api/chart-data/', views.chart_data, name='chart_data'),
]