from models import Stat, SessionLocal
from database import add_fantasy_points

def calculatePoints(stats:Stat, session):
    totalPoints = 0.0
    totalPoints += stats.goals*3.0
    totalPoints += stats.assists*3.0
    totalPoints += stats.completions*0.1
    totalPoints += stats.callahans*6.0
    totalPoints += stats.blocks*3.0
    totalPoints += stats.throwaways*-1.0

    totalPoints = round(totalPoints, 2)

    add_fantasy_points(stats.id, totalPoints, session)
    return totalPoints