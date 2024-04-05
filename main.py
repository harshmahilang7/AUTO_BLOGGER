# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   24-03-2024 12:05:16 AM       00:05:16
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 26-03-2024 01:00:26 AM       01:00:26
from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3
import subprocess
import os
import signal

running_process = None

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
    if request.method == 'POST':
        # # Assuming your external script is named 'ext.py'
        # subprocess.Popen(['python', 'ext.py'])  # Replace 'ext.py' with the actual name of your script
        return render_template('app.html')
    else:
        return render_template('app.html')  # Or whatever template you want to render
    
@app.route('/run_external_script', methods=['POST'])
def run_external_script():
    try:
        global running_process
        # Assuming your external script is named 'ext.py'
        running_process = subprocess.Popen(['python', 'ext.py'])  # Replace 'ext.py' with the actual name of your script
        return 'External script execution initiated', 200
    except Exception as e:
        return f'An error occurred: {str(e)}', 500
    

@app.route('/stop_program', methods=['POST'])
def stop_program():
    global running_process
    if running_process is None:
        return 'No program is currently running.'
    try:
        # Terminate the running process
        running_process.terminate()
        running_process = None
        return 'Program stopped successfully!'
    except Exception as e:
        return f'An error occurred: {str(e)}', 500


if __name__ == '__main__':
    app.run(debug=True)
