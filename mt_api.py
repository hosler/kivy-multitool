from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/list1')
@app.route('/list2')
def list1():
    d = {
        "thing1": {
            "type": "TwoLineListItem",
            "text": "value1",
            "secondary_text": "value1_small"
        },
        "thing2": {
            "type": "TwoLineListItem",
            "text": "value2",
            "secondary_text": "value2_small"
        }
    }
    return jsonify(d)


@app.route('/getkvfile')
def getkvfile():
    with open("mt_layout.kv", 'r') as f:
        file_content = f.read()
    return file_content

@app.route('/getnav')
def getnav():
    d = {
        "the servers": "list1",
    }
    return jsonify(d)

@app.route('/getworknav')
def getworknav():
    d = {
        "the servers": "list1",
        "other stuff": "list2"
    }
    return jsonify(d)