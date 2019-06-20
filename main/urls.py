from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('activity/', views.activity, name='activity'),
    path('wanted/', views.wanted, name='wanted'),
    path('settings/', views.settings, name='settings'),
    path('system/', views.system, name='system'),
]