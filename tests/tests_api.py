import requests


def test_auth():
    url = "http://the-internet.herokuapp.com/basic_auth"
    response = requests.get(url, auth=("admin", "admin"))
    assert response.status_code == 200, "Expected 200 status code"
    expected_text = "Congratulations! You must have the proper credentials."
    assert expected_text in response.text, "Success message not found"


def test_status_code():
    url = "http://the-internet.herokuapp.com/status_codes/200"
    response = requests.get(url)
    assert response.status_code == 200, "Expected 200 status code"
    expected_message = "This page returned 200 status code"
    assert expected_message in response.text, "Status code message not found"
