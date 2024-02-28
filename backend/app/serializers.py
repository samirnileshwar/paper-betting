# todos/serializers.py
from rest_framework import serializers
from .models import Event, Line


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','event_key','sport_key','sport_title','home_team','away_team',
                  'start_time','home_team_score','away_team_score','complete')
        model = Event

class LineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','event','line_type','name','price','point','updated')
        model = Line

class EventLinesSerializer(serializers.HyperlinkedModelSerializer):
    line_set = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = [
            'pk',
            'sport_title',
            'start_time',
            'home_team',
            'away_team',
            'line_set'
        ]

    def get_line_set(self, instance):
        lines = instance.line_set.all().order_by('pk')
        return LineSerializer(lines, many=True).data