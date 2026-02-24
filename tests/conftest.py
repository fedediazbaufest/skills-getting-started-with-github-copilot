import copy
import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    # Arrange: snapshot original in-memory state
    original = copy.deepcopy(activities)
    client = TestClient(app)
    try:
        # Act/Assert: tests will run using this client
        yield client
    finally:
        # Restore state after each test
        activities.clear()
        activities.update(original)
