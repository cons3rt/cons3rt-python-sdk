# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class VCloudClient(object):
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
        'org_name': 'str',
        'vdc_name': 'str'
    }

    attribute_map = {
        'org_name': 'orgName',
        'vdc_name': 'vdcName'
    }

    def __init__(self, org_name=None, vdc_name=None, local_vars_configuration=None):  # noqa: E501
        """VCloudClient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._org_name = None
        self._vdc_name = None
        self.discriminator = None

        if org_name is not None:
            self.org_name = org_name
        if vdc_name is not None:
            self.vdc_name = vdc_name

    @property
    def org_name(self):
        """Gets the org_name of this VCloudClient.  # noqa: E501


        :return: The org_name of this VCloudClient.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this VCloudClient.


        :param org_name: The org_name of this VCloudClient.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def vdc_name(self):
        """Gets the vdc_name of this VCloudClient.  # noqa: E501


        :return: The vdc_name of this VCloudClient.  # noqa: E501
        :rtype: str
        """
        return self._vdc_name

    @vdc_name.setter
    def vdc_name(self, vdc_name):
        """Sets the vdc_name of this VCloudClient.


        :param vdc_name: The vdc_name of this VCloudClient.  # noqa: E501
        :type: str
        """

        self._vdc_name = vdc_name

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
        if not isinstance(other, VCloudClient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VCloudClient):
            return True

        return self.to_dict() != other.to_dict()
