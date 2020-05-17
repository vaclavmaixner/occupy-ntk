from app import app

"""
Test conneciton of pytest and the app running.
"""

def test_app():
    response = app.test_client().get('/')

    assert response.status_code == 200