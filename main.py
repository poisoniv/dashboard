from flask import Flask, render_template, request, jsonify, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/forward/", methods=['POST'])
def move_forward():
    #Moving forward code
    print("Hey Cliff")
    forward_message = "Moving Forward..."
    return render_template('index.html', message=forward_message);

#@app.route("/functions")
#def functions():
#    return  "some json here"

if __name__ == "__main__":
    app.run(debug=True)