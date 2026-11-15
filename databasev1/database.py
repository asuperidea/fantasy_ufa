from models import Player, Game, Stat, Team, init_db
from sqlalchemy import select, exists
from datetime import date

def add_stats(data:dict, gameID:str, week:str, session):
    player = session.get(Player, data["player"]["playerID"])
    if player is None:
        raise Exception("Player Dosn't Exist")

    game = session.get(Game, gameID)
    if game is None:
        raise Exception("Game dosn't exist!")

    new = Stat(
        playerId = data["player"]["playerID"],
        gameId = gameID,
        week = week,

        goals = data["goals"],
        assists = data["assists"],
        completions = data["completions"],
        throwaways = data["throwaways"],
        callahans = data["callahans"],
        blocks = data["blocks"],

        secondsPlayed = data["secondsPlayed"],
        oPointsPlayed = data["oPointsPlayed"],
        dPointsPlayed = data["dPointsPlayed"],
        oPointsScored = data["oPointsScored"],
        dPointsScored = data["dPointsScored"],
    )

    session.add(new)
    session.commit()


def add_player(data:dict, session):
    team = session.get(Team, data["teams"][0]["teamID"])
    existing = session.get(Player, data["playerID"])
    if team is None:
        raise Exception("Team dosn't exist!")
    if existing:
        return False
    
    name = data["firstName"]+" "+data["lastName"]
    new = Player(name = name,
        id = data["playerID"],
        jerseyNumber = data["teams"][0]["jerseyNumber"],
        teamId = data["teams"][0]["teamID"] 
    )
    session.add(new)
    session.commit()

def add_game(data:dict, session):
    if session.get(Game, data["gameID"]):
        return False
    new = Game(
        id = data["gameID"],
        final = data["status"] == "Final",
        week = data["week"],
        homeTeamId = data["homeTeamID"],
        awayTeamId = data["awayTeamID"],
        homeScore = data["homeScore"],
        awayScore = data["awayScore"],
    )
    session.add(new)
    session.commit()

def add_team(data:dict, session):
    if session.get(Team, data["teamID"]):
        return False
    new = Team(
        id = data["teamID"],
        name = data["fullName"],
        abbrev = data["abbrev"],
        year = data["year"],
        division = data["division"]["divisionID"],
        wins = data["wins"],
        losses = data["losses"],
        ties = data["ties"],
    )
    session.add(new)
    session.commit()
 


def get_stats(playerId:str, session):
    stats = []
    player = session.get(Player, playerId)
    for stat in player.stats:
        stats.append(stat)
    return stats

def get_stat_by_id(statId:str, session):
    stats = {}
    stat = session.get(Stat, statId)
    return stats

def get_players(playerId:str, teamId=None, session=None):
    if playerId:
        player = session.get(Player, playerId)
        return player

    if teamId:
        players=[]    
        team = session.get(Team, teamId)
        for player in team.player:
            return players

def get_games(week:str, session):
    stmt = select(Game).filter_by(week=week)
    return session.scalars(stmt).all()