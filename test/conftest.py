import pytest

from sample.main import app


@pytest.fixture
def test_client():
    """
    Flask api pytest app client.
    """
    client = app.test_client()
    return client

