"""
URL configuration for chemist_backend project.

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
from django.urls import path
from chemist_backend import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicine/', views.product_list),
    path('medicine/<int:id>', views.product_detail),
    path('categories/', views.category_list),
    path('categories/<int:id>', views.category_detail),
    path('sales/', views.sales_list),
    path('expenses/', views.expenses_list),
    path('analysis/', views.category_analysis),
    path('mpesa/', views.mpesa),


]
urlpatterns=format_suffix_patterns(urlpatterns)