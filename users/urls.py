from django.urls import path
from . import views  # Импортируем все представления из views.py

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout, name='logout'),  # Используем logout из views.py
    path('profile/remove_dog/<int:pk>/', views.remove_dog_from_profile, name='remove_dog_from_profile'),
]