"""
URL configuration for django_netology project.

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

from django.contrib import admin
from django.urls import path,register_converter
from main.views import home_view,time_view,workdir_view,hello,sum,DateConverter, user_report
from main.views import pagi,cookbook
register_converter(DateConverter, 'date')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('current_time/', time_view, name='time'),
    path('workdir/', workdir_view, name='workdir'),
    path ('hello/', hello, name='hello'),
    path('sum/<int:a>/<int:b>/', sum, name='sum'),
    path('users/<int:id>/reports/<date:dt>/', user_report, name='user_report'),
    path ('pagi/', pagi, name='pagi'),
    path('<str:dish>/', cookbook, name='cookbook')
]
