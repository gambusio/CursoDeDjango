from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.info, name='info'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
