# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class OpenStackCloudSpaceRequest(object):
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
        'external_network_name': 'str',
        'dns_server_ip_addresses': 'str'
    }

    attribute_map = {
        'external_network_name': 'externalNetworkName',
        'dns_server_ip_addresses': 'dnsServerIpAddresses'
    }

    def __init__(self, external_network_name=None, dns_server_ip_addresses=None, local_vars_configuration=None):  # noqa: E501
        """OpenStackCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._external_network_name = None
        self._dns_server_ip_addresses = None
        self.discriminator = None

        self.external_network_name = external_network_name
        if dns_server_ip_addresses is not None:
            self.dns_server_ip_addresses = dns_server_ip_addresses

    @property
    def external_network_name(self):
        """Gets the external_network_name of this OpenStackCloudSpaceRequest.  # noqa: E501


        :return: The external_network_name of this OpenStackCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_network_name

    @external_network_name.setter
    def external_network_name(self, external_network_name):
        """Sets the external_network_name of this OpenStackCloudSpaceRequest.


        :param external_network_name: The external_network_name of this OpenStackCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_network_name is None:  # noqa: E501
            raise ValueError("Invalid value for `external_network_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_network_name is not None and len(external_network_name) > 255):
            raise ValueError("Invalid value for `external_network_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_network_name is not None and len(external_network_name) < 1):
            raise ValueError("Invalid value for `external_network_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._external_network_name = external_network_name

    @property
    def dns_server_ip_addresses(self):
        """Gets the dns_server_ip_addresses of this OpenStackCloudSpaceRequest.  # noqa: E501


        :return: The dns_server_ip_addresses of this OpenStackCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._dns_server_ip_addresses

    @dns_server_ip_addresses.setter
    def dns_server_ip_addresses(self, dns_server_ip_addresses):
        """Sets the dns_server_ip_addresses of this OpenStackCloudSpaceRequest.


        :param dns_server_ip_addresses: The dns_server_ip_addresses of this OpenStackCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._dns_server_ip_addresses = dns_server_ip_addresses

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
        if not isinstance(other, OpenStackCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenStackCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
