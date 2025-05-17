from django.urls import path,  re_path

from . import views

urlpatterns = [
    path('api/categories/<str:category_id>/', views.categories_by_parent, name='categories_by_parent'),
    path('explore/', views.explore, name='explore'),
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
]
