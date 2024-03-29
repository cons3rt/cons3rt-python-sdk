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


class PhysicalHost(object):
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
        'physical_machine': 'PhysicalMachine',
        'ip_address': 'str',
        'mac_address': 'str',
        'hostname': 'str'
    }

    attribute_map = {
        'physical_machine': 'physicalMachine',
        'ip_address': 'ipAddress',
        'mac_address': 'macAddress',
        'hostname': 'hostname'
    }

    def __init__(self, physical_machine=None, ip_address=None, mac_address=None, hostname=None, local_vars_configuration=None):  # noqa: E501
        """PhysicalHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._physical_machine = None
        self._ip_address = None
        self._mac_address = None
        self._hostname = None
        self.discriminator = None

        if physical_machine is not None:
            self.physical_machine = physical_machine
        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address
        if hostname is not None:
            self.hostname = hostname

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
