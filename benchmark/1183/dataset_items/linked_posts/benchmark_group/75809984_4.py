"""tests/sub_folder/test_sub_1.py"""

class TestSubClass1:

    def test_sub_1(self, app):
        http_connection = app.http_connection

        assert http_connection.get("my-url") ==  "hello-world"

    def test_sub_2(self, app):
        http_connection = app.http_connection

        assert http_connection.get("my-url") ==  "hello-world"

