import pytest
from sample.app import app


### do not use fixture
def test_hello_1():
    url = '/'
    resp = app.test_client().get(url)

    assert resp.status_code == 200
    assert resp.json == {
                'msg': 'hello'
            }


### use fixture to get test_client
#@pytest.fixture
#def test_client():
#    client = app.test_client()
#    return client

def test_hello_2(test_client):
    url = '/'
    resp = test_client.get(url)

    assert resp.status_code == 200
    assert resp.json == {
                'msg': 'hello'
            }


