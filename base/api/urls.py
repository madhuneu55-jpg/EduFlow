from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes),
    path('rooms/',views.getRooms),
    path('rooms/<str:pk>/',views.getRoom),
    path('users/',views.getUser),
    path('messages/',views.getMessages),
    path('room/create/',views.createRoom),
    path('room/update/',views.updateRoom),
    path('room/delete/',views.deleteRoom),
    path('register/', views.registerUser),
    path('login/', views.loginUser),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]