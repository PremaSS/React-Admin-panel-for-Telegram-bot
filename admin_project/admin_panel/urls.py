from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('explore/', views.explore, name='explore'),
    path("custom_page/", views.custom_admin_page, name='custom_admin_page'),
]