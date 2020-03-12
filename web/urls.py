from django.urls import path
from . import views


urlpatterns = [
    path('', views.site_list, name='site_list'),
    path('site/<int:pk>/', views.site_detail, name='site_detail'),
    path('site/new/', views.site_new, name='site_new'),
    path('site/<int:pk>/edit/', views.site_edit, name='site_edit'),
]
