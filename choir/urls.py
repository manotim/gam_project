from django.urls import path
from .views import singers_list

urlpatterns = [
    path('', singers_list, name='singers_list'),
]
