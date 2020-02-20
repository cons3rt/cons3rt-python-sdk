# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class NetworkInterface(object):
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
        'external_ip_address': 'str',
        'interface_name': 'str',
        'internal_ip_address': 'str',
        'network_function': 'str',
        'mac_address': 'str',
        'network_name': 'str',
        'network_identifier': 'str'
    }

    attribute_map = {
        'external_ip_address': 'externalIpAddress',
        'interface_name': 'interfaceName',
        'internal_ip_address': 'internalIpAddress',
        'network_function': 'networkFunction',
        'mac_address': 'macAddress',
        'network_name': 'networkName',
        'network_identifier': 'networkIdentifier'
    }

    def __init__(self, external_ip_address=None, interface_name=None, internal_ip_address=None, network_function=None, mac_address=None, network_name=None, network_identifier=None, local_vars_configuration=None):  # noqa: E501
        """NetworkInterface - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._external_ip_address = None
        self._interface_name = None
        self._internal_ip_address = None
        self._network_function = None
        self._mac_address = None
        self._network_name = None
        self._network_identifier = None
        self.discriminator = None

        if external_ip_address is not None:
            self.external_ip_address = external_ip_address
        if interface_name is not None:
            self.interface_name = interface_name
        if internal_ip_address is not None:
            self.internal_ip_address = internal_ip_address
        if network_function is not None:
            self.network_function = network_function
        if mac_address is not None:
            self.mac_address = mac_address
        if network_name is not None:
            self.network_name = network_name
        if network_identifier is not None:
            self.network_identifier = network_identifier

    @property
    def external_ip_address(self):
        """Gets the external_ip_address of this NetworkInterface.  # noqa: E501


        :return: The external_ip_address of this NetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_address

    @external_ip_address.setter
    def external_ip_address(self, external_ip_address):
        """Sets the external_ip_address of this NetworkInterface.


        :param external_ip_address: The external_ip_address of this NetworkInterface.  # noqa: E501
        :type: str
        """

        self._external_ip_address = external_ip_address

    @property
    def interface_name(self):
        """Gets the interface_name of this NetworkInterface.  # noqa: E501


        :return: The interface_name of this NetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this NetworkInterface.


        :param interface_name: The interface_name of this NetworkInterface.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

    @property
    def internal_ip_address(self):
        """Gets the internal_ip_address of this NetworkInterface.  # noqa: E501


        :return: The internal_ip_address of this NetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip_address

    @internal_ip_address.setter
    def internal_ip_address(self, internal_ip_address):
        """Sets the internal_ip_address of this NetworkInterface.


        :param internal_ip_address: The internal_ip_address of this NetworkInterface.  # noqa: E501
        :type: str
        """

        self._internal_ip_address = internal_ip_address

    @property
    def network_function(self):
        """Gets the network_function of this NetworkInterface.  # noqa: E501


        :return: The network_function of this NetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._network_function

    @network_function.setter
    def network_function(self, network_function):
        """Sets the network_function of this NetworkInterface.


        :param network_function: The network_function of this NetworkInterface.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONS3RT", "ADDITIONAL", "PRIMARY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and network_function not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `network_function` ({0}), must be one of {1}"  # noqa: E501
                .format(network_function, allowed_values)
            )

        self._network_function = network_function

    @property
    def mac_address(self):
        """Gets the mac_address of this NetworkInterface.  # noqa: E501


        :return: The mac_address of this NetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NetworkInterface.


        :param mac_address: The mac_address of this NetworkInterface.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def network_name(self):
        """Gets the network_name of this NetworkInterface.  # noqa: E501


        :return: The network_name of this NetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._network_name

    @network_name.setter
    def network_name(self, network_name):
        """Sets the network_name of this NetworkInterface.


        :param network_name: The network_name of this NetworkInterface.  # noqa: E501
        :type: str
        """

        self._network_name = network_name

    @property
    def network_identifier(self):
        """Gets the network_identifier of this NetworkInterface.  # noqa: E501


        :return: The network_identifier of this NetworkInterface.  # noqa: E501
        :rtype: str
        """
        return self._network_identifier

    @network_identifier.setter
    def network_identifier(self, network_identifier):
        """Sets the network_identifier of this NetworkInterface.


        :param network_identifier: The network_identifier of this NetworkInterface.  # noqa: E501
        :type: str
        """

        self._network_identifier = network_identifier

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
        if not isinstance(other, NetworkInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkInterface):
            return True

        return self.to_dict() != other.to_dict()
