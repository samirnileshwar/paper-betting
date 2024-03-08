from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Event, Line
from .serializers import EventSerializer, LineSerializer, EventLinesSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )
   def get(self, request):
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)
   
class LogoutView(APIView):
     permission_classes = (IsAuthenticated,)
     def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


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
'''    
class DetailMakeBet(generics.APIView):
    permission_classes = ()
    lookup_field = 'event' 
    serializer_class = EventLinesSerializer

    def get_queryset(self):
        return Event.objects.filter(complete=False)
'''
