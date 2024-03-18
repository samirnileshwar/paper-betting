from django.shortcuts import render
from .exceptions import LineChangeException
from decimal import Decimal
# Create your views here.
from rest_framework import generics

from .models import Event, Line, Bet
from .serializers import EventSerializer, LineSerializer, BetSerializer
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

class DetailBets(generics.ListCreateAPIView):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = ()

    def get_queryset(self):
        return Bet.objects.all()
    
    def perform_create(self, serializer):

        #Logic to verify that the price and point hasn't changed in the request
        expectedLine= Line.objects.get(event = self.request.data['event_id'], 
                                        line_type = self.request.data['line_type'],
                                        name = self.request.data['team_name'])
                
        #Verify the price all the time
        if float(expectedLine.price) != float(self.request.data['price']):
            raise LineChangeException()
        #Verify the point if spread or total
        if self.request.data['line_type'] in ('spreads', 'totals') and float(expectedLine.point) != float(self.request.data['point']):
            raise LineChangeException()
        
        #toWin
        toWin = float(self.request.data['wager']) * float(expectedLine.price)

        if self.request.data['line_type'] in ('h2h'):
            point = None
        else:
            point = self.request.data['point']
            
        serializer.save(event_id=Event.objects.get(id = self.request.data['event_id']), 
                        line_type=self.request.data['line_type'],
                        team_name=self.request.data['team_name'],
                        wager=self.request.data['wager'],
                        point = point,
                        price = self.request.data['price'],
                        toWin = toWin)
