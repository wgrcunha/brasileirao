from django.contrib import admin


from .models import *

class TeamAdmin(admin.ModelAdmin):
    fields = ('name', 'home_games')
    list_display = ('name', 'home_games', 'home_scores', 'away_games', 'away_scores', 'total_scores', 'get_percent')

admin.site.register(Game)
admin.site.register(Team, TeamAdmin)
admin.site.register(Stadium)
