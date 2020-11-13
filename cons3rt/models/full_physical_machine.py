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


class FullPhysicalMachine(object):
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
        'host_name': 'str',
        'ip_address': 'str',
        'mac_address': 'str',
        'cpu_count': 'int',
        'ram': 'int',
        'architecture': 'str',
        'bits': 'str',
        'operating_system': 'str',
        'remote_access_capable': 'bool',
        'remote_access_templates': 'list[MinimalRemoteAccessTemplate]',
        'base_disks': 'list[FullDisk]'
    }

    attribute_map = {
        'host_name': 'hostName',
        'ip_address': 'ipAddress',
        'mac_address': 'macAddress',
        'cpu_count': 'cpuCount',
        'ram': 'ram',
        'architecture': 'architecture',
        'bits': 'bits',
        'operating_system': 'operatingSystem',
        'remote_access_capable': 'remoteAccessCapable',
        'remote_access_templates': 'remoteAccessTemplates',
        'base_disks': 'baseDisks'
    }

    def __init__(self, host_name=None, ip_address=None, mac_address=None, cpu_count=None, ram=None, architecture=None, bits=None, operating_system=None, remote_access_capable=None, remote_access_templates=None, base_disks=None, local_vars_configuration=None):  # noqa: E501
        """FullPhysicalMachine - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host_name = None
        self._ip_address = None
        self._mac_address = None
        self._cpu_count = None
        self._ram = None
        self._architecture = None
        self._bits = None
        self._operating_system = None
        self._remote_access_capable = None
        self._remote_access_templates = None
        self._base_disks = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address
        if cpu_count is not None:
            self.cpu_count = cpu_count
        if ram is not None:
            self.ram = ram
        if architecture is not None:
            self.architecture = architecture
        if bits is not None:
            self.bits = bits
        if operating_system is not None:
            self.operating_system = operating_system
        if remote_access_capable is not None:
            self.remote_access_capable = remote_access_capable
        if remote_access_templates is not None:
            self.remote_access_templates = remote_access_templates
        if base_disks is not None:
            self.base_disks = base_disks

    @property
    def host_name(self):
        """Gets the host_name of this FullPhysicalMachine.  # noqa: E501


        :return: The host_name of this FullPhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this FullPhysicalMachine.


        :param host_name: The host_name of this FullPhysicalMachine.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def ip_address(self):
        """Gets the ip_address of this FullPhysicalMachine.  # noqa: E501


        :return: The ip_address of this FullPhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this FullPhysicalMachine.


        :param ip_address: The ip_address of this FullPhysicalMachine.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this FullPhysicalMachine.  # noqa: E501


        :return: The mac_address of this FullPhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this FullPhysicalMachine.


        :param mac_address: The mac_address of this FullPhysicalMachine.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def cpu_count(self):
        """Gets the cpu_count of this FullPhysicalMachine.  # noqa: E501


        :return: The cpu_count of this FullPhysicalMachine.  # noqa: E501
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """Sets the cpu_count of this FullPhysicalMachine.


        :param cpu_count: The cpu_count of this FullPhysicalMachine.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cpu_count is not None and cpu_count < 1):  # noqa: E501
            raise ValueError("Invalid value for `cpu_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cpu_count = cpu_count

    @property
    def ram(self):
        """Gets the ram of this FullPhysicalMachine.  # noqa: E501


        :return: The ram of this FullPhysicalMachine.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this FullPhysicalMachine.


        :param ram: The ram of this FullPhysicalMachine.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < 1):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `1`")  # noqa: E501

        self._ram = ram

    @property
    def architecture(self):
        """Gets the architecture of this FullPhysicalMachine.  # noqa: E501


        :return: The architecture of this FullPhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this FullPhysicalMachine.


        :param architecture: The architecture of this FullPhysicalMachine.  # noqa: E501
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
        """Gets the bits of this FullPhysicalMachine.  # noqa: E501


        :return: The bits of this FullPhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._bits

    @bits.setter
    def bits(self, bits):
        """Sets the bits of this FullPhysicalMachine.


        :param bits: The bits of this FullPhysicalMachine.  # noqa: E501
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
        """Gets the operating_system of this FullPhysicalMachine.  # noqa: E501


        :return: The operating_system of this FullPhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this FullPhysicalMachine.


        :param operating_system: The operating_system of this FullPhysicalMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["AMAZON_LINUX_2_LATEST_X64", "AMAZON_LINUX_LATEST_X64", "CENTOS_6_X64", "CENTOS_6_X86", "CENTOS_7_X64", "CENTOS_8_X64", "CORE_OS_1221_X64", "F5_BIGIP_X64", "FEDORA_23_X64", "FORTISIEM", "GENERIC_LINUX_X64", "GENERIC_WINDOWS_X64", "KALI_ROLLING_X64", "ORACLE_LINUX_6_X64", "ORACLE_LINUX_7_X64", "ORACLE_LINUX_8_X64", "OS_X_10", "OS_X_11", "PALO_ALTO_NETWORKS_PAN_OS_X64", "RASPBIAN", "RHEL_5_X64", "RHEL_5_X86", "RHEL_6_X64", "RHEL_6_X86", "RHEL_7_ATOMIC_HOST", "RHEL_7_PPCLE", "RHEL_7_X64", "RHEL_8_X64", "SOLARIS_11_X64", "UBUNTU_12_X64", "UBUNTU_14_X64", "UBUNTU_16_X64", "UBUNTU_18_X64", "UBUNTU_20_X64", "UBUNTU_CORE", "VYOS_1_1_X64", "VYOS_1_2_X64", "VYOS_1_3_X64", "WINDOWS_10_X64", "WINDOWS_7_X64", "WINDOWS_7_X86", "WINDOWS_8_X64", "WINDOWS_SERVER_2008_R2_X64", "WINDOWS_SERVER_2008_X64", "WINDOWS_SERVER_2012_R2_X64", "WINDOWS_SERVER_2012_X64", "WINDOWS_SERVER_2016_X64", "WINDOWS_SERVER_2019_X64", "WINDOWS_XP_X86"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operating_system not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

    @property
    def remote_access_capable(self):
        """Gets the remote_access_capable of this FullPhysicalMachine.  # noqa: E501


        :return: The remote_access_capable of this FullPhysicalMachine.  # noqa: E501
        :rtype: bool
        """
        return self._remote_access_capable

    @remote_access_capable.setter
    def remote_access_capable(self, remote_access_capable):
        """Sets the remote_access_capable of this FullPhysicalMachine.


        :param remote_access_capable: The remote_access_capable of this FullPhysicalMachine.  # noqa: E501
        :type: bool
        """

        self._remote_access_capable = remote_access_capable

    @property
    def remote_access_templates(self):
        """Gets the remote_access_templates of this FullPhysicalMachine.  # noqa: E501


        :return: The remote_access_templates of this FullPhysicalMachine.  # noqa: E501
        :rtype: list[MinimalRemoteAccessTemplate]
        """
        return self._remote_access_templates

    @remote_access_templates.setter
    def remote_access_templates(self, remote_access_templates):
        """Sets the remote_access_templates of this FullPhysicalMachine.


        :param remote_access_templates: The remote_access_templates of this FullPhysicalMachine.  # noqa: E501
        :type: list[MinimalRemoteAccessTemplate]
        """

        self._remote_access_templates = remote_access_templates

    @property
    def base_disks(self):
        """Gets the base_disks of this FullPhysicalMachine.  # noqa: E501


        :return: The base_disks of this FullPhysicalMachine.  # noqa: E501
        :rtype: list[FullDisk]
        """
        return self._base_disks

    @base_disks.setter
    def base_disks(self, base_disks):
        """Sets the base_disks of this FullPhysicalMachine.


        :param base_disks: The base_disks of this FullPhysicalMachine.  # noqa: E501
        :type: list[FullDisk]
        """

        self._base_disks = base_disks

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
        if not isinstance(other, FullPhysicalMachine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullPhysicalMachine):
            return True

        return self.to_dict() != other.to_dict()
