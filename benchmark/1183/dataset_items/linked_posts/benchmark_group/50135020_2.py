from bs4 import BeautifulSoup
import pytest
import requests


@pytest.fixture(scope='module')
def google():
    return requests.get("https://www.google.com")


@pytest.fixture(autouse=True, scope='class')
def _request_google_page(request, google):
    request.cls._response = google


class TestGoogle:

    def test_alive(self):
        assert self._response.status_code == 200

    def test_html_title(self):
        soup = BeautifulSoup(self._response.content, "html.parser")
        assert soup.title.text.upper() == "GOOGLE"
