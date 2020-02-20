# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class SoftwareInstallationAllOf(object):
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
        'asset_type': 'str',
        'reboot_delay_seconds': 'int',
        'reboot_required': 'bool'
    }

    attribute_map = {
        'asset_type': 'assetType',
        'reboot_delay_seconds': 'rebootDelaySeconds',
        'reboot_required': 'rebootRequired'
    }

    def __init__(self, asset_type=None, reboot_delay_seconds=None, reboot_required=None, local_vars_configuration=None):  # noqa: E501
        """SoftwareInstallationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_type = None
        self._reboot_delay_seconds = None
        self._reboot_required = None
        self.discriminator = None

        if asset_type is not None:
            self.asset_type = asset_type
        if reboot_delay_seconds is not None:
            self.reboot_delay_seconds = reboot_delay_seconds
        if reboot_required is not None:
            self.reboot_required = reboot_required

    @property
    def asset_type(self):
        """Gets the asset_type of this SoftwareInstallationAllOf.  # noqa: E501


        :return: The asset_type of this SoftwareInstallationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        """Sets the asset_type of this SoftwareInstallationAllOf.


        :param asset_type: The asset_type of this SoftwareInstallationAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["APPLICATION", "SOURCE_CODE", "TEST_TOOL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and asset_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `asset_type` ({0}), must be one of {1}"  # noqa: E501
                .format(asset_type, allowed_values)
            )

        self._asset_type = asset_type

    @property
    def reboot_delay_seconds(self):
        """Gets the reboot_delay_seconds of this SoftwareInstallationAllOf.  # noqa: E501


        :return: The reboot_delay_seconds of this SoftwareInstallationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._reboot_delay_seconds

    @reboot_delay_seconds.setter
    def reboot_delay_seconds(self, reboot_delay_seconds):
        """Sets the reboot_delay_seconds of this SoftwareInstallationAllOf.


        :param reboot_delay_seconds: The reboot_delay_seconds of this SoftwareInstallationAllOf.  # noqa: E501
        :type: int
        """

        self._reboot_delay_seconds = reboot_delay_seconds

    @property
    def reboot_required(self):
        """Gets the reboot_required of this SoftwareInstallationAllOf.  # noqa: E501


        :return: The reboot_required of this SoftwareInstallationAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._reboot_required

    @reboot_required.setter
    def reboot_required(self, reboot_required):
        """Sets the reboot_required of this SoftwareInstallationAllOf.


        :param reboot_required: The reboot_required of this SoftwareInstallationAllOf.  # noqa: E501
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
        if not isinstance(other, SoftwareInstallationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SoftwareInstallationAllOf):
            return True

        return self.to_dict() != other.to_dict()
