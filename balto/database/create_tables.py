import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = "ted.db"
 
    sql_create_transcripts_table = """ CREATE TABLE IF NOT EXISTS transcripts (
                                        id integer PRIMARY KEY,
                                        url text,
                                        talk text
                                    ); """
 
    sql_create_title_table = """ CREATE TABLE IF NOT EXISTS titles (
                                        id integer PRIMARY KEY,
                                        title text NOT NULL,
                                        url text NOT NULL
                                    ); """
 
    

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create transcripts table
        create_table(conn, sql_create_transcripts_table)
        create_table(conn, sql_create_title_table)

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()