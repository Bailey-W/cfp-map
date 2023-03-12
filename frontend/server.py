from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route("/categories")
def categories():
    r = requests.get(f'http://localhost:2502/categories')
    categories_obj = json.loads(r.text)
    print(categories_obj)
    capitalized_categories = []
    for cat in categories_obj['categories']:
        capitalized_categories.append(cat.capitalize())
    return render_template('categories.html', categories=capitalized_categories)

@app.route("/map")
def home():
    category = request.args.get('category')
    r = requests.get(f'http://localhost:2502/conferences?category={category}')
    conferences_obj = json.loads(r.text)
    return render_template('map.html', conferences=conferences_obj['conferences'], category=category.capitalize())

@app.route("/home")
@app.route("/")
def oops():
    return render_template('home.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()