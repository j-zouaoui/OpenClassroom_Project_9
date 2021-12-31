from django.urls import path
from . import views

urlpatterns = [
    path('home/account/', views.account, name='account'),
    ]