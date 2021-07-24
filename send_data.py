from contextlib import closing
import mariadb
from secrets import connection_data


def insert_data(weather_data):
    with closing(mariadb.connect(**connection_data)) as connection:
        cursor = connection.cursor()
        insert_command = (
            f"INSERT INTO weather_data ({', '.join(weather_data.keys())}) "
            f"VALUES ({', '.join([str(v) for v in weather_data.values()])})"
        )
        cursor.execute(insert_command)
        connection.commit()