"""tests/test_1.py"""
import pytest

class TestClass1:
    @pytest.fixture(autouse=True)
    def _app(self, app):
        self.app = app

    def test_1(self):
        assert self.app.http_connection.get("my-url") ==  "hello-world"

    def test_2(self):
        assert self.app.http_connection.get("my-url") ==  "hello-world"
