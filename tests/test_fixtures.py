import pytest

@pytest.fixture(scope="function",autouse=True)
def open_database():
    print("\nopen database\n")

@pytest.fixture(scope="function", autouse=True)
def close_database():
    yield
    print("\nclose database\n")

def test_insert_data():
    print("\ninsert data to database\n")
    assert True


def test_updat_edata():
    print("\nupdat data\n")
    assert True
   