import logging
from repository import persistence

def save(odds):

    #from set to list
    # from list to tuple
    flat_odds_list = [item for sublist in odds for item in sublist]
    list_tuples = [tuple(x) for x in flat_odds_list]

    connection = persistence.connect()
    cursor = connection.cursor()

    values = ','.join(
        cursor.mogrify("(%s, %s, %s, %s, %s)", tup).decode('utf8') for tup in
        list_tuples)
    cursor.execute("INSERT INTO Odds (match_id, bet_house, home_winner, draw, away_winner) VALUES " + values)
    connection.commit()
    cursor.close()
    connection.close()
