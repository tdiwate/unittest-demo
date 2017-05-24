#!/usr/bin/env python

import requests


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise BadResponse('Encountered Bad response code', response.status_code)


class BadResponse(Exception):
    """ Any non 2XX range response """
    def __init__(self, message, code):
        self.code = code
        Exception.__init__(self, message)
