from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Alterei denovo  2x</p>"
