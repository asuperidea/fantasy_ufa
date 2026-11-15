from database import add_stats, add_player, add_game, get_stats, add_team
from api import getGames, getStats, getTeams, getPlayers
from models import init_db
from datetime import datetime, timedelta, date

init_db()

def createTeams(season:int):
    teams = getTeams(season)
    for team in teams:
        add_team(team)

def createPlayers(season:int):
    players = getPlayers(season)
    for player in players:
        add_player(player)

def createGames(season:int):
    games = getGames(season)
    for game in games:
        add_game(game)


def constructor(season:int):
    createTeams(season)
    createPlayers(season)
    createGames(season)

constructor(2025)