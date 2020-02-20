# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputSoftwareComponent(object):
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
        'reboot_delay': 'int',
        'reboot_required': 'bool'
    }

    attribute_map = {
        'reboot_delay': 'rebootDelay',
        'reboot_required': 'rebootRequired'
    }

    def __init__(self, reboot_delay=None, reboot_required=None, local_vars_configuration=None):  # noqa: E501
        """InputSoftwareComponent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reboot_delay = None
        self._reboot_required = None
        self.discriminator = None

        if reboot_delay is not None:
            self.reboot_delay = reboot_delay
        if reboot_required is not None:
            self.reboot_required = reboot_required

    @property
    def reboot_delay(self):
        """Gets the reboot_delay of this InputSoftwareComponent.  # noqa: E501


        :return: The reboot_delay of this InputSoftwareComponent.  # noqa: E501
        :rtype: int
        """
        return self._reboot_delay

    @reboot_delay.setter
    def reboot_delay(self, reboot_delay):
        """Sets the reboot_delay of this InputSoftwareComponent.


        :param reboot_delay: The reboot_delay of this InputSoftwareComponent.  # noqa: E501
        :type: int
        """

        self._reboot_delay = reboot_delay

    @property
    def reboot_required(self):
        """Gets the reboot_required of this InputSoftwareComponent.  # noqa: E501


        :return: The reboot_required of this InputSoftwareComponent.  # noqa: E501
        :rtype: bool
        """
        return self._reboot_required

    @reboot_required.setter
    def reboot_required(self, reboot_required):
        """Sets the reboot_required of this InputSoftwareComponent.


        :param reboot_required: The reboot_required of this InputSoftwareComponent.  # noqa: E501
        :type: bool
        """

        self._reboot_required = reboot_required

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
        if not isinstance(other, InputSoftwareComponent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputSoftwareComponent):
            return True

        return self.to_dict() != other.to_dict()
