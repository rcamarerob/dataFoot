import logging
from repository import persistence

logging.basicConfig(level=logging.DEBUG)

def save_season(id, season_start_year, season_end_years, teams_by_season):
    sql = "INSERT INTO Season VALUES ('" +id+"',"+ season_start_year +", "+season_end_years+","+ str(teams_by_season)+", FALSE);"
    persistence.execute(sql)

def season_completed(season_id):
    persistence.execute("UPDATE season SET completed = TRUE WHERE id = '"+season_id+"';")

def is_season_completed(season_id):
    connection = persistence.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT completed FROM season WHERE id = '" + season_id + "';")
    raw_return = cursor.fetchall()
    for x in raw_return:
        retorno = x[0]
    cursor.close()
    connection.close()
    return retorno
