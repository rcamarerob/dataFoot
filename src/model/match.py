import datetime
import uuid


class Match:
    def __init__(self, season_id, date, local_team, away_team, half_time_local_goals, half_time_away_goals,
                 local_team_goals, away_team_goals):
        self.id = str(uuid.uuid4())
        self.season_id = season_id
        self.date = datetime.datetime.strptime(Match.formatting(date), "%d/%m/%YT%H:%M:%S-%Z")
        self.local_team = local_team
        self.away_team = away_team
        self.half_time_local_goals = half_time_local_goals
        self.half_time_away_goals = half_time_away_goals
        self.local_team_goals = local_team_goals
        self.away_team_goals = away_team_goals

    @staticmethod
    def formatting(str_date):
        if len(str_date) < 10:
            date_components = str_date.split("/")
            return date_components[0] + "/" + date_components[1] + "/20" + date_components[2] + "T00:00:00-UTC"
        elif len(str_date) == 10:
            return str_date + "T00:00:00-UTC"
        else:
            return str_date

    def get_id(self):
        return self.id

    def get_date(self):
        return self.date

    def is_local(self, team):
        return team == self.local_team

    def wins(self, team):

        if self.drawn():
            return False

        if team == self.local_team:
            return self.local_team_goals > self.away_team_goals
        else:
            return self.local_team_goals < self.away_team_goals

    def drawn(self):
        return self.local_team_goals == self.away_team_goals

    def __iter__(self):
        return iter(vars(self).values())
