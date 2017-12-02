from flask import Flask, render_template, request, jsonify, url_for
from functions import fetch

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/fetch_all/", methods=['GET'])
def fetch_all():
    resp = fetch()
    return jsonify(resp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)