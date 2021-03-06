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
from cons3rt.api.categories_api import CategoriesApi  # noqa: E501
from cons3rt.rest import ApiException


class TestCategoriesApi(unittest.TestCase):
    """CategoriesApi unit test stubs"""

    def setUp(self):
        self.api = cons3rt.api.categories_api.CategoriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_category_to_asset(self):
        """Test case for add_category_to_asset

        Assign asset to category  # noqa: E501
        """
        pass

    def test_create_category(self):
        """Test case for create_category

        Create a category  # noqa: E501
        """
        pass

    def test_delete_category(self):
        """Test case for delete_category

        Delete category  # noqa: E501
        """
        pass

    def test_get_categories(self):
        """Test case for get_categories

        List all categories  # noqa: E501
        """
        pass

    def test_remove_category_from_asset(self):
        """Test case for remove_category_from_asset

        Unassign asset from category  # noqa: E501
        """
        pass

    def test_remove_team_manager_from_team(self):
        """Test case for remove_team_manager_from_team

        Unassign manager from team  # noqa: E501
        """
        pass

    def test_set_category_parent(self):
        """Test case for set_category_parent

        Set parent category  # noqa: E501
        """
        pass

    def test_update_category(self):
        """Test case for update_category

        Update category  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
