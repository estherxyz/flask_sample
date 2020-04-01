import pytest
from sample.app import app


def test_hello_success(test_client):
    """
    Test url=/ response is correct.

    @param test_client    (fixture) flask api app.
    """
    url = '/'
    resp = test_client.get(url)

    assert resp.status_code == 200

    resp_body = resp.json
    assert resp_body['msg'] == 'hello'
    assert type(resp_body['msg']) == str


def test_hello_fail(test_client):
    """
    Test url=/ response is different with assert value.

    @param test_client    (fixture) flask api app.
    """
    url = '/'
    resp = test_client.get(url)

    assert resp.status_code == 200

    resp_body = resp.json
    assert resp_body['msg'] == 'hello world'
    assert type(resp_body['msg']) == str

