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


class BasicPhysicalMachineAllOf(object):
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
        'architecture': 'str',
        'bits': 'str',
        'operating_system': 'str'
    }

    attribute_map = {
        'architecture': 'architecture',
        'bits': 'bits',
        'operating_system': 'operatingSystem'
    }

    def __init__(self, architecture=None, bits=None, operating_system=None, local_vars_configuration=None):  # noqa: E501
        """BasicPhysicalMachineAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._architecture = None
        self._bits = None
        self._operating_system = None
        self.discriminator = None

        if architecture is not None:
            self.architecture = architecture
        if bits is not None:
            self.bits = bits
        if operating_system is not None:
            self.operating_system = operating_system

    @property
    def architecture(self):
        """Gets the architecture of this BasicPhysicalMachineAllOf.  # noqa: E501


        :return: The architecture of this BasicPhysicalMachineAllOf.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this BasicPhysicalMachineAllOf.


        :param architecture: The architecture of this BasicPhysicalMachineAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["X86", "X64", "ARM", "SPARC", "PPCLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and architecture not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `architecture` ({0}), must be one of {1}"  # noqa: E501
                .format(architecture, allowed_values)
            )

        self._architecture = architecture

    @property
    def bits(self):
        """Gets the bits of this BasicPhysicalMachineAllOf.  # noqa: E501


        :return: The bits of this BasicPhysicalMachineAllOf.  # noqa: E501
        :rtype: str
        """
        return self._bits

    @bits.setter
    def bits(self, bits):
        """Sets the bits of this BasicPhysicalMachineAllOf.


        :param bits: The bits of this BasicPhysicalMachineAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["BITS32", "BITS64"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and bits not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `bits` ({0}), must be one of {1}"  # noqa: E501
                .format(bits, allowed_values)
            )

        self._bits = bits

    @property
    def operating_system(self):
        """Gets the operating_system of this BasicPhysicalMachineAllOf.  # noqa: E501


        :return: The operating_system of this BasicPhysicalMachineAllOf.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this BasicPhysicalMachineAllOf.


        :param operating_system: The operating_system of this BasicPhysicalMachineAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["AMAZON_LINUX_LATEST_X64", "CENTOS_6_X64", "CENTOS_6_X86", "CENTOS_7_X64", "CORE_OS_1221_X64", "F5_BIGIP_X64", "FORTISIEM", "PALO_ALTO_NETWORKS_PAN_OS_X64", "FEDORA_23_X64", "GENERIC_LINUX_X64", "GENERIC_WINDOWS_X64", "KALI_ROLLING_X64", "ORACLE_LINUX_6_X64", "ORACLE_LINUX_7_X64", "OS_X_10", "OS_X_11", "RASPBIAN", "RHEL_5_X64", "RHEL_5_X86", "RHEL_6_X64", "RHEL_6_X86", "RHEL_7_ATOMIC_HOST", "RHEL_7_PPCLE", "RHEL_7_X64", "SOLARIS_11_X64", "UBUNTU_12_X64", "UBUNTU_14_X64", "UBUNTU_16_X64", "UBUNTU_18_X64", "UBUNTU_CORE", "VYOS_117_X64", "VYOS_118_X64", "WINDOWS_10_X64", "WINDOWS_7_X64", "WINDOWS_7_X86", "WINDOWS_8_X64", "WINDOWS_SERVER_2008_R2_X64", "WINDOWS_SERVER_2008_X64", "WINDOWS_SERVER_2012_R2_X64", "WINDOWS_SERVER_2012_X64", "WINDOWS_SERVER_2016_X64", "WINDOWS_SERVER_2019_X64", "WINDOWS_XP_X86"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operating_system not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

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
        if not isinstance(other, BasicPhysicalMachineAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicPhysicalMachineAllOf):
            return True

        return self.to_dict() != other.to_dict()
