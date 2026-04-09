from app import app

def test_index():
    response=app.test_client().get("/")

    assert response.status_code==200
    assert response.data== b"Homepage of Devops-Team uuuu"

def test_hello():
    response=app.test_client().get("/hello")

    assert response.status_code==200
    assert response.data== b"Hello, Welcome to Devops-Team"

def about_us():
    response=app.test_client().get("/about_us")

    assert response.status_code==200
    assert response.data== b"About Devops-Team"