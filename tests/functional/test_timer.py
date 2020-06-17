from app import app


def test_home():
    client = app.test_client()
    resp = client.get('/timer')
    assert resp.status_code == 200
