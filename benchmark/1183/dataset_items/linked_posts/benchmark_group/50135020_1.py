@pytest.fixture(autouse=True)
def _request_google_page(self):
    self._response = requests.get("https://www.google.com")
