from django.contrib import admin
from django.urls import path, include
from library.views import inventory_number_management

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    #path('api/', include('myapp.urls')),
]
