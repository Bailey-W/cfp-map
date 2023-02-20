from flask import Flask, request
import mysql.connector

app = Flask(__name__)

# establish connection to local MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="admin",
    database="cfp-map"
)

cur = db.cursor()

@app.route("/conferences", methods=['GET'])
def conferences():
    category = request.args.get('category')
    conference_list = []
    cur.execute('SELECT * FROM categories_conferences INNER JOIN conferences ON categories_conferences.conference=conferences.conf_name WHERE category=%s', (category, ))
    for conf in cur.fetchall():
        conference_obj = {'name': conf[1], 
                          'link': conf[6],
                          'location': conf[3],
                          'lat': conf[4],
                          'lng': conf[5],
                          'deadline': conf[7],
                          'category': category}
        conference_list.append(conference_obj)
    return {'conferences': conference_list}

@app.route("/categories", methods=['GET'])
def categories():
    cur.execute('SELECT category_name FROM categories')
    category_list = []
    for category in cur.fetchall():
        category_list.append(category[0])
    return {'categories': category_list}

if __name__ == '__main__':
    # app.run(debug=True, port=2502)
    app.run(port=2502)