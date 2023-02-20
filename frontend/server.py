from flask import Flask, request, render_template
import requests
import json


app = Flask(__name__)

@app.route("/categories")
def categories():
    r = requests.get(f'http://localhost:2502/categories')
    categories_obj = json.loads(r.text)
    return render_template('categories.html', categories=categories_obj['categories'])

@app.route("/map")
def home():
    category = request.args.get('category')
    r = requests.get(f'http://localhost:2502/conferences?category={category}')
    conferences_obj = json.loads(r.text)
    return render_template('map.html', conferences=conferences_obj['conferences'])

if __name__ == '__main__':
    app.run(debug=True)