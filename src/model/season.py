from dataclasses import dataclass, field
from datetime import datetime
from model import match
from model import teamstats
from typing import Dict

@dataclass
class Season:
    years: str
    matches: Dict[datetime, list] = field(default_factory=lambda: ({}))
    # key= date, value = positions
    tables: Dict[datetime, teamstats.TeamStats] = field(default_factory=lambda: ({}), hash=True)
    #dict = field(default_factory=dict, hash=True)
    teams: set = field(default_factory=set, hash=True)
    is_completed: bool = False

    def add_table(self, date_matches, stats):
        self.tables[date_matches] = stats


    def add_team(self, local_team, away_team):
        self.teams.add(local_team)
        self.teams.add(away_team)


    def add_match(self, match):
        date = match.get_date()
        if date in self.matches:
            previous_matches = self.matches[date]
        else:
            previous_matches = list()

        if previous_matches:
            previous_matches.append(match)
        else:
            previous_matches = [match]

        self.matches[date] = previous_matches
        if len(self.teams) < 20:
            self.add_team(match.__getattribute__('local_team'), match.__getattribute__('away_team'))


    def get_matches(self):
        all_matches = list()

        for sublist in self.matches.values():
            for item in sublist:
                all_matches.append(item)

        return all_matches


    def get_completed(self):
        return self.is_completed

    def set_completed(self, value):
        self.is_completed = value

    def __str__(self):
        return "Year: " + self.years + " match dates ("+str(len(self.matches))+") : "+('[%s]' % ', '.join(map(str, self.matches)))

    def __iter__(self):
        return iter(self)