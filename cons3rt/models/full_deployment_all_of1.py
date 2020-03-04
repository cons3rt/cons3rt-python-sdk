"""
   Copyright 2020 Jackpine Technologies Corporation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration

__author__ = 'Jackpine Technologies Corporation'
__copyright__ = 'Copyright 2020, Jackpine Technologies Corporation'
__license__ = 'Apache 2.0',
__version__ = '1.0.0'
__maintainer__ = 'API Support'
__email__ = 'support@cons3rt.com'


class FullDeploymentAllOf1(object):
    """NOTE: This class is auto-generated. Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'recurring_schedules': 'list[MinimalRecurringSchedule]',
        'scenario': 'list[GeneralScenario]',
        'test_bundles': 'list[MinimalTestBundle]',
        'deployment_hosts': 'list[MinimalDeploymentHost]'
    }

    attribute_map = {
        'recurring_schedules': 'recurringSchedules',
        'scenario': 'scenario',
        'test_bundles': 'testBundles',
        'deployment_hosts': 'deploymentHosts'
    }

    def __init__(self, recurring_schedules=None, scenario=None, test_bundles=None, deployment_hosts=None, local_vars_configuration=None):  # noqa: E501
        """FullDeploymentAllOf1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._recurring_schedules = None
        self._scenario = None
        self._test_bundles = None
        self._deployment_hosts = None
        self.discriminator = None

        if recurring_schedules is not None:
            self.recurring_schedules = recurring_schedules
        if scenario is not None:
            self.scenario = scenario
        if test_bundles is not None:
            self.test_bundles = test_bundles
        if deployment_hosts is not None:
            self.deployment_hosts = deployment_hosts

    @property
    def recurring_schedules(self):
        """Gets the recurring_schedules of this FullDeploymentAllOf1.  # noqa: E501


        :return: The recurring_schedules of this FullDeploymentAllOf1.  # noqa: E501
        :rtype: list[MinimalRecurringSchedule]
        """
        return self._recurring_schedules

    @recurring_schedules.setter
    def recurring_schedules(self, recurring_schedules):
        """Sets the recurring_schedules of this FullDeploymentAllOf1.


        :param recurring_schedules: The recurring_schedules of this FullDeploymentAllOf1.  # noqa: E501
        :type: list[MinimalRecurringSchedule]
        """

        self._recurring_schedules = recurring_schedules

    @property
    def scenario(self):
        """Gets the scenario of this FullDeploymentAllOf1.  # noqa: E501


        :return: The scenario of this FullDeploymentAllOf1.  # noqa: E501
        :rtype: list[GeneralScenario]
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this FullDeploymentAllOf1.


        :param scenario: The scenario of this FullDeploymentAllOf1.  # noqa: E501
        :type: list[GeneralScenario]
        """

        self._scenario = scenario

    @property
    def test_bundles(self):
        """Gets the test_bundles of this FullDeploymentAllOf1.  # noqa: E501


        :return: The test_bundles of this FullDeploymentAllOf1.  # noqa: E501
        :rtype: list[MinimalTestBundle]
        """
        return self._test_bundles

    @test_bundles.setter
    def test_bundles(self, test_bundles):
        """Sets the test_bundles of this FullDeploymentAllOf1.


        :param test_bundles: The test_bundles of this FullDeploymentAllOf1.  # noqa: E501
        :type: list[MinimalTestBundle]
        """

        self._test_bundles = test_bundles

    @property
    def deployment_hosts(self):
        """Gets the deployment_hosts of this FullDeploymentAllOf1.  # noqa: E501


        :return: The deployment_hosts of this FullDeploymentAllOf1.  # noqa: E501
        :rtype: list[MinimalDeploymentHost]
        """
        return self._deployment_hosts

    @deployment_hosts.setter
    def deployment_hosts(self, deployment_hosts):
        """Sets the deployment_hosts of this FullDeploymentAllOf1.


        :param deployment_hosts: The deployment_hosts of this FullDeploymentAllOf1.  # noqa: E501
        :type: list[MinimalDeploymentHost]
        """

        self._deployment_hosts = deployment_hosts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FullDeploymentAllOf1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullDeploymentAllOf1):
            return True

        return self.to_dict() != other.to_dict()
