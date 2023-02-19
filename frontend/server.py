from flask import Flask, request, render_template
import requests
import json


app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get(f'http://localhost:2502/conferences?category=AI')
    conferences_obj = json.loads(r.text)
    return render_template('map.html', conferences=conferences_obj['conferences'])

if __name__ == '__main__':
    app.run(debug=True)