import mysql.connector
from datetime import datetime

# establish connection to local MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="admin",
    database="cfp-map"
)

cur = db.cursor()

# Adds a conference to the database
# If it already exists, updates entry instead
# Also adds the corresponding category and relation if necessary
def add_conference_safely(conference):
    # checks if conference already exists in database
    cur.execute("SELECT * FROM conferences WHERE conf_name=%s", ( conference['name'] ,))
    if(cur.fetchone() != None):
        # If conference already exists, update its information
        cur.execute("UPDATE conferences SET location=%s, lat=%s, lng=%s, link=%s, deadline=%s WHERE conf_name=%s", (conference['location'], conference['lat'], conference['lng'], conference['link'], conference['deadline'], conference['name']))
    else:
        cur.execute("INSERT INTO conferences VALUES (%s, %s, %s, %s, %s, %s)", (conference['name'], conference['location'], conference['lat'], conference['lng'], conference['link'], conference['deadline']))

    cur.execute("SELECT * FROM categories WHERE category_name=%s", ( conference['category'] ,))
    if(cur.fetchone() == None):
        # Inserts category if it doesn't already exist
        cur.execute("INSERT INTO categories (category_name) VALUES (%s)", (conference['category'], ))
    else:
        # Updates the category without changing information in order to force an updated datetime in DB
        cur.execute("UPDATE categories SET last_updated=%s WHERE category_name=%s", (datetime.now(), conference['category']))

    cur.execute("SELECT * FROM categories_conferences WHERE category=%s AND conference=%s", ( conference['category'] , conference['name'] ))
    if(cur.fetchone() == None):
        # Adds the relation if it doesn't already exist
        cur.execute("INSERT INTO categories_conferences VALUES (%s, %s)", ( conference['category'] , conference['name'] ))
    
    db.commit()

if __name__ == '__main__':
    currentConference = {'name': "TEST1", 
                         'link': 'http://www.wikicfp.com' + "/test",
                         'location': "London, United Kingdom",
                         'lat': 69,
                         'lng': -122.09711,
                         'deadline': "Mar 10, 2023",
                         'category': "robotics"}
    add_conference_safely(currentConference)