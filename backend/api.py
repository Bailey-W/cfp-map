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
def home():
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

if __name__ == '__main__':
    app.run(debug=True, port=2502)