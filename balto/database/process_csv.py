import csv
import sqlite3
from sqlite3 import Error

#todo: init script for building database
def insert_rows_from_csv(type, conn, filename, sql):
    new_rows = []
    with open(filename, "rb") as f:
        reader = csv.reader(f)
        for row in reader:
            if type == "title":
                # 7 name, 15 url
                new_row = (row[7].decode("unicode_escape"), row[15].decode("unicode_escape"),)
            else: # if it's a transcript row
                # 0 transcript, 1 url
                new_row = (row[0].decode("unicode_escape"), row[1].decode("unicode_escape"))
            new_rows.append(new_row)
    cursor = conn.cursor()
    cursor.executemany(sql, new_rows)
    
def main():
    database = "ted.db"
    conn = sqlite3.connect("ted.db")

    insert_talks = """
        INSERT INTO titles (title, url)
        VALUES (?, ?)"""
    talks_file = "./ted-csv/ted_main.csv"
    insert_rows_from_csv("title", conn, talks_file, insert_talks)

    insert_transcripts = """
        INSERT INTO transcripts (talk, url)
        VALUES (?, ?)"""
    transcripts_file = "./ted-csv/transcripts.csv"
    insert_rows_from_csv("transcripts", conn, transcripts_file, insert_transcripts)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

        