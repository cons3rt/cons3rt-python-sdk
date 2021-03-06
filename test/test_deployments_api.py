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
from cons3rt.api.deployments_api import DeploymentsApi  # noqa: E501
from cons3rt.rest import ApiException


class TestDeploymentsApi(unittest.TestCase):
    """DeploymentsApi unit test stubs"""

    def setUp(self):
        self.api = cons3rt.api.deployments_api.DeploymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_recurring_schedule(self):
        """Test case for add_recurring_schedule

        Add recurring schedule  # noqa: E501
        """
        pass

    def test_clone_deployment(self):
        """Test case for clone_deployment

        Clone deployment  # noqa: E501
        """
        pass

    def test_clone_system(self):
        """Test case for clone_system

        Clone system  # noqa: E501
        """
        pass

    def test_create_deployment_entire(self):
        """Test case for create_deployment_entire

        Create deployment  # noqa: E501
        """
        pass

    def test_determine_valid_virtualization_realms(self):
        """Test case for determine_valid_virtualization_realms

        List valid virtualization realms  # noqa: E501
        """
        pass

    def test_get_bindings_for_deployment(self):
        """Test case for get_bindings_for_deployment

        List bindings  # noqa: E501
        """
        pass

    def test_get_deployment(self):
        """Test case for get_deployment

        Retrieve deployment  # noqa: E501
        """
        pass

    def test_get_deployment_metric(self):
        """Test case for get_deployment_metric

        Retrieve metrics  # noqa: E501
        """
        pass

    def test_get_deployment_runs(self):
        """Test case for get_deployment_runs

        List deployment runs  # noqa: E501
        """
        pass

    def test_get_deployment_runs_in_virtualization_realm(self):
        """Test case for get_deployment_runs_in_virtualization_realm

        List deployment runs  # noqa: E501
        """
        pass

    def test_get_deployments(self):
        """Test case for get_deployments

        List deployments  # noqa: E501
        """
        pass

    def test_get_deployments_expanded(self):
        """Test case for get_deployments_expanded

        List all deployments, including project assets  # noqa: E501
        """
        pass

    def test_get_valid_networks_for_virtualization_realm(self):
        """Test case for get_valid_networks_for_virtualization_realm

        List virtualization realm networks  # noqa: E501
        """
        pass

    def test_launch_deployment(self):
        """Test case for launch_deployment

        Launch deployment  # noqa: E501
        """
        pass

    def test_list_options(self):
        """Test case for list_options

        List run options  # noqa: E501
        """
        pass

    def test_list_properties(self):
        """Test case for list_properties

        List properties  # noqa: E501
        """
        pass

    def test_list_schedules(self):
        """Test case for list_schedules

        List recurring schedules  # noqa: E501
        """
        pass

    def test_remove_recurring_schedule(self):
        """Test case for remove_recurring_schedule

        Remove recurring schedule  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
