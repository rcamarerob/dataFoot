from model.odd import Odd
from model.odd_enum import OddEnum
from model.odd_headers import OddHeaders


def has_bet(row, bet):
    try:
        return getattr(row, bet.home_csv_header)
    except:
        return "ERROR_CODE"


def read_odds(match_id, row):

    odds = []
    for dictOddEnum in OddEnum.__dict__:
        if isinstance(OddEnum.__dict__.get(dictOddEnum), OddHeaders):
            betname = dictOddEnum
            bet = OddEnum.__dict__.get(dictOddEnum)
            if has_bet(row, bet) == 'ERROR_CODE':
                print("no tiene apuesta de ", bet)
            else:
                odd = Odd(match_id, betname, getattr(row, bet.home_csv_header), getattr(row, bet.draw_csv_header), getattr(row, bet.away_csv_header))
                odds.append(odd)
                print("has bet ", odd)

    return odds