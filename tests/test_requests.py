import requests


def test_successful_response():
    assert requests.get("http://techstepacademy.com/training-ground").status_code == 200


def test_404_error():
    assert requests.get("http://techstepacademy.com/t").status_code == 404


def test_twitter():
    assert "twitter" in requests.get("http://techstepacademy.com/training-ground").text
