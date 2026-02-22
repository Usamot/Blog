"""
URL configuration for blog3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingPage, name='HomePageurl'),
    path('user/register', views.RegisterUser, name='RegisterPageUrl'),
    path('user/login', views.LoginUser, name='LoginPageUrl'),
    path('user/logout', views.LogOutUser, name='LogOutUrl'),
    path('addPage/', views.AddPage, name='AddPageurl'),
    path('viewMorePage/<str:pk>/', views.ViewMorePage, name='ViewMorePageurl'),
    path('viewMorePage/<str:pk>/delete', views.DeleteSinglePage, name='deleteSinglePageurl'),
    path('viewMorePage/<str:pk>/edit', views.EditMorePage, name='editSinglePageurl'),
    # path('filterPage/', views.FilterPage, name='filterPageurl'),
    
]
