import pytest


def test_api_client_not_implemented():
    """Test that the BaseAPIClient request raises NotImplementedError initially."""
    from automations.api.client import BaseAPIClient

    client = BaseAPIClient(base_url="https://api.example.com")
    with pytest.raises(NotImplementedError):
        client.request("GET", "/health")


def test_api_health_not_implemented():
    """Test that check_api_health raises NotImplementedError initially."""
    from automations.api.health import check_api_health

    with pytest.raises(NotImplementedError):
        check_api_health("https://api.example.com/health")
