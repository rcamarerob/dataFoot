import pandas as pd
import logging
from model import season
from model import match
from model import matchstats
from odds import odd_reader
from repository import persistence
from repository import season_repository
from repository import odd_repository

import table_generator

logging.basicConfig(level=logging.DEBUG)

firstSeason = "00-01"
lastSeason = "21-22"
previousSeasonTeams = set()
teams_by_season = 20


def nextSeasonYear(currentYear):
    if (currentYear < 9):
        return "0" + str(currentYear + 1)
    else:
        return str(currentYear + 1)


def add_match(current_season, current_match):
    current_season.add_match(current_match)


def main():
    persistence.init_database()
    current_season_years = firstSeason

    while current_season_years != lastSeason:
        season_years = current_season_years.split("-")

        current_season = season.Season(current_season_years, dict(), dict(), set(), False)
        season_id = str(season_years[0]) + "-" + str(season_years[1])
        season_repository.save_season(season_id, str(season_years[0]), str(season_years[1]), teams_by_season)

        if season_repository.is_season_completed(season_id):
            logging.info("Season " + season_id + " is already completed")

        else:

            csv_url = 'https://www.football-data.co.uk/mmz4281/' + str(season_years[0]) + str(
                season_years[1]) + '/SP1.csv'
            logging.debug("Calling %s", csv_url)
            # newSeason
            try:
                season_data = pd.read_csv(csv_url)
            except:
                columns = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'B365H',
                           'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'GBH', 'GBD', 'GBA', 'IWH', 'IWD', 'IWA', 'LBH',
                           'LBD', 'LBA', 'SBH', 'SBD', 'SBA', 'WHH', 'WHD', 'WHA', 'GB>2.5', 'GB<2.5', 'B365>2.5',
                           'B365<2.5', 'GBAHH', 'GBAHA', 'GBAH', 'LBAHH', 'LBAHA', 'LBAH', 'B365AHH', 'B365AHA',
                           'B365AH']
                season_data = pd.read_csv(csv_url, usecols=columns)

            all_odds = []
            for row in season_data.itertuples():
                current_match = match.Match(season_id, row.Date, row.HomeTeam, row.AwayTeam, str(row.HTHG),
                                            str(row.HTAG), str(row.FTHG), str(row.FTAG))

                try:
                    match_stats = matchstats.MatchStats(current_match, row.HS, row.AS, row.HST, row.AST, row.HHW,
                                                        row.AHW, row.HC, row.AC, row.HF, row.AF, row.HO, row.AO, row.HR,
                                                        row.AR, row.HR, row.AY)
                    print("Match stats ", match_stats)
                except:
                    print("No Match stats found")

                add_match(current_season, current_match)
                all_odds.append(odd_reader.read_odds(current_match.get_id(), row))

            persistence.save(current_season.get_matches())
            odd_repository.save(all_odds)
            table_generator.generate_table(current_season)
            if (len(current_season.get_matches()) == (teams_by_season / 2) * ((teams_by_season - 1) * 2)):
                current_season.set_completed(True)
                season_repository.season_completed(season_id)

            logging.info("Season " + current_season.years + " is completed: " + str(current_season.is_completed))

        nextYear = nextSeasonYear(int(season_years[1]))
        current_season_years = str(season_years[1]) + "-" + nextYear
        logging.info("Season %s", current_season)


if __name__ == '__main__':
    main()
