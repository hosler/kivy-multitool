from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/list1')
def list1():
    d = [
            {
                "type": "MDList",
                "widgets": [
                            {
                                "type": "TwoLineListItem",
                                "text": "value1",
                                "secondary_text": "value1_small"
                            },
                            {
                                "type": "TwoLineListItem",
                                "text": "value2",
                                "secondary_text": "value2_small"
                            }
                        ]
            }
        ]
    return jsonify(d)

@app.route('/list2')
def list2():
    d = [
        {
        "type": "FloatLayout",
        "widgets": [
            {
                "type": "BoxLayout",
                #"size": "root.size",
                "orientation": "vertical",
                "widgets": [
                            {
                                "type": "MDLabel",
                                "text": "hoora",
                                "id": "l1"
                            },
                            {
                                "type": "MDRaisedButton",
                                "text": "value1",
                            },
                            {
                                "type": "MDRaisedButton",
                                "text": "value2",
                                "on_release": {
                                    "api": "action1",
                                    "display": "l1"
                                }
                            }
                        ]
            }
            ]
        }
        ]
    return jsonify(d)

@app.route('/action1')
def action1():
    d = "hi"
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