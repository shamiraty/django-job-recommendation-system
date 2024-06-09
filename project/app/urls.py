from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import ProfileView


urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', views.apply_for_job, name='apply_for_job'),

    path('register/', views.register, name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),

     path('profile/', ProfileView.as_view(), name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
]
