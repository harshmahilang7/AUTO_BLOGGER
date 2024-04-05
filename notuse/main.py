# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   24-03-2024 12:05:16 AM       00:05:16
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 24-03-2024 06:23:52 PM       18:23:52
from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3

app = Flask(__name__, template_folder='template')
app.config['DATABASE'] = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DATABASE'])
        db.execute('PRAGMA foreign_keys = ON')  # Enable foreign key support
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        try:
            db = get_db()
            cursor = db.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            db.commit()
            return redirect(url_for('run_program')) 
        except sqlite3.Error as e:
            return f'An error occurred: {str(e)}'
    else:
        return render_template('login.html')

@app.route('/run_program', methods=['POST', 'GET'])
def run_program():
    # Code to run the program
    return render_template('app.html')

@app.route('/stop_program', methods=['POST', 'GET'])
def stop_program():
    # Code to stop the program
    return 'Program stopped successfully!'

if __name__ == '__main__':
    app.run(debug=True)
