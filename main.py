# You definitely (or maybe) want to modularize this file into several files to improve readability.
# I only use one file for simplicity.

import os
import sqlite3
from flask import Flask, g, jsonify

'''
DATABASE
'''

# Define the sqlite3 database file. It is safe to delete this file to reinitialize db.
DATABASE = './database.db'

# Setting static_url_path to blank allows us to serve index.html from the root URL.
app = Flask(__name__, static_url_path='')

# Use sqlite3 as the database engine for simplicity.
def connect_db():
    return sqlite3.connect(DATABASE)

# Retrieves a database connection.
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_db()
    return db

# Initialize tables inside the db according to schema.sql.
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Performs SELECT queries on the database.
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Performs INSERT queries on the database.
def insert_db(query, args=()):
    db = get_db()
    db.cursor().execute(query, args)
    db.commit()

# Database teardown/cleanup.
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

'''
APPLICATION
'''

# Example REST API endpoint. Will insert a new record then queries the table.
@app.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    # Insert new record to the table.
    insert_db('INSERT INTO tasks (name, owner) VALUES (?, ?)', ['Finish this hackathon!', 'Sammy'])

    # Query the table.
    tasks = query_db('SELECT * FROM tasks')

    # Return JSON array of the rows.
    # TODO: The result still does not include table fields. Anyone know which library to use? The data got inserted though.
    return jsonify(tasks=tasks)

# Handles static files request from inside the static direcory.
@app.route('/static/<path:path>', methods=['GET'])
def serve_static_files(path):
    return app.send_from_directory('static', path)

# Handles index.
@app.route('/', methods=['GET'])
def serve_index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    init_db() # WILL INITIALIZE (DROP) THE DB IN EVERY SERVER RESTARTS. Remove if not desired.
    app.run(debug=True)
