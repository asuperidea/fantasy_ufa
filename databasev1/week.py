from database import get_games, add_stats
from api import getStats
from calculate import calculatePoints

def statsByWeek(week:str, session):
    games = get_games(week, session)
    for game in games:
        stats = getStats(game.id)
        for stat in stats:
            add_stats(stat, game.id, week, session)
