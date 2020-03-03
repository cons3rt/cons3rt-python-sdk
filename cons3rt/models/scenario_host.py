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


class ScenarioHost(object):
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
        'build_order': 'int',
        'configure_scenario_configuration': 'Configuration',
        'teardown_scenario_configuration': 'Configuration',
        'id': 'int',
        'master': 'bool',
        'system_module': 'SystemModule',
        'system_role': 'str'
    }

    attribute_map = {
        'build_order': 'buildOrder',
        'configure_scenario_configuration': 'configureScenarioConfiguration',
        'teardown_scenario_configuration': 'teardownScenarioConfiguration',
        'id': 'id',
        'master': 'master',
        'system_module': 'systemModule',
        'system_role': 'systemRole'
    }

    def __init__(self, build_order=None, configure_scenario_configuration=None, teardown_scenario_configuration=None, id=None, master=None, system_module=None, system_role=None, local_vars_configuration=None):  # noqa: E501
        """ScenarioHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build_order = None
        self._configure_scenario_configuration = None
        self._teardown_scenario_configuration = None
        self._id = None
        self._master = None
        self._system_module = None
        self._system_role = None
        self.discriminator = None

        if build_order is not None:
            self.build_order = build_order
        if configure_scenario_configuration is not None:
            self.configure_scenario_configuration = configure_scenario_configuration
        if teardown_scenario_configuration is not None:
            self.teardown_scenario_configuration = teardown_scenario_configuration
        if id is not None:
            self.id = id
        if master is not None:
            self.master = master
        self.system_module = system_module
        self.system_role = system_role

    @property
    def build_order(self):
        """Gets the build_order of this ScenarioHost.  # noqa: E501


        :return: The build_order of this ScenarioHost.  # noqa: E501
        :rtype: int
        """
        return self._build_order

    @build_order.setter
    def build_order(self, build_order):
        """Sets the build_order of this ScenarioHost.


        :param build_order: The build_order of this ScenarioHost.  # noqa: E501
        :type: int
        """

        self._build_order = build_order

    @property
    def configure_scenario_configuration(self):
        """Gets the configure_scenario_configuration of this ScenarioHost.  # noqa: E501


        :return: The configure_scenario_configuration of this ScenarioHost.  # noqa: E501
        :rtype: Configuration
        """
        return self._configure_scenario_configuration

    @configure_scenario_configuration.setter
    def configure_scenario_configuration(self, configure_scenario_configuration):
        """Sets the configure_scenario_configuration of this ScenarioHost.


        :param configure_scenario_configuration: The configure_scenario_configuration of this ScenarioHost.  # noqa: E501
        :type: Configuration
        """

        self._configure_scenario_configuration = configure_scenario_configuration

    @property
    def teardown_scenario_configuration(self):
        """Gets the teardown_scenario_configuration of this ScenarioHost.  # noqa: E501


        :return: The teardown_scenario_configuration of this ScenarioHost.  # noqa: E501
        :rtype: Configuration
        """
        return self._teardown_scenario_configuration

    @teardown_scenario_configuration.setter
    def teardown_scenario_configuration(self, teardown_scenario_configuration):
        """Sets the teardown_scenario_configuration of this ScenarioHost.


        :param teardown_scenario_configuration: The teardown_scenario_configuration of this ScenarioHost.  # noqa: E501
        :type: Configuration
        """

        self._teardown_scenario_configuration = teardown_scenario_configuration

    @property
    def id(self):
        """Gets the id of this ScenarioHost.  # noqa: E501


        :return: The id of this ScenarioHost.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScenarioHost.


        :param id: The id of this ScenarioHost.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def master(self):
        """Gets the master of this ScenarioHost.  # noqa: E501


        :return: The master of this ScenarioHost.  # noqa: E501
        :rtype: bool
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this ScenarioHost.


        :param master: The master of this ScenarioHost.  # noqa: E501
        :type: bool
        """

        self._master = master

    @property
    def system_module(self):
        """Gets the system_module of this ScenarioHost.  # noqa: E501


        :return: The system_module of this ScenarioHost.  # noqa: E501
        :rtype: SystemModule
        """
        return self._system_module

    @system_module.setter
    def system_module(self, system_module):
        """Sets the system_module of this ScenarioHost.


        :param system_module: The system_module of this ScenarioHost.  # noqa: E501
        :type: SystemModule
        """
        if self.local_vars_configuration.client_side_validation and system_module is None:  # noqa: E501
            raise ValueError("Invalid value for `system_module`, must not be `None`")  # noqa: E501

        self._system_module = system_module

    @property
    def system_role(self):
        """Gets the system_role of this ScenarioHost.  # noqa: E501


        :return: The system_role of this ScenarioHost.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this ScenarioHost.


        :param system_role: The system_role of this ScenarioHost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_role is None:  # noqa: E501
            raise ValueError("Invalid value for `system_role`, must not be `None`")  # noqa: E501

        self._system_role = system_role

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
        if not isinstance(other, ScenarioHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScenarioHost):
            return True

        return self.to_dict() != other.to_dict()
