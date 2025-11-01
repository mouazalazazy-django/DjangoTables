from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:pk>/print/', views.customer_print, name='customer_print'),
    path('customer-row/<int:pk>/edit/', views.customer_row_edit, name='customer_row_edit'),
    path('customer-row/<int:pk>/delete/', views.customer_row_delete, name='customer_row_delete'),
    
    path('craftsmen/', views.craftsman_list, name='craftsman_list'),
    path('craftsmen/<int:pk>/', views.craftsman_detail, name='craftsman_detail'),
    path('craftsman-row/<int:pk>/edit/', views.craftsman_row_edit, name='craftsman_row_edit'),
    path('craftsman-row/<int:pk>/delete/', views.craftsman_row_delete, name='craftsman_row_delete'),
    
    path('workers/', views.worker_list, name='worker_list'),
    path('workers/<int:pk>/', views.worker_detail, name='worker_detail'),
    path('worker-row/<int:pk>/edit/', views.worker_row_edit, name='worker_row_edit'),
    path('worker-row/<int:pk>/delete/', views.worker_row_delete, name='worker_row_delete'),


    path('factory/', views.factory_detail, name='factory_detail'),
    path('factory-row/<int:pk>/edit/', views.factory_row_edit, name='factory_row_edit'),
    path('factory-row/<int:pk>/delete/', views.factory_row_delete, name='factory_row_delete'),

]
