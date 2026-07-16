"""
URL configuration for hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path ,include
from . import views

urlpatterns = [
    path('load_admin_app/', views.load_admin_app, name='load_admin_app'),
    path('menu/', views.menu_page, name='menu_page'),
    path('book_table/', views.book_table, name='book_table'),
    path('book_table/delete/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_gallery/', views.admin_gallery_list, name='admin_gallery_list'),
    path('admin_gallery/add/', views.admin_gallery_add, name='admin_gallery_add'),
    path('admin_gallery/edit/<int:pk>/', views.admin_gallery_edit, name='admin_gallery_edit'),
    path('admin_gallery/delete/<int:pk>/', views.admin_gallery_delete, name='admin_gallery_delete'),
    path('admin_hero/', views.admin_hero_list, name='admin_hero_list'),
    path('admin_hero/add/', views.admin_hero_add, name='admin_hero_add'),
    path('admin_hero/edit/<int:pk>/', views.admin_hero_edit, name='admin_hero_edit'),
    path('admin_hero/delete/<int:pk>/', views.admin_hero_delete, name='admin_hero_delete'),
    path('admin_news/', views.admin_news_list, name='admin_news_list'),
    path('admin_news/add/', views.admin_news_add, name='admin_news_add'),
    path('admin_news/edit/<int:pk>/', views.admin_news_edit, name='admin_news_edit'),
    path('admin_news/delete/<int:pk>/', views.admin_news_delete, name='admin_news_delete'),

    # MainCategory CRUD
    path('maincategories/', views.maincategory_list, name='maincategory_list'),
    path('maincategories/add/', views.maincategory_add, name='maincategory_add'),
    path('maincategories/edit/<int:pk>/', views.maincategory_edit, name='maincategory_edit'),
    path('maincategories/delete/<int:pk>/', views.maincategory_delete, name='maincategory_delete'),

    # Category CRUD
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/edit/<int:pk>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),
    path('categories/toggle_main/<int:pk>/', views.category_toggle_main, name='category_toggle_main'),

    # # MenuItem CRUD
    # path('menuitems/', views.menuitem_list, name='menuitem_list'),
    # path('menuitems/add/', views.menuitem_add, name='menuitem_add'),
    # path('menuitems/edit/<int:pk>/', views.menuitem_edit, name='menuitem_edit'),
    # path('menuitems/delete/<int:pk>/', views.menuitem_delete, name='menuitem_delete'),
]
