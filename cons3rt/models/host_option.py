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


class HostOption(object):
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
        'system_role': 'str',
        'cpus': 'int',
        'ram': 'int',
        'additional_disks': 'list[Disk]',
        'network_interfaces': 'list[NetworkInterface]',
        'batch_software_install': 'bool',
        'gpu_profile': 'str',
        'gpu_type': 'str'
    }

    attribute_map = {
        'system_role': 'systemRole',
        'cpus': 'cpus',
        'ram': 'ram',
        'additional_disks': 'additionalDisks',
        'network_interfaces': 'networkInterfaces',
        'batch_software_install': 'batchSoftwareInstall',
        'gpu_profile': 'gpuProfile',
        'gpu_type': 'gpuType'
    }

    def __init__(self, system_role=None, cpus=None, ram=None, additional_disks=None, network_interfaces=None, batch_software_install=None, gpu_profile=None, gpu_type=None, local_vars_configuration=None):  # noqa: E501
        """HostOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_role = None
        self._cpus = None
        self._ram = None
        self._additional_disks = None
        self._network_interfaces = None
        self._batch_software_install = None
        self._gpu_profile = None
        self._gpu_type = None
        self.discriminator = None

        self.system_role = system_role
        if cpus is not None:
            self.cpus = cpus
        if ram is not None:
            self.ram = ram
        if additional_disks is not None:
            self.additional_disks = additional_disks
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if batch_software_install is not None:
            self.batch_software_install = batch_software_install
        if gpu_profile is not None:
            self.gpu_profile = gpu_profile
        if gpu_type is not None:
            self.gpu_type = gpu_type

    @property
    def system_role(self):
        """Gets the system_role of this HostOption.  # noqa: E501


        :return: The system_role of this HostOption.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this HostOption.


        :param system_role: The system_role of this HostOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_role is None:  # noqa: E501
            raise ValueError("Invalid value for `system_role`, must not be `None`")  # noqa: E501

        self._system_role = system_role

    @property
    def cpus(self):
        """Gets the cpus of this HostOption.  # noqa: E501


        :return: The cpus of this HostOption.  # noqa: E501
        :rtype: int
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this HostOption.


        :param cpus: The cpus of this HostOption.  # noqa: E501
        :type: int
        """

        self._cpus = cpus

    @property
    def ram(self):
        """Gets the ram of this HostOption.  # noqa: E501


        :return: The ram of this HostOption.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this HostOption.


        :param ram: The ram of this HostOption.  # noqa: E501
        :type: int
        """

        self._ram = ram

    @property
    def additional_disks(self):
        """Gets the additional_disks of this HostOption.  # noqa: E501


        :return: The additional_disks of this HostOption.  # noqa: E501
        :rtype: list[Disk]
        """
        return self._additional_disks

    @additional_disks.setter
    def additional_disks(self, additional_disks):
        """Sets the additional_disks of this HostOption.


        :param additional_disks: The additional_disks of this HostOption.  # noqa: E501
        :type: list[Disk]
        """

        self._additional_disks = additional_disks

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this HostOption.  # noqa: E501


        :return: The network_interfaces of this HostOption.  # noqa: E501
        :rtype: list[NetworkInterface]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this HostOption.


        :param network_interfaces: The network_interfaces of this HostOption.  # noqa: E501
        :type: list[NetworkInterface]
        """

        self._network_interfaces = network_interfaces

    @property
    def batch_software_install(self):
        """Gets the batch_software_install of this HostOption.  # noqa: E501


        :return: The batch_software_install of this HostOption.  # noqa: E501
        :rtype: bool
        """
        return self._batch_software_install

    @batch_software_install.setter
    def batch_software_install(self, batch_software_install):
        """Sets the batch_software_install of this HostOption.


        :param batch_software_install: The batch_software_install of this HostOption.  # noqa: E501
        :type: bool
        """

        self._batch_software_install = batch_software_install

    @property
    def gpu_profile(self):
        """Gets the gpu_profile of this HostOption.  # noqa: E501


        :return: The gpu_profile of this HostOption.  # noqa: E501
        :rtype: str
        """
        return self._gpu_profile

    @gpu_profile.setter
    def gpu_profile(self, gpu_profile):
        """Sets the gpu_profile of this HostOption.


        :param gpu_profile: The gpu_profile of this HostOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["M10_0Q", "M10_1Q", "M10_2Q", "M10_4Q", "V100D_2Q", "V100D_4Q"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and gpu_profile not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `gpu_profile` ({0}), must be one of {1}"  # noqa: E501
                .format(gpu_profile, allowed_values)
            )

        self._gpu_profile = gpu_profile

    @property
    def gpu_type(self):
        """Gets the gpu_type of this HostOption.  # noqa: E501


        :return: The gpu_type of this HostOption.  # noqa: E501
        :rtype: str
        """
        return self._gpu_type

    @gpu_type.setter
    def gpu_type(self, gpu_type):
        """Sets the gpu_type of this HostOption.


        :param gpu_type: The gpu_type of this HostOption.  # noqa: E501
        :type: str
        """
        allowed_values = ["K80", "M10", "M60", "P40", "T4", "V100D"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and gpu_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `gpu_type` ({0}), must be one of {1}"  # noqa: E501
                .format(gpu_type, allowed_values)
            )

        self._gpu_type = gpu_type

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
        if not isinstance(other, HostOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostOption):
            return True

        return self.to_dict() != other.to_dict()
