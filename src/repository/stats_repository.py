from repository import persistence

def save(stats):

    stats_list = list(stats.values())

    stats_iter = iter(stats_list)

    # from list to tuple
    list_tuples = [tuple(x) for x in stats_iter]

    connection = persistence.connect()
    cursor = connection.cursor()

    # xºxº
    values = ','.join(
        cursor.mogrify(
            "(%s, TIMESTAMP %s, %s, %s, %s, "
            "%s, %s, %s, %s, %s, "
            "%s, %s, %s, %s, %s, "
            "%s, %s, %s, %s, %s,"
            "%s, %s, %s)",
            tup).decode('utf8') for tup in list_tuples)
    cursor.execute(
        "INSERT INTO Stats VALUES "+ values)
    connection.commit()
    cursor.close()
    connection.close()

