from models import Stat
from datetime import datetime, timedelta, date
from database import get_stats
from constructor import constructor

def calculatePoints(stats:Stat):
    totalPoints = 0.0
    totalPoints += stats.goals*3.0
    totalPoints += stats.assists*3.0
    totalPoints += stats.completions*0.1
    totalPoints += stats.callahans*6.0
    totalPoints += stats.blocks*3.0
    totalPoints += stats.throwaways*-1.0

    return totalPoints