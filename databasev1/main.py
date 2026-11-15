from models import init_db
from datetime import datetime, timedelta, date
from database import get_stats, get_games
from constructor import constructor
from api import getGames, getStats, getTeams, getPlayers
from week import statsByWeek

init_db()

constructor(2025)

statsByWeek("week-5")