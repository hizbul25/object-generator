import os, json

def dump_result(result: str):
    try:
        f = open(os.getcwd() + '/data/objects.txt', 'w')  
        f.write(result)
        f.close()
    except IOError as e:
        print("{}".format(e))
        
        
def dump_report(result: str):
    try:
        report_file = open(os.getcwd() + '/data/report.json', 'w')
        json.dump(result, report_file, indent=4)
        report_file.close()
    except IOError as e:
        print("{}".format(e))
        
def get_report():
    try:
        report_file = open(os.getcwd() + '/data/report.json', 'r')
        data = json.loads(report_file.read())
        report_file.close()
        
        return data
    except IOError as e:
        print("{}".format(e))