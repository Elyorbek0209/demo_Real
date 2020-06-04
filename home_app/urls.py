from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('about/', views.aboutView, name='about'),
    path('data/', views.getView, name='data'),
]

