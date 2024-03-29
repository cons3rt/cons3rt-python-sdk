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


class InputTemplateProfile(object):
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
        'virt_realm_template_name': 'str',
        'operating_system': 'str',
        'min_num_cpus': 'int',
        'min_ram': 'int',
        'vgpu_required': 'bool',
        'requires_nested_virtualization': 'bool',
        'additional_disks': 'list[InputDisk]',
        'min_boot_disk_capacity': 'int',
        'remote_access_required': 'bool',
        'virt_realm_id': 'int'
    }

    attribute_map = {
        'virt_realm_template_name': 'virtRealmTemplateName',
        'operating_system': 'operatingSystem',
        'min_num_cpus': 'minNumCpus',
        'min_ram': 'minRam',
        'vgpu_required': 'vgpuRequired',
        'requires_nested_virtualization': 'requiresNestedVirtualization',
        'additional_disks': 'additionalDisks',
        'min_boot_disk_capacity': 'minBootDiskCapacity',
        'remote_access_required': 'remoteAccessRequired',
        'virt_realm_id': 'virtRealmId'
    }

    def __init__(self, virt_realm_template_name=None, operating_system=None, min_num_cpus=None, min_ram=None, vgpu_required=None, requires_nested_virtualization=None, additional_disks=None, min_boot_disk_capacity=None, remote_access_required=None, virt_realm_id=None, local_vars_configuration=None):  # noqa: E501
        """InputTemplateProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._virt_realm_template_name = None
        self._operating_system = None
        self._min_num_cpus = None
        self._min_ram = None
        self._vgpu_required = None
        self._requires_nested_virtualization = None
        self._additional_disks = None
        self._min_boot_disk_capacity = None
        self._remote_access_required = None
        self._virt_realm_id = None
        self.discriminator = None

        if virt_realm_template_name is not None:
            self.virt_realm_template_name = virt_realm_template_name
        if operating_system is not None:
            self.operating_system = operating_system
        self.min_num_cpus = min_num_cpus
        self.min_ram = min_ram
        if vgpu_required is not None:
            self.vgpu_required = vgpu_required
        if requires_nested_virtualization is not None:
            self.requires_nested_virtualization = requires_nested_virtualization
        if additional_disks is not None:
            self.additional_disks = additional_disks
        if min_boot_disk_capacity is not None:
            self.min_boot_disk_capacity = min_boot_disk_capacity
        if remote_access_required is not None:
            self.remote_access_required = remote_access_required
        if virt_realm_id is not None:
            self.virt_realm_id = virt_realm_id

    @property
    def virt_realm_template_name(self):
        """Gets the virt_realm_template_name of this InputTemplateProfile.  # noqa: E501


        :return: The virt_realm_template_name of this InputTemplateProfile.  # noqa: E501
        :rtype: str
        """
        return self._virt_realm_template_name

    @virt_realm_template_name.setter
    def virt_realm_template_name(self, virt_realm_template_name):
        """Sets the virt_realm_template_name of this InputTemplateProfile.


        :param virt_realm_template_name: The virt_realm_template_name of this InputTemplateProfile.  # noqa: E501
        :type: str
        """

        self._virt_realm_template_name = virt_realm_template_name

    @property
    def operating_system(self):
        """Gets the operating_system of this InputTemplateProfile.  # noqa: E501


        :return: The operating_system of this InputTemplateProfile.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this InputTemplateProfile.


        :param operating_system: The operating_system of this InputTemplateProfile.  # noqa: E501
        :type: str
        """
        allowed_values = ["AMAZON_LINUX_2_LATEST_X64", "AMAZON_LINUX_LATEST_X64", "CENTOS_6_X64", "CENTOS_6_X86", "CENTOS_7_X64", "CENTOS_8_X64", "CORE_OS_1221_X64", "F5_BIGIP_X64", "FEDORA_23_X64", "FORTISIEM", "GENERIC_LINUX_X64", "GENERIC_WINDOWS_X64", "KALI_ROLLING_X64", "ORACLE_LINUX_6_X64", "ORACLE_LINUX_7_X64", "ORACLE_LINUX_8_X64", "OS_X_10", "OS_X_11", "PALO_ALTO_NETWORKS_PAN_OS_X64", "RASPBIAN", "RHEL_5_X64", "RHEL_5_X86", "RHEL_6_X64", "RHEL_6_X86", "RHEL_7_ATOMIC_HOST", "RHEL_7_PPCLE", "RHEL_7_X64", "RHEL_8_X64", "SOLARIS_11_X64", "UBUNTU_12_X64", "UBUNTU_14_X64", "UBUNTU_16_X64", "UBUNTU_18_X64", "UBUNTU_20_X64", "UBUNTU_CORE", "VYOS_1_1_X64", "VYOS_1_2_X64", "VYOS_1_3_X64", "VYOS_ROLLING_X64", "WINDOWS_10_X64", "WINDOWS_7_X64", "WINDOWS_7_X86", "WINDOWS_8_X64", "WINDOWS_SERVER_2008_R2_X64", "WINDOWS_SERVER_2008_X64", "WINDOWS_SERVER_2012_R2_X64", "WINDOWS_SERVER_2012_X64", "WINDOWS_SERVER_2016_X64", "WINDOWS_SERVER_2019_X64", "WINDOWS_SERVER_2019_CORE_X64", "WINDOWS_XP_X86"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operating_system not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

    @property
    def min_num_cpus(self):
        """Gets the min_num_cpus of this InputTemplateProfile.  # noqa: E501


        :return: The min_num_cpus of this InputTemplateProfile.  # noqa: E501
        :rtype: int
        """
        return self._min_num_cpus

    @min_num_cpus.setter
    def min_num_cpus(self, min_num_cpus):
        """Sets the min_num_cpus of this InputTemplateProfile.


        :param min_num_cpus: The min_num_cpus of this InputTemplateProfile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and min_num_cpus is None:  # noqa: E501
            raise ValueError("Invalid value for `min_num_cpus`, must not be `None`")  # noqa: E501

        self._min_num_cpus = min_num_cpus

    @property
    def min_ram(self):
        """Gets the min_ram of this InputTemplateProfile.  # noqa: E501


        :return: The min_ram of this InputTemplateProfile.  # noqa: E501
        :rtype: int
        """
        return self._min_ram

    @min_ram.setter
    def min_ram(self, min_ram):
        """Sets the min_ram of this InputTemplateProfile.


        :param min_ram: The min_ram of this InputTemplateProfile.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and min_ram is None:  # noqa: E501
            raise ValueError("Invalid value for `min_ram`, must not be `None`")  # noqa: E501

        self._min_ram = min_ram

    @property
    def vgpu_required(self):
        """Gets the vgpu_required of this InputTemplateProfile.  # noqa: E501


        :return: The vgpu_required of this InputTemplateProfile.  # noqa: E501
        :rtype: bool
        """
        return self._vgpu_required

    @vgpu_required.setter
    def vgpu_required(self, vgpu_required):
        """Sets the vgpu_required of this InputTemplateProfile.


        :param vgpu_required: The vgpu_required of this InputTemplateProfile.  # noqa: E501
        :type: bool
        """

        self._vgpu_required = vgpu_required

    @property
    def requires_nested_virtualization(self):
        """Gets the requires_nested_virtualization of this InputTemplateProfile.  # noqa: E501


        :return: The requires_nested_virtualization of this InputTemplateProfile.  # noqa: E501
        :rtype: bool
        """
        return self._requires_nested_virtualization

    @requires_nested_virtualization.setter
    def requires_nested_virtualization(self, requires_nested_virtualization):
        """Sets the requires_nested_virtualization of this InputTemplateProfile.


        :param requires_nested_virtualization: The requires_nested_virtualization of this InputTemplateProfile.  # noqa: E501
        :type: bool
        """

        self._requires_nested_virtualization = requires_nested_virtualization

    @property
    def additional_disks(self):
        """Gets the additional_disks of this InputTemplateProfile.  # noqa: E501


        :return: The additional_disks of this InputTemplateProfile.  # noqa: E501
        :rtype: list[InputDisk]
        """
        return self._additional_disks

    @additional_disks.setter
    def additional_disks(self, additional_disks):
        """Sets the additional_disks of this InputTemplateProfile.


        :param additional_disks: The additional_disks of this InputTemplateProfile.  # noqa: E501
        :type: list[InputDisk]
        """

        self._additional_disks = additional_disks

    @property
    def min_boot_disk_capacity(self):
        """Gets the min_boot_disk_capacity of this InputTemplateProfile.  # noqa: E501


        :return: The min_boot_disk_capacity of this InputTemplateProfile.  # noqa: E501
        :rtype: int
        """
        return self._min_boot_disk_capacity

    @min_boot_disk_capacity.setter
    def min_boot_disk_capacity(self, min_boot_disk_capacity):
        """Sets the min_boot_disk_capacity of this InputTemplateProfile.


        :param min_boot_disk_capacity: The min_boot_disk_capacity of this InputTemplateProfile.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                min_boot_disk_capacity is not None and min_boot_disk_capacity > 1000000):  # noqa: E501
            raise ValueError("Invalid value for `min_boot_disk_capacity`, must be a value less than or equal to `1000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_boot_disk_capacity is not None and min_boot_disk_capacity < 10000):  # noqa: E501
            raise ValueError("Invalid value for `min_boot_disk_capacity`, must be a value greater than or equal to `10000`")  # noqa: E501

        self._min_boot_disk_capacity = min_boot_disk_capacity

    @property
    def remote_access_required(self):
        """Gets the remote_access_required of this InputTemplateProfile.  # noqa: E501


        :return: The remote_access_required of this InputTemplateProfile.  # noqa: E501
        :rtype: bool
        """
        return self._remote_access_required

    @remote_access_required.setter
    def remote_access_required(self, remote_access_required):
        """Sets the remote_access_required of this InputTemplateProfile.


        :param remote_access_required: The remote_access_required of this InputTemplateProfile.  # noqa: E501
        :type: bool
        """

        self._remote_access_required = remote_access_required

    @property
    def virt_realm_id(self):
        """Gets the virt_realm_id of this InputTemplateProfile.  # noqa: E501


        :return: The virt_realm_id of this InputTemplateProfile.  # noqa: E501
        :rtype: int
        """
        return self._virt_realm_id

    @virt_realm_id.setter
    def virt_realm_id(self, virt_realm_id):
        """Sets the virt_realm_id of this InputTemplateProfile.


        :param virt_realm_id: The virt_realm_id of this InputTemplateProfile.  # noqa: E501
        :type: int
        """

        self._virt_realm_id = virt_realm_id

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
        if not isinstance(other, InputTemplateProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputTemplateProfile):
            return True

        return self.to_dict() != other.to_dict()
