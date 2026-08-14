from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('login/', views.loginpage, name='login'),

    path('register/', views.registerpage, name='register'),
    
    path('logout/', views.logoutpage, name='logout'),

    path('room/<str:pk>/', views.room, name='room'),
    
    path('profile/<str:pk>/',views.userprofile,name='user_profile'),

    path('create_room/', views.createRoom, name='create_room'),

    path('update_room/<str:pk>/', views.updateRoom, name='update_room'),

    path('delete_room/<str:pk>/', views.deleteRoom, name='delete_room'),
    
    path('delete-message/<int:pk>/', views.deleteMessage, name='delete_message'),
    
    
]