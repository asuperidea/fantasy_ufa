import requests
from datetime import datetime, timedelta, date


def apiGames(date:str):
    response = requests.get(f"https://www.backend.ufastats.com/api/v1/games?date={date}")
    data = response.json()
    print("api.py :: apiGames Called")
    return data

def apiStats(gameId:str):
    response = requests.get(f"https://www.backend.ufastats.com/api/v1/playerGameStats?gameID={gameId}")
    data = response.json()
    print("api.py :: apiStats Called")
    return data

def apiTeams(season:int):
    response = requests.get(f"https://www.backend.ufastats.com/api/v1/teams?years={season}")
    data = response.json()
    print("api.py :: apiTeams Called")
    return data

def apiPlayers(season:int):
    response = requests.get(f"https://www.backend.ufastats.com/api/v1/players?years={season}")
    data = response.json()
    print("api.py :: apiPlayers Called")
    return data

# Data Collectors

def getGames(day:date):
    games = []   
    data = apiGames(day)["data"]
    if not data:
        pass
    for game in data:
        games.append(game)
    return games

def getStats(gameId:str):
    data = apiStats(gameId)["data"] 
    if not data:
        return None
    return data

def getTeams(season:int):
    data = apiTeams(season)["data"]
    if not data:
        return None
    return data

def getPlayers(season:int):
    data = apiPlayers(season)["data"]
    if not data:
        return None
    return data