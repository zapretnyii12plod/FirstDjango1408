"""
URL configuration for FirstDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# from MainApp import views
from DjangoCountries import views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
#    path('', views.root, name='root'),
#    path('about', views.about, name='about'),
#    path('item/<int:id>', views.item, name='item'),
#    path('items', views.items, name='items')
    path('', views.root, name='root'),
    path('countries-list/<int:p>', views.countries_list, name='countries-list'),
    path('country/<int:id>', views.country, name='country'),
    path('countries_by_letter/<str:letter>', views.countries_by_letter, name='countries_by_letter'),
    path('languages-list', views.languages_list, name='languages-list'),
    path('language/<int:id>', views.language, name='language'),
]
