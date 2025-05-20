from django.urls import path
from . import views

urlpatterns = [
    path('', views.awal, name='awal'),         # http://127.0.0.1:8000/
    path('home/', views.home, name='home'),    # http://127.0.0.1:8000/home
]
