
@patch("requests.request")
def test_request(request_mock: Mock):
    response_mock = Mock(status_code=200)
    response_mock.json.return_value = {"foo": "bar"}