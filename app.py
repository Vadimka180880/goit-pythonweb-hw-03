from flask import Flask, request, render_template, redirect, url_for, abort
import json
from datetime import datetime
import os

app = Flask(__name__)
DATA_FILE = os.path.join('storage', 'data.json')


def save_message(username, message):
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
    except:
        data = {}

    timestamp = str(datetime.now())
    data[timestamp] = {'username': username, 'message': message}

    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)


def load_messages():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except:
        return {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('message')
        save_message(username, message)
        return redirect(url_for('index'))
    return render_template('message.html')

@app.route('/read')
def read():
    messages = load_messages()
    return render_template('read.html', messages=messages)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(port=3000, debug=True)

