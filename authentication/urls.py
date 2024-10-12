from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh_session'),
    path('verify/', TokenVerifyView.as_view(), name='verify_session'),
    path('profile/', views.get_profile, name='get_profile')
]