from flask import Flask, jsonify
from services.output import get_report
from tasks import generate_object_background
import json

app = Flask(__name__)



@app.route('/api/v1/generate-object', methods=['POST'])
def generate_object():
    task = generate_object_background.delay()
    print("task id {0}".format(task.id))
    return jsonify({"msg": "Object creation is running in background!!"})

@app.route('/api/v1/generate-report', methods=['GET'])
def generate_report():
    res = get_report()
    if not isinstance(res, dict):
        raise Exception("Something is wrong happen!!")
    return jsonify(res)
    

@app.route('/')
def index():
    return jsonify({"msg": "Object generator running"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)