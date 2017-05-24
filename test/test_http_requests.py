#!/usr/bin/env python

import unittest
from src import http_requests
from mock import MagicMock, patch
import requests


class TestHttpRequest(unittest.TestCase):

    def test_get_version_1(self):
        """ Not a good ut """
        response = http_requests.get_data('http://www.google.com')
        self.assertIsNotNone(response)

    def test_get_with_patch(self):
        """ Test a positive test case with status_code 200 """
        with patch('src.http_requests.requests') as mock_request:
            mock_url = 'xyz'
            mock_response = MagicMock()
            # mock status code to 200 and text to something
            mock_response.status_code = 200
            mock_response.text = 'some_response text'
            mock_request.get.return_value = mock_response
            response = http_requests.get_data(mock_url)
            mock_request.get.assert_called_with(mock_url)
            self.assertEqual(response, mock_response.text)

    def test_get_raises_bad_response(self):
        """ Test get_data raises BadResponse exception """
        with patch('src.http_requests.requests') as mock_request:
            mock_response = MagicMock()
            # mock status code to non 200 code
            mock_response.status_code = 500
            mock_request.get.return_value = mock_response
            self.assertRaises(http_requests.BadResponse, http_requests.get_data, 'xyz.com')

    def test_get_raises_connection_timeout_exception(self):
        """ Test get_data raises ConnectionError """
        with patch('src.http_requests.requests') as mock_request:
            # add a side_effect as ConnectionError and test whether it is being raised or not
            mock_request.get.side_effect = requests.ConnectionError()
            self.assertRaises(requests.ConnectionError, http_requests.get_data, 'xyz.com')
