"""tests/test_1.py"""
from conftest import Base

class TestClass1(Base):

    def test_1(self):
        assert self.app.http_connection.get("my-url") ==  "hello-world"

    def test_2(self):
        assert self.app.http_connection.get("my-url") ==  "hello-world"

