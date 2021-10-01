from flask import Flask
from services.generator import Generator
from services.output import dump_report, dump_result, get_report

TWO_MB = 2097152


app = Flask(__name__)



@app.route('/api/v1/generate-object', methods=['POST'])
def generate_object():
    generator = Generator()
    object_string = str(generator.get_object())
    
    while len(object_string.encode('utf-8')) <= TWO_MB:
        object_string += ', ' + str(generator.get_object())
        
    dump_report(generator.make_report())
    dump_result(object_string)
    
    
    return "Object generated successfully!!"

@app.route('/api/v1/generate-report', methods=['GET'])
def generate_report():
    res = get_report()
    if not isinstance(res, dict):
        raise Exception("Something is wrong happen!!")
    return res
    

@app.route('/')
def index():
    return 'Object generator running'

if __name__ == '__main__':
    app.run(debug=True)