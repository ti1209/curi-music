import os

from flask import Flask, render_template
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

client = MongoClient("mongodb address")

db = client['musicDB']
col = db['musiclist']

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/level')
def level():
    return render_template('level.html')


@app.route('/pretest')
def pretest():
    return render_template('pretest.html')


@app.route('/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/playlist')
def playlist():
    try:
        data = col.find()
        return render_template('playlist.html', tasks=data)
    except Exception as e:
        return dumps({'error': str(e)})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
