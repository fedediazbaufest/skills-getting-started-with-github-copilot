import urllib.parse


def test_get_activities(client):
    # Arrange: client fixture provides TestClient and activities prepopulated

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert "Chess Club" in data
    assert "michael@mergington.edu" in data["Chess Club"]["participants"]


def test_signup_success(client):
    # Arrange
    email = "newstudent@example.com"
    path = f"/activities/{urllib.parse.quote('Chess Club')}/signup"

    # Act
    resp = client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 200
    data = client.get("/activities").json()
    assert email in data["Chess Club"]["participants"]


def test_signup_duplicate(client):
    # Arrange
    email = "michael@mergington.edu"
    path = f"/activities/{urllib.parse.quote('Chess Club')}/signup"

    # Act
    resp = client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_unregister_success(client):
    # Arrange
    email = "alex@mergington.edu"
    path = f"/activities/{urllib.parse.quote('Basketball Team')}/unregister"

    # Act
    resp = client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 200
    data = client.get("/activities").json()
    assert email not in data["Basketball Team"]["participants"]


def test_unregister_missing(client):
    # Arrange
    email = "nonexistent@example.com"
    path = f"/activities/{urllib.parse.quote('Basketball Team')}/unregister"

    # Act
    resp = client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 400
