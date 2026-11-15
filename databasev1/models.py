from sqlalchemy import String, create_engine, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, relationship

engine = create_engine("sqlite:///database.db", echo=False)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

class Player(Base):
    __tablename__ = "players"

    id: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    teamId: Mapped[str] = mapped_column(ForeignKey("teams.id"))
    jerseyNumber: Mapped[str] = mapped_column(nullable=True)

    stats: Mapped[list["Stat"]] = relationship(back_populates="player")
    team: Mapped["Team"] = relationship(back_populates="players")


class Game(Base):
    __tablename__ = "games"

    id: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    final: Mapped[bool] = mapped_column(nullable=False, default=False)
    week: Mapped[str] = mapped_column(nullable=False)

    homeTeamId: Mapped[str] = mapped_column(ForeignKey("teams.id"))
    awayTeamId: Mapped[str] = mapped_column(ForeignKey("teams.id"))
    homeScore: Mapped[int] = mapped_column(nullable=False)
    awayScore: Mapped[int] = mapped_column(nullable=False)

    stats: Mapped[list["Stat"]] = relationship(back_populates="game")

    homeTeam: Mapped["Team"] = relationship(foreign_keys=[homeTeamId], back_populates="homeGames")
    awayTeam: Mapped["Team"] = relationship(foreign_keys=[awayTeamId], back_populates="awayGames")


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[str] = mapped_column(nullable=False, primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    abbrev: Mapped[str] = mapped_column(nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    division: Mapped[str] = mapped_column(nullable=False)

    wins: Mapped[int] = mapped_column(default=0)
    losses: Mapped[int] = mapped_column(default=0)
    ties: Mapped[int] = mapped_column(default=0)

    homeGames: Mapped[list["Game"]] = relationship(foreign_keys=[Game.homeTeamId], back_populates="homeTeam")
    awayGames: Mapped[list["Game"]] = relationship(foreign_keys=[Game.awayTeamId], back_populates="awayTeam")

    players: Mapped[list["Player"]] = relationship(back_populates="team")
    

class Stat(Base):
    __tablename__ = "stats"

    id: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    playerId: Mapped[str] = mapped_column(ForeignKey("players.id"))
    gameId: Mapped[str] = mapped_column(ForeignKey("games.id"))
    week: Mapped[str] = mapped_column(nullable=False)

    fantasyPoints: Mapped[float] = mapped_column(nullable=True)

    goals: Mapped[int] = mapped_column(default=0)
    assists: Mapped[int] = mapped_column(default=0)
    completions: Mapped[int] = mapped_column(default=0)
    throwaways: Mapped[int] = mapped_column(default=0)
    callahans: Mapped[int] = mapped_column(default=0)
    blocks: Mapped[int] = mapped_column(default=0)

    oPointsPlayed: Mapped[int] = mapped_column(default=0)
    dPointsPlayed: Mapped[int] = mapped_column(default=0)
    secondsPlayed: Mapped[int] = mapped_column(default=0)
    oPointsScored: Mapped[int] = mapped_column(default=0)
    dPointsScored: Mapped[int] = mapped_column(default=0)

    player: Mapped["Player"] = relationship(back_populates="stats")
    game: Mapped["Game"] = relationship(back_populates="stats")

def init_db():
  Base.metadata.create_all(engine)