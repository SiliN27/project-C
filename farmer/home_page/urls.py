from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('login/', views.login_index, name='login_index'),
]