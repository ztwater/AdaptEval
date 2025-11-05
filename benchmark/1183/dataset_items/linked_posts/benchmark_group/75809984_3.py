class TestClass2:

    def test_1(self, app):
        http_connection = app.http_connection

        assert http_connection.get("my-url") ==  "hello-world"

    def test_2(self, app):
        http_connection = app.http_connection

        assert http_connection.get("my-url") ==  "hello-world"
