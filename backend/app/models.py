from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=20, decimal_places=2, default = 0)

class Event(models.Model):
    event_key = models.CharField(max_length=50, unique=True)
    sport_key = models.CharField(max_length=50)
    sport_title = models.CharField(max_length=50)
    home_team = models.CharField(max_length=50)
    away_team = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    home_team_score = models.IntegerField(null=True)
    away_team_score = models.IntegerField(null=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.away_team + ' vs ' + self.home_team 

class Line(models.Model):

    class LineTypes(models.TextChoices):
        H2H = 'h2h'
        SPREADS = 'spreads'
        TOTALS = 'totals'

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    line_type = models.CharField(max_length = 10, choices = LineTypes.choices)
    name = models.CharField(max_length=50, null = True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    point = models.DecimalField(max_digits=10, decimal_places=1, null = True)
    updated = models.DateTimeField()

class Bet(models.Model):

    class LineTypes(models.TextChoices):
        H2H = 'h2h'
        SPREADS = 'spreads'
        TOTALS = 'totals'

    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    line_type = models.CharField(max_length = 10, choices = LineTypes.choices)
    team_name = models.CharField(max_length=50, null = True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    point = models.DecimalField(max_digits=10, decimal_places=1, null = True)
    wager = models.DecimalField(max_digits=10, decimal_places=1, null = True)
    toWin = models.DecimalField(max_digits=10, decimal_places=1, null = True)
    settled = models.BooleanField(null=True, default=False)
