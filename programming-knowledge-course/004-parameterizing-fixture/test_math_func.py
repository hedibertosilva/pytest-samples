import pytest

from math_func import StudentDB


@pytest.fixture(scope="session")
def db(request):
    print('---- setup ----')
    db = StudentDB()
    db.connect("data.json")
    yield db
    print('---- teardown ----')
    db.disconnect()


@pytest.fixture(scope="session",
                params=[
                    {"id": 1, "name": "Scott", "result": "pass"},
                    {"id": 2, "name": "Mark", "result": "fail"}
                ])
def user(request):
    return request.param


def test_scott_data(db, user):
    user_data = db.get_data(user["name"])
    assert user_data["id"] == user["id"]
    assert user_data["name"] == user["name"]
    assert user_data["result"] == user["result"]
