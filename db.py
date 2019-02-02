import psycopg2
from config import config


def connect():
    """connection to postgresql db server"""
    conn = None
    try:
        # read connection params
        params = config()

        # connect to postgresql server
        print('Connection to PostgresQL database...')
        conn = psycopg2.connect(**params)

        # create cursor
        cur = conn.cursor()

        # test connection
        print('PostgreSQL database version: ')
        cur.execute('SELECT version()')

        # display db server version
        db_version = cur.fetchone()
        print(db_version)

        # close db connection
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')


if __name__ == '__main__':
    connect()
