from django.urls import path
from . import views

urlpatterns = [
    # Cambia 'home/' por ''
    path('', views.home, name='home'),
    path('detail_book/<int:id>/', views.detail_book, name='detail_book'),
]