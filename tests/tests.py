

import pytest

from tests.all_requests import make_request


def test_search_asteroids_with_sucess():
    # Arrange:
    api_key = "DEMO_KEY"
    #Act:
    response = make_request(api_key)
    #Assertion:
    assert response.status_code == 200  # Validation of status code
    data = response.json()
    # Assertion of body response content:
    assert len(data) > 0
    assert data["element_count"] > 0