"""tests/conftest.py"""
import pytest


class MockServer():
    def get(self, url):
        return "hello-world"

class App:
    def __init__(self, http_connection):
        print("APP CREATED")
        self.http_connection = http_connection

@pytest.fixture(scope="session")
def http_connection():
    print("HTTP_CONNECTION FIXTURE")
    return MockServer()

@pytest.fixture(scope="session")
def app(http_connection):
    print("CREATE APP")
    return App(http_connection)


class Base:
    @pytest.fixture(autouse=True)
    def _app(self, app):
        self.app = app

