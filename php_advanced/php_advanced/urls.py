"""php_advanced URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import os
from example import views as example_views

urlpatterns = [
    path(r'admin/', admin.site.urls),

    path(r'hello/', example_views.hello_world, name="hello"),
    path(r'hello/<str:name>', example_views.hello_name),
    path(r'hello_template/', example_views.hello_world_template),

    path(r'gift_list_by_func/', example_views.simple_list_view),
    path(r'gift_list_by_class/', example_views.GiftListListView.as_view(),name = 'list_gfl'),

    path(r'gift_list/add/', example_views.PostCreateView.as_view(), name='add_gfl'),
    path(r'gift_list/edit/<int:pk>', example_views.PostEditView.as_view(), name='edit_gfl'),
    path(r'gift_list/delete/<int:pk>', example_views.PostDeleteView.as_view(), name='delete_gfl'),

    path(r'gift/add/', example_views.PostCreateGiftView.as_view()),
    path(r'gift/edit/<int:pk>', example_views.PostEditGiftView.as_view(), name='edit_gf'),
    path(r'gift/delete/<int:pk>', example_views.PostDeleteGiftView.as_view(), name='delete_gf'),
]
