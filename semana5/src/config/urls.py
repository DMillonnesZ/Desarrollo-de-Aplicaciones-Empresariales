from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('taller/', include('taller.urls')),
    path('vetcar/', include('vetcar.urls')),
]