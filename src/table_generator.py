from model import table
from repository import stats_repository
import datetime

def generate_table(current_season):

    matches = current_season.__getattribute__('matches')
    match_dates = list(matches.keys())
    match_dates.sort()
    first_table = table.Table(dict())
    first_date = match_dates[0] - datetime.timedelta(days=1)
    first_stats = first_table.create_first(current_season, first_date)#
    #current_season.add_table(first_date, first_table)
    previous_stats = first_stats
    for date in match_dates:
        date_matches = matches[date]
        stats = generate_stats(date, date_matches, previous_stats)
        #persist stats
        stats_repository.save(stats)
        current_season.add_table(date, stats)
        previous_stats = stats


def cmp_team_stats(stat):
    return stat.points*10000 + 100*(stat.goals_favour-stat.goals_against) + stat.goals_favour + 0.1*stat.goals_against


def calculate_positions(all_teams_stats):
    #previous_stats from key (name) -> key(position)
    sorted_stats = sorted(all_teams_stats.values(), key=cmp_team_stats, reverse=True)
    first_pos = 1
    for stat in sorted_stats:
        stat.position = first_pos
        first_pos = first_pos+1


def update_previous_stats(previous_stats, date):
    new_date_previous_stats = previous_stats
    for team_name in new_date_previous_stats:
        new_date_previous_stats[team_name].stats_date = date

    return new_date_previous_stats

def generate_stats(date, matches,  previous_stats):
    all_teams_stats = update_previous_stats(previous_stats, date)
    for match in matches:
        local_stats = update_team(match, match.local_team, previous_stats[match.local_team])
        all_teams_stats[match.local_team] = local_stats
        away_stats = update_team(match, match.away_team, previous_stats[match.away_team])
        all_teams_stats[match.away_team] = away_stats

    calculate_positions(all_teams_stats)
    print("all_teams_stats ts ", all_teams_stats)

    return all_teams_stats


def update_team(match, team, previous_stats):
    ts = previous_stats
    ts.games_played = ts.games_played + 1
    if match.is_local(team):
        ts.games_played_home = ts.games_played_home + 1
        ts.goals_favour_home = ts.goals_favour_home + int(match.local_team_goals)
        ts.goals_against_home = ts.goals_against_home + int(match.away_team_goals)
        if match.wins(team):
            ts.games_won_home = ts.games_won_home + 1
            ts.points = ts.points + 3
        elif match.drawn():
            ts.games_drawn_home = ts.games_drawn_home + 1
            ts.points = ts.points + 1
        else:
            ts.games_lost_home = ts.games_lost_home + 1
    else:
        ts.games_played_away = ts.games_played_away + 1
        ts.goals_favour_away = ts.goals_favour_away + int(match.away_team_goals)
        ts.goals_against_away = ts.goals_against_away + int(match.local_team_goals)
        if match.wins(team):
            ts.games_won_away = ts.games_won_away + 1
            ts.points = ts.points + 3
        elif match.drawn():
            ts.games_drawn_away = ts.games_drawn_away + 1
            ts.points = ts.points + 1
        else:
            ts.games_lost_away = ts.games_lost_away + 1

    ts.goals_favour = ts.goals_favour_home + ts.goals_favour_away
    ts.goals_against = ts.goals_against_home + ts.goals_against_away
    ts.games_won = ts.games_won_home + ts.games_won_away
    ts.games_drawn = ts.games_drawn_home + ts.games_drawn_away
    ts.games_lost = ts.games_lost_home + ts.games_lost_away

    return ts




