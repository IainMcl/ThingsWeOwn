#!/var/www/ThingsWeOwn/ThingsWeOwn/venv/bin/ python3
from flask import Flask
from flask_assistant import Assistant, ask
import json

app = Flask(__name__)
assist = Assistant(app, project_id="things-we-own-51334")
change = 5


@app.route('/test')
def home():
    return json.dumps({"Did this work": "Yes"}), 200, {'Content-Type': 'josn', 'Google-Assistant-Version': 'v2'}


@assist.action("/")
def hello_world():
    speech = "Microphone check 1, 2 what is this?"
    return ask(speech), 200, {'Content-Type': 'application/json',
                              'Google-Assistant-API-Version': 'v2'}


if __name__ == "__main__":
    app.run(debug=True)
