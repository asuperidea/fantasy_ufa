from models import init_db
from datetime import datetime, timedelta, date
from database import get_stats
from constructor import constructor

init_db()
constructor(2025)

def calculatePoints(statId:int):
    