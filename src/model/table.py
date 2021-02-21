from dataclasses import dataclass
from model import teamstats


@dataclass
class Table:
    positions: dict() #key: name of the team, value  teamstats
    number_of_teams: int = 20

    def create_first(self, season, date):
        if len(season.teams) == self.number_of_teams:
            for x in season.teams:
                team = teamstats.TeamStats(season.years, date, x)
                self.positions[x] = team

            return self.positions

        else:
            raise Exception("Not enough teams for a table")


