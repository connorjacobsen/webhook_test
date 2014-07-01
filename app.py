import json
from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    print json.dumps(request.json)
    return json.dumps(request.json), 200

if __name__ == "__main__":
    app.debug = True 
    app.run(port=8080)