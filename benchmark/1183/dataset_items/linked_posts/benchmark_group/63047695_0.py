from bs4 import BeautifulSoup
import pytest
import requests

@pytest.fixture(scope="class")
def google(request):
    request.cls.google = requests.get("https://www.google.com")


@pytest.mark.usefixtures("google")
class TestGoogle:
    def test_alive(self):
        assert self.google.status_code == 200

    def test_html_title(self):
        soup = BeautifulSoup(self.google.content, "html.parser")
        assert soup.title.text.upper() == "GOOGLE"
