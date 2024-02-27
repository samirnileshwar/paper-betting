from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Event, Line
from .serializers import EventSerializer, LineSerializer, EventLinesSerializer
from rest_framework.permissions import IsAuthenticated


class DetailEvent(generics.ListAPIView):
    permission_classes = (  )
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(id=self.kwargs['pk'])

class DetailEventLines(generics.ListAPIView):
    permission_classes = ()
    lookup_field = 'event' 
    serializer_class = LineSerializer

    def get_queryset(self):
        return Line.objects.filter(event=self.kwargs['event'])

class DetailEventLiveLines(generics.ListAPIView):
    permission_classes = ()
    lookup_field = 'event' 
    serializer_class = EventLinesSerializer

    def get_queryset(self):
        return Event.objects.filter(complete=False)