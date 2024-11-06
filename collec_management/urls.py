"""
URL configuration for cc project.

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
from collec_management import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about/', views.about, name='about'),
    path('collection/<int:id>/', views.collection_detail, name='collection_detail'),
    path('all/', views.collection_list, name='collection_list'),
    path('new/', views.add_collection, name='add_collection'), 
    path('delete/<int:id>/', views.delete_collection, name='delete_collection'),
    path('change/<int:id>/', views.edit_collection,name='edit_collection'),
]
