from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    #Login
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('home/', views.HomeView.as_view(), name ='home'),
    path('logout/', views.LogoutView.as_view(), name ='logout'),

    #Events
    path('events/<int:pk>/', views.DetailEvent.as_view()),

    #Lines
    path('events/<int:event>/lines/', views.DetailEventLines.as_view()),

    #Returns all open events and the lines to bet on
    path('events/live/lines/', views.DetailEventLines.as_view()),

    #Bets
    path('bet/', views.Bets.as_view())
]