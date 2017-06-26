from django.core.management.base import BaseCommand, CommandError
from brasileirao.models import *
import fileinput
import datetime
import os
from HTMLParser import HTMLParser

from unicodedata import normalize


def get_create_generic(model, value):
    try:
        return model.objects.get(name=value)
    except model.DoesNotExist:
        m = model()
        m.name = value
        m.save()
        return m

def get_cup(year):
    try:
        return Cup.objects.get(year=int(year))
    except Cup.DoesNotExist:
        m = Cup()
        m.year = int(year)
        m.name = "Brasileirao"
        m.save()
        return m

def create_update_game(cup, home, away, stadium, home_score, away_score, date, rodada, game_num):
    try:
        g = Game.objects.get(cup=cup, game_num=game_num)
    except Game.DoesNotExist:
        g = Game()
        g.cup = cup
        g.game_num = game_num

    g.home = home
    g.away = away
    g.stadium = stadium
    g.home_score = int(home_score)
    g.away_score = int(away_score)
    g.date = date
    g.rodada = rodada
    g.save()

class MyHTMLParser(HTMLParser):

    current = []

    def __init__(self, year):
        self.cup = get_cup(year)
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.current = []
            self.current.append(tag)

    def handle_endtag(self, tag):
        if tag == 'tr':
            if len(self.current) == 8:
                #['tr', '380', '38', '02/12/2012 - 17:00', 'Atl\xc3\xa9tico - GO', '0 x 1', 'Bahia - BA', 'Serra Dourada - Goiania - GO
                _, game_num, rodada, date, home, score, away, stadium = self.current
                home = get_create_generic(Team, normalize('NFKD', home.decode('utf-8')).encode('ASCII','ignore'))
                away = get_create_generic(Team, normalize('NFKD', away.decode('utf-8')).encode('ASCII','ignore'))
                stadium = get_create_generic(Stadium, stadium)
                home_score, _, away_score = score.split()
                date = datetime.datetime.strptime(date, '%d/%m/%Y - %H:%M')
                create_update_game(self.cup, home, away, stadium, home_score, away_score, date, rodada, game_num)
            self.current = []

    def handle_data(self, data):
        data = data.strip()
        if data:
            self.current.append(data)

class Command(BaseCommand):
    help = 'Parse html'

    def add_arguments(self, parser):
       parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
       filename = options['filename']
       year = os.path.basename(filename)
       parser = MyHTMLParser(year)
       parser.feed(open(filename).read())
