from __future__ import absolute_import

from mock import Mock, patch, MagicMock
from unittest import TestCase
import httpretty
from httpretty import HTTPretty, httprettified
from python_purify import WordPurify

from json import dumps


class TestWordPurify(TestCase):
    # @patch('python_purify.WordPurify._call_method.urlopen')
    # @patch('python_purify.core.urlopen')
    # @patch('six.moves.urllib')
    # @httprettified
    def test_word_call(self):
        """
        HTTPretty.register_uri(
            HTTPretty.GET,
            "https://api1.webpurify.com/services/rest/",
            body={
                "rsp": {
                    "success": "1"
                }
            },
            status=200
        )
        """
        mock_out = dumps({"rsp": {"found": "1"}})
        mock_urlopen = Mock()
        mock_urlopen.read = Mock(return_value=mock_out)
        mock_urlopen.getcode = Mock(return_value=200)
        #mock.getcode.return_value = 200
        #m = Mock()
        #m.read.side_effect = dumps({"rsp": {"success": "1"}})
        #m.getcode.side_effect = [200]
        #mock.return_value = m
        with patch('python_purify.core.urlopen', return_value=mock_urlopen):

            wp = WordPurify("asdf")

            resp = wp.check("foo")
        print(resp)
        assert resp.get('rsp').get('found') == '1'


"""
@patch("requests.request")
def test_request(request_mock: Mock):
    response_mock = Mock(status_code=200)
    response_mock.json.return_value = {"foo": "bar"}

"""
