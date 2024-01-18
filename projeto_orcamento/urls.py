
from django.contrib import admin
from django.urls import path
from app_orcamento import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
]
