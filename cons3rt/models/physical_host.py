# coding: utf-8

"""
    CONS3RT API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@cons3rt.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class PhysicalHost(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'physical_machine': 'PhysicalMachine',
        'hostname': 'str',
        'ip_address': 'str',
        'mac_address': 'str'
    }

    attribute_map = {
        'physical_machine': 'physicalMachine',
        'hostname': 'hostname',
        'ip_address': 'ipAddress',
        'mac_address': 'macAddress'
    }

    def __init__(self, physical_machine=None, hostname=None, ip_address=None, mac_address=None, local_vars_configuration=None):  # noqa: E501
        """PhysicalHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._physical_machine = None
        self._hostname = None
        self._ip_address = None
        self._mac_address = None
        self.discriminator = None

        if physical_machine is not None:
            self.physical_machine = physical_machine
        if hostname is not None:
            self.hostname = hostname
        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address

    @property
    def physical_machine(self):
        """Gets the physical_machine of this PhysicalHost.  # noqa: E501


        :return: The physical_machine of this PhysicalHost.  # noqa: E501
        :rtype: PhysicalMachine
        """
        return self._physical_machine

    @physical_machine.setter
    def physical_machine(self, physical_machine):
        """Sets the physical_machine of this PhysicalHost.


        :param physical_machine: The physical_machine of this PhysicalHost.  # noqa: E501
        :type: PhysicalMachine
        """

        self._physical_machine = physical_machine

    @property
    def hostname(self):
        """Gets the hostname of this PhysicalHost.  # noqa: E501


        :return: The hostname of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PhysicalHost.


        :param hostname: The hostname of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def ip_address(self):
        """Gets the ip_address of this PhysicalHost.  # noqa: E501


        :return: The ip_address of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PhysicalHost.


        :param ip_address: The ip_address of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this PhysicalHost.  # noqa: E501


        :return: The mac_address of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this PhysicalHost.


        :param mac_address: The mac_address of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

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
        if not isinstance(other, PhysicalHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhysicalHost):
            return True

        return self.to_dict() != other.to_dict()
