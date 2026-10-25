from l1json import fetch_post, fetch_todos
from unittest.mock import Mock,patch
import requests
with patch("requests.get",side_effect=requests.exceptions.ConnectionError("Simulated connection failure")):
    result=fetch_post(1)
    print("Returned:",result)
    assert result is None
fake_response = Mock()
fake_response.raise_for_status.return_value = None
fake_response.json.side_effect = requests.exceptions.JSONDecodeError("Invalid JSON", "not json", 0)

with patch("requests.get", return_value=fake_response):
    result = fetch_post(1)
    print("Returned:", result)
    assert result is None

fake_response=Mock()
fake_response.raise_for_status.return_value=None
expected={
    "userId":1,
    "id":1,
    "title":"Test title",
    "body":"Test body"
}
fake_response.json.return_value=expected
with patch("requests.get",return_value=fake_response):
    result=fetch_post(1)

assert result==expected
print("Successful post test passed")

fake_response=Mock()
fake_response.raise_for_status.side_effect=requests.exceptions.HTTPError("Simulated HTTP 404")
with patch("requests.get",return_value=fake_response):
    result=fetch_post(9999)
    print("Returned",result)
    assert result is None
print("HTTP error test passed")

fake_response=Mock()
fake_response.raise_for_status.return_value=None
expected=[
    {
        "userId":1,
        "id":1,
        "title":"Test todo",
        "completed":False
    }
]

fake_response.json.return_value=expected
with patch("requests.get",return_value=fake_response):
    result=fetch_todos(1)

assert result==expected
assert isinstance(result,list)

print("Successful todos test passed")