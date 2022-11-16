from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import *

urlpatterns = [
    path('', UserListView.as_view(), name='all_users'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail_users'),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('<int:pk>/delete/', UserDeleteView.as_view()),

    # Аутентификация
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
