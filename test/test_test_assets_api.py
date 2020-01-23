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
from cons3rt.api.test_assets_api import TestAssetsApi  # noqa: E501
from cons3rt.rest import ApiException


class TestTestAssetsApi(unittest.TestCase):
    """TestAssetsApi unit test stubs"""

    def setUp(self):
        self.api = cons3rt.api.test_assets_api.TestAssetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_test_asset_trusted_project(self):
        """Test case for add_test_asset_trusted_project

        """
        pass

    def test_get_test_asset(self):
        """Test case for get_test_asset

        Retrieve test asset  # noqa: E501
        """
        pass

    def test_get_test_assets(self):
        """Test case for get_test_assets

        List test assets  # noqa: E501
        """
        pass

    def test_get_test_assets_expanded(self):
        """Test case for get_test_assets_expanded

        List all test assets, including project assets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
