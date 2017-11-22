import requests
import time
import re
from bs4 import BeautifulSoup
import sqlite3

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

def main():
    database = "../../ted.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        talkstxt="talks.txt"
        talks=open(talkstxt, 'r')

        for talk in talks:        
            # create the ted talk url 
            talkclean = re.sub("\n","", talk)
            transcript="https://www.ted.com" + talkclean + "/transcript?language=en"
            print(transcript)

            # get the contents of the ted talk
            # note: cannot get the transcript without 
            # a library to interact with the TED React app
            result = requests.get(transcript)
            content = result.content

            # parse the website content
            soup = BeautifulSoup(content, "html.parser")
            # todo: process the transcript
            time.sleep(1.5)
        talks.close()


if __name__ == '__main__':
    main()