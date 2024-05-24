from django.urls import path, include
from .views import inventory_number_management, get_inventory_number_list, add_inventory_number, \
    check_inventory_number_exists, test

urlpatterns = [
    path('inventory_number_management/<int:pk>/', inventory_number_management, name='inventory_number_management'),
    path('get_inventory_number_list/<int:book_id>/', get_inventory_number_list, name='get_inventory_number_list'),
    path('add_inventory_numbers_multiple/<int:book_id>/', add_inventory_number, name='add_inventory_number'),
    path('check_inventory_numbers_exists_multiple/', check_inventory_number_exists, name='check_inventory_numbers_exists_multiple'),
    path('test/', test, name='test'),
]

