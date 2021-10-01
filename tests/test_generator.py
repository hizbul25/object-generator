import json, os

def test_generator_running(app, client):
    res = client.get("/")
    expected = {"msg": "Object generator running"}
    assert expected == json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    
def test_object_generation(app, client):
    res = client.post("/api/v1/generate-object")
    expected = {"msg": "Object generated successfully"}
    assert expected == json.loads(res.get_data(as_text=True))
    assert res.status_code == 200
    
def test_generated_object_size(app, client):
    size = int(os.path.getsize(os.getcwd() + '/data/objects.txt') / 1048576)
    assert  size == 2.0
    
def test_generated_report(app, client):
    res = client.get("/api/v1/generate-report")
    assert 'integers' in json.loads(res.get_data())
    assert 'string' in json.loads(res.get_data())
    assert 'alphanumerics' in json.loads(res.get_data())
    assert 'realnumber' in json.loads(res.get_data())
    assert 'float' not in json.loads(res.get_data())