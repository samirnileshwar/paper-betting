from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    #Login
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    #Events
    path('event/<int:pk>/', views.DetailEvent.as_view()),

    #Lines
    path('event/<int:event>/lines/', views.DetailEventLines.as_view()),
]