# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class MinimalConfiguration(object):
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
        'configuration_script_type': 'str',
        'script_name': 'str',
        'script': 'str'
    }

    attribute_map = {
        'configuration_script_type': 'configurationScriptType',
        'script_name': 'scriptName',
        'script': 'script'
    }

    def __init__(self, configuration_script_type=None, script_name=None, script=None, local_vars_configuration=None):  # noqa: E501
        """MinimalConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._configuration_script_type = None
        self._script_name = None
        self._script = None
        self.discriminator = None

        if configuration_script_type is not None:
            self.configuration_script_type = configuration_script_type
        if script_name is not None:
            self.script_name = script_name
        if script is not None:
            self.script = script

    @property
    def configuration_script_type(self):
        """Gets the configuration_script_type of this MinimalConfiguration.  # noqa: E501


        :return: The configuration_script_type of this MinimalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._configuration_script_type

    @configuration_script_type.setter
    def configuration_script_type(self, configuration_script_type):
        """Sets the configuration_script_type of this MinimalConfiguration.


        :param configuration_script_type: The configuration_script_type of this MinimalConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["HOST_INIT", "CONFIGURE_SCENARIO_HOST", "CUSTOMIZE_OS_HOST", "CONFIGURE_SCENARIO_MASTER", "CONFIGURE_TEST_MASTER", "CONFIGURE_TEST_HOST", "TEARDOWN_TEST_MASTER", "TEARDOWN_SCENARIO_HOST", "TEARDOWN_SCENARIO_MASTER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and configuration_script_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `configuration_script_type` ({0}), must be one of {1}"  # noqa: E501
                .format(configuration_script_type, allowed_values)
            )

        self._configuration_script_type = configuration_script_type

    @property
    def script_name(self):
        """Gets the script_name of this MinimalConfiguration.  # noqa: E501


        :return: The script_name of this MinimalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        """Sets the script_name of this MinimalConfiguration.


        :param script_name: The script_name of this MinimalConfiguration.  # noqa: E501
        :type: str
        """

        self._script_name = script_name

    @property
    def script(self):
        """Gets the script of this MinimalConfiguration.  # noqa: E501


        :return: The script of this MinimalConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this MinimalConfiguration.


        :param script: The script of this MinimalConfiguration.  # noqa: E501
        :type: str
        """

        self._script = script

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
        if not isinstance(other, MinimalConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalConfiguration):
            return True

        return self.to_dict() != other.to_dict()
