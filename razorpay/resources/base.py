"""Base Resource class."""


class Resource:
    """Base resource class for interacting with Razorpay API."""

    def __init__(self, client=None):
        self.client = client

    def all(self, data, **kwargs):
        """Retrieve all resources."""
        return self.get(self.base_url, data, **kwargs)

    def fetch(self, resource_id, data, **kwargs):
        """Fetch a specific resource by its ID."""
        url = f"{self.base_url}/{resource_id}"
        return self.get(url, data, **kwargs)

    def get(self, url, data, **kwargs):
        """Make a GET request to the specified URL."""
        return self.client.get(url, data, **kwargs)

    def patch(self, url, data, **kwargs):
        """Make a PATCH request to the specified URL."""
        return self.client.patch(url, data, **kwargs)

    def post(self, url, data, **kwargs):
        """Make a POST request to the specified URL."""
        return self.client.post(url, data, **kwargs)

    def put(self, url, data, **kwargs):
        """Make a PUT request to the specified URL."""
        return self.client.put(url, data, **kwargs)

    def delete_url(self, url, data, **kwargs):
        """Make a DELETE request to the specified URL."""
        return self.client.delete(url, data, **kwargs)

    def delete(self, resource_id, data, **kwargs):
        """Delete a specific resource by its ID."""
        url = f"{self.base_url}/{resource_id}/delete"
        return self.delete_url(url, data, **kwargs)

    def file(self, url, data, **kwargs):
        """Upload a file to the specified URL."""
        return self.client.file(url, data, **kwargs)
