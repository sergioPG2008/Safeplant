from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def creadores_view(request):
    return render(request, 'creadores.html')

def principal_view(request):
    return render(request, 'principal.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def navbar_view(request):
    return render(request, 'navbar.html')