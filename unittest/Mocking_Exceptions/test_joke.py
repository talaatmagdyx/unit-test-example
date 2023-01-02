import unittest
from unittest.mock import patch, MagicMock

from joke import get_joke, len_joke
from requests.exceptions import Timeout, HTTPError
import requests.exceptions


class TestJoke(unittest.TestCase):

    @patch('joke.requests')
    def test_get_joke_timeout_exception(self, mock_requests):
        mock_requests.exceptions = requests.exceptions
        mock_requests.get.side_effect = Timeout('Seems that the server is down')

        self.assertEqual(get_joke(), 'No jokes')


    @patch('joke.requests')
    def test_get_joke_raise_for_status(self, mock_requests):
        mock_requests.exceptions = requests.exceptions

        mock_response = MagicMock(status_code=403)
        mock_response.raise_for_status.side_effect = HTTPError('Something goes wrong')

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_joke(), 'HTTPError was raise')

if __name__ == '__main__':
    unittest.main()
