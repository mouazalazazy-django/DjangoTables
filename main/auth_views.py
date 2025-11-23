from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from .models import LoginSession


def get_client_ip(request):
    """Get the client's IP address from the request"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def user_login(request):
    """Handle user login and create LoginSession record"""
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Create login session record
            LoginSession.objects.create(
                user=user,
                ip_address=get_client_ip(request),
                session_key=request.session.session_key
            )
            
            messages.success(request, f'مرحباً {user.username}! تم تسجيل الدخول بنجاح')
            return redirect('home')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة المرور غير صحيحة')
    
    return render(request, 'main/login.html')


@login_required
def user_logout(request):
    """Handle user logout and update LoginSession record"""
    # Update the logout time for the most recent login session
    try:
        session = LoginSession.objects.filter(
            user=request.user,
            session_key=request.session.session_key,
            logout_time__isnull=True
        ).latest('login_time')
        session.logout_time = timezone.now()
        session.save()
    except LoginSession.DoesNotExist:
        pass
    
    logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح')
    return redirect('login')


@user_passes_test(lambda u: u.is_superuser)
def user_register(request):
    """Admin-only view to register new users"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        is_staff = request.POST.get('is_staff') == 'on'
        is_superuser = request.POST.get('is_superuser') == 'on'
        
        # Validation
        if not username or not password:
            messages.error(request, 'اسم المستخدم وكلمة المرور مطلوبان')
            return render(request, 'main/register.html')
        
        if password != password_confirm:
            messages.error(request, 'كلمة المرور غير متطابقة')
            return render(request, 'main/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'اسم المستخدم موجود بالفعل')
            return render(request, 'main/register.html')
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        
        messages.success(request, f'تم إنشاء المستخدم {username} بنجاح')
        return redirect('register')
    
    return render(request, 'main/register.html')
