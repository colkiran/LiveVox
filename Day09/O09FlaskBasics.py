
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
   return "<h2> Welcome to Flask framework </h2>"

@app.route("/<usrname>")
def user(usrname):
    return f"<h3> Greetings {usrname}, Welcome to flask programming....."

if __name__ == '__main__':
    app.run(debug=True)

