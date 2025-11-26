from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal_view, name='principal'), # Ruta raíz
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('navbar/', views.navbar_view, name='navbar'),
    path('creadores/', views.creadores_view, name='creadores'),
]