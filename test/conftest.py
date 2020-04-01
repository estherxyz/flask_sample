import pytest

from sample.app import app


@pytest.fixture
def test_client():
    """
    Flask api pytest app client.
    """
    client = app.test_client()
    return client

