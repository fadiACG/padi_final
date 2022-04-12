"""padi_final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
                  path('', views.index, name="index"),
                  path('properties', views.properties, name="properties"),
                  path('about', views.about, name="about"),
                  path('contact', views.contact, name="contact"),
                  path('dashboard', views.dashboardView, name="dashboard"),
                  path('login', LoginView.as_view(), name="login_url"),
                  path('register', views.registerView, name="register_url"),
                  path('logout', LogoutView.as_view(next_page='dashboard'), name="logout"),
                  path('base', views.edit_profile, name="base"),
                  path('view_profile', views.edit_profile, name="view_profile"),
                  path('edit_profile', views.edit_profile, name="edit_profile"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
