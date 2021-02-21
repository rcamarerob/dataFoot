from dataclasses import dataclass
import datetime


@dataclass
class TeamStats:
    _season_id: str
    _stats_date: datetime
    _team: str
    _points: int = 0
    _position: int = -1
    _games_played: int = 0
    _games_won: int = 0
    _games_drawn: int = 0
    _games_lost: int = 0
    _goals_favour: int = 0
    _goals_against: int = 0
    _games_played_home: int = 0
    _games_won_home: int = 0
    _games_drawn_home: int = 0
    _games_lost_home: int = 0
    _goals_favour_home: int = 0
    _goals_against_home: int = 0
    _games_played_away: int = 0
    _games_won_away: int = 0
    _games_drawn_away: int = 0
    _games_lost_away: int = 0
    _goals_favour_away: int = 0
    _goals_against_away: int = 0


    ## GETTERS
    @property
    def games_played(self) -> int:
        return self._games_played

    @property
    def points(self) -> int:
        return self._points

    @property
    def position(self) -> int:
        return self._position

    @property
    def games_won(self) -> int:
        return self._games_won

    @property
    def games_drawn(self) -> int:
        return self._games_drawn

    @property
    def games_lost(self) -> int:
        return self._games_lost

    @property
    def goals_favour(self) -> int:
        return self._goals_favour

    @property
    def goals_against(self) -> int:
        return self._goals_against

    @property
    def games_played_home(self) -> int:
        return self._games_played_home

    @property
    def games_won_home(self) -> int:
        return self._games_won_home

    @property
    def games_drawn_home(self) -> int:
        return self._games_drawn_home

    @property
    def games_lost_home(self) -> int:
        return self._games_lost_home

    @property
    def goals_favour_home(self) -> int:
        return self._goals_favour_home

    @property
    def goals_against_home(self) -> int:
        return self._goals_against_home

    @property
    def games_played_away(self) -> int:
        return self._games_played_away

    @property
    def games_won_away(self) -> int:
        return self._games_won_away

    @property
    def games_drawn_away(self) -> int:
        return self._games_drawn_away

    @property
    def games_lost_away(self) -> int:
        return self._games_lost_away


    @property
    def goals_favour_away(self) -> int:
        return self._goals_favour_away


    @property
    def goals_against_away(self) -> int:
        return self._goals_against_away


    @property
    def team(self) -> str:
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

    @property
    def season_id(self) -> str:
        return self._season_id

    @season_id.setter
    def season_id(self, value):
        self._season_id = value

    @property
    def stats_date(self) -> datetime:
        return self._stats_date


    @stats_date.setter
    def stats_date(self, value):
        self._stats_date = value


    @points.setter
    def points(self, value):
        self._points = value


    @position.setter
    def position(self, value):
        self._position = value

    @games_played.setter
    def games_played(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_played = value

    @games_won.setter
    def games_won(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_won = value

    @games_drawn.setter
    def games_drawn(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_drawn = value

    @games_lost.setter
    def games_lost(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_lost = value

    @goals_favour.setter
    def goals_favour(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._goals_favour = value

    @goals_against.setter
    def goals_against(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._goals_against = value

    @games_played_home.setter
    def games_played_home(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_played_home = value

    @games_won_home.setter
    def games_won_home(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_won_home = value

    @games_drawn_home.setter
    def games_drawn_home(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_drawn_home = value

    @games_lost_home.setter
    def games_lost_home(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_lost_home = value

    @goals_favour_home.setter
    def goals_favour_home(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._goals_favour_home = value

    @goals_against_home.setter
    def goals_against_home(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._goals_against_home = value


    @games_played_away.setter
    def games_played_away(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_played_away = value


    @games_won_away.setter
    def games_won_away(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_won_away = value

    @games_drawn_away.setter
    def games_drawn_away(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_drawn_away = value

    @games_lost_away.setter
    def games_lost_away(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._games_lost_away = value

    @goals_favour_away.setter
    def goals_favour_away(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._goals_favour_away = value

    @goals_against_away.setter
    def goals_against_away(self, value):
        if value < 0:
            raise ValueError("Sorry you value is below eligibility criteria")
        self._goals_against_away = value

    def __hash__(self) -> int:
        return super().__hash__()


    def __iter__(self):
        return iter(vars(self).values())


