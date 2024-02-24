from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Event, Line
from .serializers import EventSerializer, LineSerializer


class DetailEvent(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(id=self.kwargs['pk'])

class DetailEventLines(generics.ListAPIView):
    lookup_field = 'event' 
    serializer_class = LineSerializer

    def get_queryset(self):
        return Line.objects.filter(event=self.kwargs['event'])