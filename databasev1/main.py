from models import init_db, SessionLocal, Stat
from datetime import datetime, timedelta, date
from database import get_stats, get_games
from constructor import constructor
from api import getGames, getStats, getTeams, getPlayers
from week import statsByWeek
from calculate import calculatePoints
import os
from sqlalchemy import select

db_exists = False
if os.path.isfile("./database.db"):
    db_exists = True

init_db()
with SessionLocal() as session:

    if not db_exists:
        constructor(2025, session)

    statsByWeek("week-5", session)

    stmt = select(Stat).where(Stat.week == "week-5")
    stats = session.scalars(stmt).all()

    for stat in stats:
        print(calculatePoints(stat, session))