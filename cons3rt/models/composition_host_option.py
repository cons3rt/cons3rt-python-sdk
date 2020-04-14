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


class CompositionHostOption(object):
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
        'additional_disks': 'list[Disk]',
        'batch_software_install': 'bool',
        'instance_type_name': 'str',
        'network_interfaces': 'list[NetworkInterface]',
        'cpus': 'int',
        'ram': 'int',
        'system_role': 'str',
        'template_name': 'str'
    }

    attribute_map = {
        'additional_disks': 'additionalDisks',
        'batch_software_install': 'batchSoftwareInstall',
        'instance_type_name': 'instanceTypeName',
        'network_interfaces': 'networkInterfaces',
        'cpus': 'cpus',
        'ram': 'ram',
        'system_role': 'systemRole',
        'template_name': 'templateName'
    }

    def __init__(self, additional_disks=None, batch_software_install=None, instance_type_name=None, network_interfaces=None, cpus=None, ram=None, system_role=None, template_name=None, local_vars_configuration=None):  # noqa: E501
        """CompositionHostOption - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_disks = None
        self._batch_software_install = None
        self._instance_type_name = None
        self._network_interfaces = None
        self._cpus = None
        self._ram = None
        self._system_role = None
        self._template_name = None
        self.discriminator = None

        if additional_disks is not None:
            self.additional_disks = additional_disks
        if batch_software_install is not None:
            self.batch_software_install = batch_software_install
        if instance_type_name is not None:
            self.instance_type_name = instance_type_name
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if cpus is not None:
            self.cpus = cpus
        if ram is not None:
            self.ram = ram
        self.system_role = system_role
        if template_name is not None:
            self.template_name = template_name

    @property
    def additional_disks(self):
        """Gets the additional_disks of this CompositionHostOption.  # noqa: E501


        :return: The additional_disks of this CompositionHostOption.  # noqa: E501
        :rtype: list[Disk]
        """
        return self._additional_disks

    @additional_disks.setter
    def additional_disks(self, additional_disks):
        """Sets the additional_disks of this CompositionHostOption.


        :param additional_disks: The additional_disks of this CompositionHostOption.  # noqa: E501
        :type: list[Disk]
        """

        self._additional_disks = additional_disks

    @property
    def batch_software_install(self):
        """Gets the batch_software_install of this CompositionHostOption.  # noqa: E501


        :return: The batch_software_install of this CompositionHostOption.  # noqa: E501
        :rtype: bool
        """
        return self._batch_software_install

    @batch_software_install.setter
    def batch_software_install(self, batch_software_install):
        """Sets the batch_software_install of this CompositionHostOption.


        :param batch_software_install: The batch_software_install of this CompositionHostOption.  # noqa: E501
        :type: bool
        """

        self._batch_software_install = batch_software_install

    @property
    def instance_type_name(self):
        """Gets the instance_type_name of this CompositionHostOption.  # noqa: E501


        :return: The instance_type_name of this CompositionHostOption.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_name

    @instance_type_name.setter
    def instance_type_name(self, instance_type_name):
        """Sets the instance_type_name of this CompositionHostOption.


        :param instance_type_name: The instance_type_name of this CompositionHostOption.  # noqa: E501
        :type: str
        """

        self._instance_type_name = instance_type_name

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this CompositionHostOption.  # noqa: E501


        :return: The network_interfaces of this CompositionHostOption.  # noqa: E501
        :rtype: list[NetworkInterface]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this CompositionHostOption.


        :param network_interfaces: The network_interfaces of this CompositionHostOption.  # noqa: E501
        :type: list[NetworkInterface]
        """

        self._network_interfaces = network_interfaces

    @property
    def cpus(self):
        """Gets the cpus of this CompositionHostOption.  # noqa: E501


        :return: The cpus of this CompositionHostOption.  # noqa: E501
        :rtype: int
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus):
        """Sets the cpus of this CompositionHostOption.


        :param cpus: The cpus of this CompositionHostOption.  # noqa: E501
        :type: int
        """

        self._cpus = cpus

    @property
    def ram(self):
        """Gets the ram of this CompositionHostOption.  # noqa: E501


        :return: The ram of this CompositionHostOption.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this CompositionHostOption.


        :param ram: The ram of this CompositionHostOption.  # noqa: E501
        :type: int
        """

        self._ram = ram

    @property
    def system_role(self):
        """Gets the system_role of this CompositionHostOption.  # noqa: E501


        :return: The system_role of this CompositionHostOption.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this CompositionHostOption.


        :param system_role: The system_role of this CompositionHostOption.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_role is None:  # noqa: E501
            raise ValueError("Invalid value for `system_role`, must not be `None`")  # noqa: E501

        self._system_role = system_role

    @property
    def template_name(self):
        """Gets the template_name of this CompositionHostOption.  # noqa: E501


        :return: The template_name of this CompositionHostOption.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this CompositionHostOption.


        :param template_name: The template_name of this CompositionHostOption.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

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
        if not isinstance(other, CompositionHostOption):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CompositionHostOption):
            return True

        return self.to_dict() != other.to_dict()
