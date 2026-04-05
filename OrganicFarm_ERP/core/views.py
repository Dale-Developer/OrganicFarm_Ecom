from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
  return render(request, 'core/index.html')

def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
      login(request, user)
      return redirect('dashboard')
    else:
      messages.error(request, 'Invalid username or password')
      return redirect('index')
    
def signup(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    
    if password != confirm_password:
      messages.error(request, 'Passwords do not match')
      return redirect('index')
    
    if User.objects.filter(username=username).exists():
      messages.error(request, 'Username already exists')
      return redirect('index')
    
    if User.objects.filter(email=email).exists():
      messages.error(request, 'Email already registered')
      return redirect('index')
    
    user = User.objects.create_user(username=username, email=email, password=password)
    login(request, user)
    return redirect('dashboard')


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required

# def index(request):
#     """Landing page with login and signup forms"""
#     if request.user.is_authenticated:
#         # Redirect to appropriate dashboard based on role
#         if request.user.is_staff:
#             return redirect('dashboard:admin')
#         else:
#             return redirect('dashboard:customer')
    
#     return render(request, 'core/index.html')

# def login_view(request):
#     """Handle login form submission"""
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Check if input is email
#         if '@' in username:
#             try:
#                 user_obj = User.objects.get(email=username)
#                 username = user_obj.username
#             except User.DoesNotExist:
#                 messages.error(request, 'No account found with this email.')
#                 return redirect('core:index')
        
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             messages.success(request, f'Welcome back, {user.get_full_name() or user.username}!')
            
#             # Redirect based on role
#             if user.is_staff:
#                 return redirect('dashboard:admin')
#             else:
#                 return redirect('dashboard:customer')
#         else:
#             messages.error(request, 'Invalid username or password.')
#             return redirect('core:index')
    
#     return redirect('core:index')

# def signup_view(request):
#     """Handle signup form submission"""
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')
        
#         # Validation
#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match.')
#             return redirect('core:index')
        
#         if len(password) < 8:
#             messages.error(request, 'Password must be at least 8 characters long.')
#             return redirect('core:index')
        
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists. Please choose another.')
#             return redirect('core:index')
        
#         if User.objects.filter(email=email).exists():
#             messages.error(request, 'Email already registered. Please login or use another email.')
#             return redirect('core:index')
        
#         # Create user
#         try:
#             user = User.objects.create_user(
#                 username=username,
#                 email=email,
#                 password=password
#             )
            
#             # Auto-login after signup
#             login(request, user)
#             messages.success(request, f'Account created successfully! Welcome {username}!')
            
#             # Redirect to customer dashboard
#             return redirect('dashboard:customer')
            
#         except Exception as e:
#             messages.error(request, 'An error occurred. Please try again.')
#             return redirect('core:index')
    
#     return redirect('core:index')

# def logout_view(request):
#     """Handle logout"""
#     logout(request)
#     messages.info(request, 'You have been successfully logged out.')
#     return redirect('core:index')