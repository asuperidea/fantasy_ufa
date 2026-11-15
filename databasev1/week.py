from database import get_games, add_stats
from api import getStats

def statsByWeek(week:str):
    games = get_games(week)
    for game in games:
        stats = getStats(game.id)
        for stat in stats:
            add_stats(stat, game.id, week)