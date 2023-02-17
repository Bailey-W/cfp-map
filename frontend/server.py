from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('map.html', conferences=['1', '2', '3', '4'])

if __name__ == '__main__':
    app.run(debug=True)