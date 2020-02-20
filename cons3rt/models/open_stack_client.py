# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class OpenStackClient(object):
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
        'keystone_version': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'keystone_version': 'keystoneVersion',
        'tenant_name': 'tenantName'
    }

    def __init__(self, keystone_version=None, tenant_name=None, local_vars_configuration=None):  # noqa: E501
        """OpenStackClient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._keystone_version = None
        self._tenant_name = None
        self.discriminator = None

        if keystone_version is not None:
            self.keystone_version = keystone_version
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def keystone_version(self):
        """Gets the keystone_version of this OpenStackClient.  # noqa: E501


        :return: The keystone_version of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._keystone_version

    @keystone_version.setter
    def keystone_version(self, keystone_version):
        """Sets the keystone_version of this OpenStackClient.


        :param keystone_version: The keystone_version of this OpenStackClient.  # noqa: E501
        :type: str
        """

        self._keystone_version = keystone_version

    @property
    def tenant_name(self):
        """Gets the tenant_name of this OpenStackClient.  # noqa: E501


        :return: The tenant_name of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this OpenStackClient.


        :param tenant_name: The tenant_name of this OpenStackClient.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

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
        if not isinstance(other, OpenStackClient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenStackClient):
            return True

        return self.to_dict() != other.to_dict()
