from database import add_player, add_game, add_team
from api import getGames, getTeams, getPlayers

def createTeams(season:int, session):
    teams = getTeams(season)
    for team in teams:
        add_team(team, session)

def createPlayers(season:int, session):
    players = getPlayers(season)
    for player in players:
        add_player(player, session)

def createGames(season:int, session):
    games = getGames(season)
    for game in games:
        add_game(game, session)


def constructor(season:int, session):
    createTeams(season, session)
    createPlayers(season, session)
    createGames(season, session)