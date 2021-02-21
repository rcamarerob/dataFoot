import psycopg2
import logging

logging.basicConfig(level=logging.DEBUG)

def init_database():
    connection = connect()
    with connection.cursor() as cursor:
        cursor.execute(open("./resources/booting_database.sql", "r").read())
        cursor.close()

    connection.commit()
    connection.close()

def save(matches):

    #from set to list
    list_matches = list(matches)
    # from list to tuple
    list_tuples = [tuple(x) for x in list_matches]

    connection = connect()
    cursor = connection.cursor()

    first_tuple = list_tuples[0]
    print("First tuple "+str(first_tuple) + "len "+str(len(first_tuple)))
    values = ','.join(
        cursor.mogrify("(%s, %s, TIMESTAMP %s, %s, %s, %s, %s, %s, %s)", tup).decode('utf8') for tup in
        list_tuples)
    cursor.execute("INSERT INTO Matches(match_id, season_id, match_date, local_team, away_team, half_time_local_team_goals, half_time_away_team_goals, local_team_goals, away_team_goals) VALUES " + values)
    connection.commit()
    cursor.close()
    connection.close()



def execute(query):
    connection = connect()
    cursor = connection.cursor()
    logging.debug("Before calling booting_database")
    result_script = cursor.execute(query)
    logging.debug("result_script "+str(result_script))
    connection.commit()
    cursor.close()
    connection.close()
    return result_script

def connect():
    connection_params = {}
    connection_params['host'] = 'localhost'
    connection_params['database'] = 'datafoot_db'
    connection_params['user'] = 'my_user'
    connection_params['password'] = 'password123'
    return psycopg2.connect(**connection_params)