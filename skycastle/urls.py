"""skycastle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views
from accounts import views as accounts_views

urlpatterns = [
        path('', views.Main, name='main'),
        path('admin/', admin.site.urls),
        path('login/', accounts_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('signup/', TemplateView.as_view(template_name='accounts/signup_select.html'), name='signup'),
        path('signup/coordinator/', accounts_views.CoordinatorSignupView.as_view(), name='coordinator_signup'),
        path('signup/coordinator/add_info/', accounts_views.AddCoordiInfoView.as_view(), name='addinfo_coordi'),
        path('signup/parent/', accounts_views.ParentSignupView.as_view(), name='parent_signup'),
        path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
        path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
        path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
		path('api/check_id/', accounts_views.check_id, name='check_id'),
		path('signup/coordinator/add_info/add_certificate', accounts_views.add_certificate.as_view(), name='add_certificate'),
]
