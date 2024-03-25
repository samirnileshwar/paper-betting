from django.contrib import admin
from .models import User, Event, Line, Bet

# Register your models here.
admin.site.register(User)
admin.site.register(Event)
admin.site.register(Line)
admin.site.register(Bet)


