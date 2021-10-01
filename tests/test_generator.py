import pytest
from app import app

def test_generator_running():
    res = app.get("/")
    assert res.data == 'Object generator running'
    assert res.status_code == 200