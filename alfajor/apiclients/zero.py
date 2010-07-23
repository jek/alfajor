# Copyright Action Without Borders, Inc., the Alfajor authors and contributors.
# All rights reserved.  See AUTHORS.
#
# This file is part of 'Alfajor' and is distributed under the BSD license.
# See LICENSE for more details.

"""A non-functional web API client.

Documents the canonical base implementation of api clients.  Zero is
instantiable and usable, however it does not supply any capabilities.

"""

__all__ = ['Zero']


class Zero(object):
    """A non-functional APIClient"""

    #: Capabilities provided by this APIClient implementation
    capabilities = []

    #: Default HTTP version for new requests
    http_version = 'HTTP/1.0'

    user_agent = {
        'browser': 'zero-client',
        'platform': 'python',
        'version': '0.1',
        }

    def open(self, uri, method, query=None, post=None, body=None,
             base_url=None, headers=(), http_version=None):
        """Issue a http request & return a response."""
        return ZeroResponse(self)

    def get(self, uri, query=None, base_url=None, headers=()):
        """Issue a GET request & return a response."""
        return self.open(uri, 'GET', query=query,
                         base_url=base_url, headers=headers)

    def head(self, uri, query=None, base_url=None, headers=()):
        """Issue a HEAD request & return a response."""
        return self.open(uri, 'HEAD', query=query,
                         base_url=base_url, headers=headers)

    def post(self, uri, post=None, base_url=None, headers=()):
        """Issue a POST request & return a response."""
        return self.open(uri, 'POST', post=post,
                         base_url=base_url, headers=headers)

    def put(self, uri, body=None, base_url=None, headers=()):
        """Issue a PUT request & return a response."""
        return self.open(uri, 'PUT', body=body,
                         base_url=base_url, headers=headers)

    def delete(self, uri, base_url=None, headers=()):
        """Issue a DELETE request & return a response."""
        return self.open(uri, 'DELETE', base_url=base_url, headers=headers)

    def options(self, uri, body=None, base_url=None, headers=()):
        """Issue an OPTIONS request & return a response."""
        return self.open(uri, 'OPTIONS', body=body,
                         base_url=base_url, headers=headers)

    def set_cookie(self, name, value, domain=None, path='/', **kw):
        """Set a cookie."""

    def delete_cookie(self, name, domain=None, path='/', **kw):
        """Delete a cookie."""


class ZeroResponse(object):
    """An APIClient response."""

    status_code = 0
    status = None

    request_uri = None

    headers = {}
    cookies = {}

    #: The source URI for this response.
    response = None

    #: True if ``Content-Type`` indicates :attr:`response` contains JSON data.
    is_json = False

    #: The :attr:`response` parsed as JSON.
    #:
    #: No attempt is made to ensure the response is valid or even looks
    #: like JSON before parsing.
    json = None

    def __init__(self, _client):
        self._client = _client

    @property
    def client(self):
        """A new client born from this response.

        The client will have access to any cookies that were sent as part
        of this response & send this response's URL as a referrer.

        Each access to this property returns an independent client with its
        own copy of the cookie jar.

        """
        return self._client
