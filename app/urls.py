from django.urls import path

from . import views

urlpatterns = [
    #Events
    path('event/<int:pk>/', views.DetailEvent.as_view()),

    #Lines
    path('event/<int:event>/lines/', views.DetailEventLines.as_view()),
]