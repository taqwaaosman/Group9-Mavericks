"""
URL configuration for MavericksProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import login_view
from .views import index
from .views import home
from .views import registration
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('registration/', registration, name='registration'),
]

