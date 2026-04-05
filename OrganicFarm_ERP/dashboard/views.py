# dashboard/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def dashboard_redirect(request):
    """Redirect to appropriate dashboard based on user role"""
    if request.user.is_staff:
        return redirect('dashboard:admin')
    else:
        return redirect('dashboard:customer')

@login_required
@staff_member_required
def admin_dashboard(request):
    """Admin dashboard view"""
    return render(request, 'dashboard/admin_dashboard.html')

@login_required
def customer_dashboard(request):
    """Customer dashboard view"""
    return render(request, 'dashboard/customer_dashboard.html')