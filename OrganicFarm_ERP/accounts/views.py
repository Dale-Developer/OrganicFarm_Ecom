# accounts/views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def ajax_login(request):
    """AJAX view for login modal"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Check user role (assuming you have a profile model with role)
            # For now, using is_staff to determine admin
            if user.is_staff:
                redirect_url = '/dashboard/admin/'
            else:
                redirect_url = '/dashboard/customer/'
            
            return JsonResponse({'success': True, 'redirect_url': redirect_url})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid username or password'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def ajax_signup(request):
    """AJAX view for signup modal"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'success': False, 'error': 'Username already exists'})
        
        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'error': 'Email already registered'})
        
        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_staff = False  # Regular customer by default
        user.save()
        
        # Log the user in
        login(request, user)
        
        return JsonResponse({'success': True, 'redirect_url': '/dashboard/customer/'})
    
    return JsonResponse({'success': False, 'error': 'Invalid request'})

def logout_view(request):
    """Logout view"""
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    """User profile view"""
    return render(request, 'accounts/profile.html', {'user': request.user})