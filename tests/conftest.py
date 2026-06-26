from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Ensure each test runs with a clean in-memory activity dataset."""
    app_module.activities = deepcopy(INITIAL_ACTIVITIES)
    yield
    app_module.activities = deepcopy(INITIAL_ACTIVITIES)


@pytest.fixture
def client():
    with TestClient(app_module.app) as test_client:
        yield test_client
