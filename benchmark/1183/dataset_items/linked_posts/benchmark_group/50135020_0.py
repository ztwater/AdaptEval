from bs4 import BeautifulSoup
import pytest
import requests

@pytest.fixture()
def google():
    return requests.get("https://www.google.com")


class TestGoogle:

    @pytest.fixture(autouse=True)
    def _request_google_page(self, google):
        self._response = google

    def test_alive(self):
        assert self._response.status_code == 200

    def test_html_title(self):
        soup = BeautifulSoup(self._response.content, "html.parser")
        assert soup.title.text.upper() == "GOOGLE"
