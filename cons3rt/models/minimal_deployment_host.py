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


class MinimalDeploymentHost(object):
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
        'additional_disks': 'list[FullDisk]',
        'id': 'int',
        'num_cpus': 'int',
        'ram': 'int',
        'build_order': 'int',
        'system_module': 'MinimalSystemModule',
        'system_role': 'str'
    }

    attribute_map = {
        'additional_disks': 'additionalDisks',
        'id': 'id',
        'num_cpus': 'numCpus',
        'ram': 'ram',
        'build_order': 'buildOrder',
        'system_module': 'systemModule',
        'system_role': 'systemRole'
    }

    def __init__(self, additional_disks=None, id=None, num_cpus=None, ram=None, build_order=None, system_module=None, system_role=None, local_vars_configuration=None):  # noqa: E501
        """MinimalDeploymentHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_disks = None
        self._id = None
        self._num_cpus = None
        self._ram = None
        self._build_order = None
        self._system_module = None
        self._system_role = None
        self.discriminator = None

        if additional_disks is not None:
            self.additional_disks = additional_disks
        if id is not None:
            self.id = id
        if num_cpus is not None:
            self.num_cpus = num_cpus
        if ram is not None:
            self.ram = ram
        if build_order is not None:
            self.build_order = build_order
        if system_module is not None:
            self.system_module = system_module
        if system_role is not None:
            self.system_role = system_role

    @property
    def additional_disks(self):
        """Gets the additional_disks of this MinimalDeploymentHost.  # noqa: E501


        :return: The additional_disks of this MinimalDeploymentHost.  # noqa: E501
        :rtype: list[FullDisk]
        """
        return self._additional_disks

    @additional_disks.setter
    def additional_disks(self, additional_disks):
        """Sets the additional_disks of this MinimalDeploymentHost.


        :param additional_disks: The additional_disks of this MinimalDeploymentHost.  # noqa: E501
        :type: list[FullDisk]
        """

        self._additional_disks = additional_disks

    @property
    def id(self):
        """Gets the id of this MinimalDeploymentHost.  # noqa: E501


        :return: The id of this MinimalDeploymentHost.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalDeploymentHost.


        :param id: The id of this MinimalDeploymentHost.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def num_cpus(self):
        """Gets the num_cpus of this MinimalDeploymentHost.  # noqa: E501


        :return: The num_cpus of this MinimalDeploymentHost.  # noqa: E501
        :rtype: int
        """
        return self._num_cpus

    @num_cpus.setter
    def num_cpus(self, num_cpus):
        """Sets the num_cpus of this MinimalDeploymentHost.


        :param num_cpus: The num_cpus of this MinimalDeploymentHost.  # noqa: E501
        :type: int
        """

        self._num_cpus = num_cpus

    @property
    def ram(self):
        """Gets the ram of this MinimalDeploymentHost.  # noqa: E501


        :return: The ram of this MinimalDeploymentHost.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this MinimalDeploymentHost.


        :param ram: The ram of this MinimalDeploymentHost.  # noqa: E501
        :type: int
        """

        self._ram = ram

    @property
    def build_order(self):
        """Gets the build_order of this MinimalDeploymentHost.  # noqa: E501


        :return: The build_order of this MinimalDeploymentHost.  # noqa: E501
        :rtype: int
        """
        return self._build_order

    @build_order.setter
    def build_order(self, build_order):
        """Sets the build_order of this MinimalDeploymentHost.


        :param build_order: The build_order of this MinimalDeploymentHost.  # noqa: E501
        :type: int
        """

        self._build_order = build_order

    @property
    def system_module(self):
        """Gets the system_module of this MinimalDeploymentHost.  # noqa: E501


        :return: The system_module of this MinimalDeploymentHost.  # noqa: E501
        :rtype: MinimalSystemModule
        """
        return self._system_module

    @system_module.setter
    def system_module(self, system_module):
        """Sets the system_module of this MinimalDeploymentHost.


        :param system_module: The system_module of this MinimalDeploymentHost.  # noqa: E501
        :type: MinimalSystemModule
        """

        self._system_module = system_module

    @property
    def system_role(self):
        """Gets the system_role of this MinimalDeploymentHost.  # noqa: E501


        :return: The system_role of this MinimalDeploymentHost.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this MinimalDeploymentHost.


        :param system_role: The system_role of this MinimalDeploymentHost.  # noqa: E501
        :type: str
        """

        self._system_role = system_role

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
        if not isinstance(other, MinimalDeploymentHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalDeploymentHost):
            return True

        return self.to_dict() != other.to_dict()
