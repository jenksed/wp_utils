import requests

class WordPressAPI:
    """
    Main client for interacting with the WordPress API.
    """
    def __init__(self, api_url):
        self.api_url = api_url

    def _make_request(self, method, endpoint, params=None, data=None):
        """Handles API requests, error handling, etc."""
        url = f"{self.api_url}{endpoint}"
        response = requests.request(method, url, params=params, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()

    def fetch_pages(self, params=None):
        """Fetches pages from WordPress."""
        endpoint = "/wp-json/wp/v2/pages"
        return self._make_request("GET", endpoint, params=params)

    def fetch_page(self, page_id):
        """Fetches a single page from WordPress by ID."""
        endpoint = f"/wp-json/wp/v2/pages/{page_id}"
        return self._make_request("GET", endpoint)
