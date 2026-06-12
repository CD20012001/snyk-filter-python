import flask
import requests

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Snyk SAST Python test"

if __name__ == "__main__":
    app.run()
