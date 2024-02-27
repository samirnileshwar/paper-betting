from django.urls import path

from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    #Login
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    #Events
    path('events/<int:pk>/', views.DetailEvent.as_view()),

    #Lines
    path('events/<int:event>/lines/', views.DetailEventLines.as_view()),

    #Returns all open events and the lines to bet on
    path('events/live/lines/', views.DetailEventLiveLines.as_view()),

]