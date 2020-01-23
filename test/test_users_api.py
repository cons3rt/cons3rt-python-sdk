# coding: utf-8

"""
    CONS3RT Web API

    A CONS3RT ReSTful API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: Fred@gigagantic-server.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import cons3rt
from cons3rt.api.users_api import UsersApi  # noqa: E501
from cons3rt.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = cons3rt.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_user(self):
        """Test case for create_user

        Create a new user  # noqa: E501
        """
        pass

    def test_get_pending_users(self):
        """Test case for get_pending_users

        List pending users  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        List all Users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
