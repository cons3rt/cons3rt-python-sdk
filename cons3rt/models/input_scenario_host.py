# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputScenarioHost(object):
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
        'system_role': 'str',
        'system_module': 'InputSystemModuleFull',
        'master': 'bool',
        'configure_scenario_configuration': 'InputConfiguration',
        'teardown_scenario_configuration': 'InputConfiguration'
    }

    attribute_map = {
        'build_order': 'buildOrder',
        'system_role': 'systemRole',
        'system_module': 'systemModule',
        'master': 'master',
        'configure_scenario_configuration': 'configureScenarioConfiguration',
        'teardown_scenario_configuration': 'teardownScenarioConfiguration'
    }

    def __init__(self, build_order=None, system_role=None, system_module=None, master=None, configure_scenario_configuration=None, teardown_scenario_configuration=None, local_vars_configuration=None):  # noqa: E501
        """InputScenarioHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build_order = None
        self._system_role = None
        self._system_module = None
        self._master = None
        self._configure_scenario_configuration = None
        self._teardown_scenario_configuration = None
        self.discriminator = None

        if build_order is not None:
            self.build_order = build_order
        self.system_role = system_role
        if system_module is not None:
            self.system_module = system_module
        if master is not None:
            self.master = master
        if configure_scenario_configuration is not None:
            self.configure_scenario_configuration = configure_scenario_configuration
        if teardown_scenario_configuration is not None:
            self.teardown_scenario_configuration = teardown_scenario_configuration

    @property
    def build_order(self):
        """Gets the build_order of this InputScenarioHost.  # noqa: E501


        :return: The build_order of this InputScenarioHost.  # noqa: E501
        :rtype: int
        """
        return self._build_order

    @build_order.setter
    def build_order(self, build_order):
        """Sets the build_order of this InputScenarioHost.


        :param build_order: The build_order of this InputScenarioHost.  # noqa: E501
        :type: int
        """

        self._build_order = build_order

    @property
    def system_role(self):
        """Gets the system_role of this InputScenarioHost.  # noqa: E501


        :return: The system_role of this InputScenarioHost.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this InputScenarioHost.


        :param system_role: The system_role of this InputScenarioHost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_role is None:  # noqa: E501
            raise ValueError("Invalid value for `system_role`, must not be `None`")  # noqa: E501

        self._system_role = system_role

    @property
    def system_module(self):
        """Gets the system_module of this InputScenarioHost.  # noqa: E501


        :return: The system_module of this InputScenarioHost.  # noqa: E501
        :rtype: InputSystemModuleFull
        """
        return self._system_module

    @system_module.setter
    def system_module(self, system_module):
        """Sets the system_module of this InputScenarioHost.


        :param system_module: The system_module of this InputScenarioHost.  # noqa: E501
        :type: InputSystemModuleFull
        """

        self._system_module = system_module

    @property
    def master(self):
        """Gets the master of this InputScenarioHost.  # noqa: E501


        :return: The master of this InputScenarioHost.  # noqa: E501
        :rtype: bool
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this InputScenarioHost.


        :param master: The master of this InputScenarioHost.  # noqa: E501
        :type: bool
        """

        self._master = master

    @property
    def configure_scenario_configuration(self):
        """Gets the configure_scenario_configuration of this InputScenarioHost.  # noqa: E501


        :return: The configure_scenario_configuration of this InputScenarioHost.  # noqa: E501
        :rtype: InputConfiguration
        """
        return self._configure_scenario_configuration

    @configure_scenario_configuration.setter
    def configure_scenario_configuration(self, configure_scenario_configuration):
        """Sets the configure_scenario_configuration of this InputScenarioHost.


        :param configure_scenario_configuration: The configure_scenario_configuration of this InputScenarioHost.  # noqa: E501
        :type: InputConfiguration
        """

        self._configure_scenario_configuration = configure_scenario_configuration

    @property
    def teardown_scenario_configuration(self):
        """Gets the teardown_scenario_configuration of this InputScenarioHost.  # noqa: E501


        :return: The teardown_scenario_configuration of this InputScenarioHost.  # noqa: E501
        :rtype: InputConfiguration
        """
        return self._teardown_scenario_configuration

    @teardown_scenario_configuration.setter
    def teardown_scenario_configuration(self, teardown_scenario_configuration):
        """Sets the teardown_scenario_configuration of this InputScenarioHost.


        :param teardown_scenario_configuration: The teardown_scenario_configuration of this InputScenarioHost.  # noqa: E501
        :type: InputConfiguration
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
        if not isinstance(other, InputScenarioHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputScenarioHost):
            return True

        return self.to_dict() != other.to_dict()
