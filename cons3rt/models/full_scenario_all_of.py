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


class FullScenarioAllOf(object):
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
        'scenario_hosts': 'list[MinimalScenarioHost]',
        'prepare_scenario_configuration': 'MinimalConfiguration',
        'teardown_scenario_configuration': 'MinimalConfiguration'
    }

    attribute_map = {
        'scenario_hosts': 'scenarioHosts',
        'prepare_scenario_configuration': 'prepareScenarioConfiguration',
        'teardown_scenario_configuration': 'teardownScenarioConfiguration'
    }

    def __init__(self, scenario_hosts=None, prepare_scenario_configuration=None, teardown_scenario_configuration=None, local_vars_configuration=None):  # noqa: E501
        """FullScenarioAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._scenario_hosts = None
        self._prepare_scenario_configuration = None
        self._teardown_scenario_configuration = None
        self.discriminator = None

        if scenario_hosts is not None:
            self.scenario_hosts = scenario_hosts
        if prepare_scenario_configuration is not None:
            self.prepare_scenario_configuration = prepare_scenario_configuration
        if teardown_scenario_configuration is not None:
            self.teardown_scenario_configuration = teardown_scenario_configuration

    @property
    def scenario_hosts(self):
        """Gets the scenario_hosts of this FullScenarioAllOf.  # noqa: E501


        :return: The scenario_hosts of this FullScenarioAllOf.  # noqa: E501
        :rtype: list[MinimalScenarioHost]
        """
        return self._scenario_hosts

    @scenario_hosts.setter
    def scenario_hosts(self, scenario_hosts):
        """Sets the scenario_hosts of this FullScenarioAllOf.


        :param scenario_hosts: The scenario_hosts of this FullScenarioAllOf.  # noqa: E501
        :type: list[MinimalScenarioHost]
        """

        self._scenario_hosts = scenario_hosts

    @property
    def prepare_scenario_configuration(self):
        """Gets the prepare_scenario_configuration of this FullScenarioAllOf.  # noqa: E501


        :return: The prepare_scenario_configuration of this FullScenarioAllOf.  # noqa: E501
        :rtype: MinimalConfiguration
        """
        return self._prepare_scenario_configuration

    @prepare_scenario_configuration.setter
    def prepare_scenario_configuration(self, prepare_scenario_configuration):
        """Sets the prepare_scenario_configuration of this FullScenarioAllOf.


        :param prepare_scenario_configuration: The prepare_scenario_configuration of this FullScenarioAllOf.  # noqa: E501
        :type: MinimalConfiguration
        """

        self._prepare_scenario_configuration = prepare_scenario_configuration

    @property
    def teardown_scenario_configuration(self):
        """Gets the teardown_scenario_configuration of this FullScenarioAllOf.  # noqa: E501


        :return: The teardown_scenario_configuration of this FullScenarioAllOf.  # noqa: E501
        :rtype: MinimalConfiguration
        """
        return self._teardown_scenario_configuration

    @teardown_scenario_configuration.setter
    def teardown_scenario_configuration(self, teardown_scenario_configuration):
        """Sets the teardown_scenario_configuration of this FullScenarioAllOf.


        :param teardown_scenario_configuration: The teardown_scenario_configuration of this FullScenarioAllOf.  # noqa: E501
        :type: MinimalConfiguration
        """

        self._teardown_scenario_configuration = teardown_scenario_configuration

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
        if not isinstance(other, FullScenarioAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullScenarioAllOf):
            return True

        return self.to_dict() != other.to_dict()
