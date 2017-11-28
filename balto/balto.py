import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file
print(app.root_path)
# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'database/ted.db'),
    SECRET_KEY='',
    USERNAME='',
    PASSWORD=''
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    conn = sqlite3.connect(app.config['DATABASE'])
    return conn

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def hello_world():
    db = get_db()
    cur = db.execute('select * from titles order by title asc')
    titles = cur.fetchall()
    return render_template('home.html', titles=titles)

@app.route('/talk/<talk_id>')
def get_talk(talk_id):
    db = get_db()
    cur = db.execute('select * from transcripts left join titles on transcripts.url = titles.url where titles.id=' + talk_id)
    selected = cur.fetchone()
    
    text = selected[2]
    cur = db.execute('select * from titles order by title asc')
    titles = cur.fetchall()
    return render_template('talk.html', selected=selected, titles=titles)