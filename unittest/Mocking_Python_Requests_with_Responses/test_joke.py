import unittest
from unittest.mock import patch, MagicMock

import requests

from joke import get_joke
import responses


class TestJoke(unittest.TestCase):

    @responses.activate
    def test_get_joke_returns_a_joke(self):
        responses.get(
            url='https://v2.jokeapi.dev/joke/Any?safe-mode',
            json={'joke': 'hello world'},
            status=200
        )
        self.assertEqual(get_joke(), 'hello world')

    @responses.activate
    def test_get_joke_connection_error(self):
        responses.get(
            url='https://v2.jokeapi.dev/joke/Any?safe-mode',
            json={'joke': 'hello world'},
            status=403
        )
        self.assertEqual(get_joke(), 'HTTPError was raise')


    @responses.activate
    def test_get_joke_raise_for_status(self):
        responses.get(
            url='https://v2.jokeapi.dev/joke/Any?safe-mode',
            body=requests.ConnectionError('ConnectionError was raised')
        )
        self.assertEqual(get_joke(), 'ConnectionError was raised')

if __name__ == '__main__':
    unittest.main()
