from django.db import models
from django.db.models import Sum


class Team(models.Model):
    name = models.CharField(max_length=200)

    def home_games(self):
        return self.team_home.count()

    def home_scores(self):
        return self.team_home.all().aggregate(Sum('home_score')).get('home_score__sum', 0) or 0

    def away_games(self):
        return self.team_away.count()

    def away_scores(self):
        return self.team_away.all().aggregate(Sum('away_score')).get('away_score__sum', 0) or 0

    def total_scores(self):
        return self.away_scores() + self.home_scores()

    def get_percent(self):
        games = 0
        points = 0
        full = 0
        for game in self.team_home.all():
            full += 3
            games += 1
            if game.home_score > game.away_score:
                points += 3
            elif game.home_score == game.away_score:
                points += 1

        for game in self.team_away.all():
            full += 3
            games += 1
            if game.home_score < game.away_score:
                points += 3
            elif game.home_score == game.away_score:
                points += 1

        if points == 0: return 0
        return (float(points) / full) * 100

    def __str__(self):
        return self.name

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Cup(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    def __str__(self):
        return self.name

class Game(models.Model):
    cup = models.ForeignKey(Cup)
    home = models.ForeignKey(Team, related_name='team_home')
    away = models.ForeignKey(Team, related_name='team_away')
    stadium = models.ForeignKey(Stadium)
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    rodada = models.IntegerField()
    game_num = models.IntegerField()

class Result(models.Model):
    team = models.ForeignKey(Team)
    goals_pro = models.IntegerField()
    goals_con = models.IntegerField()
    points = models.IntegerField()
    goals_sal = models.IntegerField()
    cup = models.ForeignKey(Cup)
    win = models.IntegerField()
    lost = models.IntegerField()
    percent = models.FloatField()
