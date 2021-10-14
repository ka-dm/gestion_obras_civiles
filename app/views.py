from django.shortcuts import render

def login_view(request):
    return render(request, 'accounts/login.html', {})

def register_view(request):
    return render(request, 'accounts/register.html')

def dashboard_view(request):
    return render(request, 'dashboard/dashboard-base.html')

def index(request):
    return render(request, 'index.html', {})

