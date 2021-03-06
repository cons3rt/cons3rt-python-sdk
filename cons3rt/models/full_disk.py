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


class FullDisk(object):
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
        'create_order': 'int',
        'capacity_in_megabytes': 'int',
        'file_system_type': 'str',
        'mount_point': 'str',
        'name': 'str',
        'id': 'int',
        'is_additional_disk': 'bool',
        'is_boot_disk': 'bool'
    }

    attribute_map = {
        'create_order': 'createOrder',
        'capacity_in_megabytes': 'capacityInMegabytes',
        'file_system_type': 'fileSystemType',
        'mount_point': 'mountPoint',
        'name': 'name',
        'id': 'id',
        'is_additional_disk': 'isAdditionalDisk',
        'is_boot_disk': 'isBootDisk'
    }

    def __init__(self, create_order=None, capacity_in_megabytes=None, file_system_type=None, mount_point=None, name=None, id=None, is_additional_disk=None, is_boot_disk=None, local_vars_configuration=None):  # noqa: E501
        """FullDisk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._create_order = None
        self._capacity_in_megabytes = None
        self._file_system_type = None
        self._mount_point = None
        self._name = None
        self._id = None
        self._is_additional_disk = None
        self._is_boot_disk = None
        self.discriminator = None

        if create_order is not None:
            self.create_order = create_order
        if capacity_in_megabytes is not None:
            self.capacity_in_megabytes = capacity_in_megabytes
        if file_system_type is not None:
            self.file_system_type = file_system_type
        if mount_point is not None:
            self.mount_point = mount_point
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if is_additional_disk is not None:
            self.is_additional_disk = is_additional_disk
        if is_boot_disk is not None:
            self.is_boot_disk = is_boot_disk

    @property
    def create_order(self):
        """Gets the create_order of this FullDisk.  # noqa: E501


        :return: The create_order of this FullDisk.  # noqa: E501
        :rtype: int
        """
        return self._create_order

    @create_order.setter
    def create_order(self, create_order):
        """Sets the create_order of this FullDisk.


        :param create_order: The create_order of this FullDisk.  # noqa: E501
        :type: int
        """

        self._create_order = create_order

    @property
    def capacity_in_megabytes(self):
        """Gets the capacity_in_megabytes of this FullDisk.  # noqa: E501


        :return: The capacity_in_megabytes of this FullDisk.  # noqa: E501
        :rtype: int
        """
        return self._capacity_in_megabytes

    @capacity_in_megabytes.setter
    def capacity_in_megabytes(self, capacity_in_megabytes):
        """Sets the capacity_in_megabytes of this FullDisk.


        :param capacity_in_megabytes: The capacity_in_megabytes of this FullDisk.  # noqa: E501
        :type: int
        """

        self._capacity_in_megabytes = capacity_in_megabytes

    @property
    def file_system_type(self):
        """Gets the file_system_type of this FullDisk.  # noqa: E501


        :return: The file_system_type of this FullDisk.  # noqa: E501
        :rtype: str
        """
        return self._file_system_type

    @file_system_type.setter
    def file_system_type(self, file_system_type):
        """Sets the file_system_type of this FullDisk.


        :param file_system_type: The file_system_type of this FullDisk.  # noqa: E501
        :type: str
        """

        self._file_system_type = file_system_type

    @property
    def mount_point(self):
        """Gets the mount_point of this FullDisk.  # noqa: E501


        :return: The mount_point of this FullDisk.  # noqa: E501
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """Sets the mount_point of this FullDisk.


        :param mount_point: The mount_point of this FullDisk.  # noqa: E501
        :type: str
        """

        self._mount_point = mount_point

    @property
    def name(self):
        """Gets the name of this FullDisk.  # noqa: E501


        :return: The name of this FullDisk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FullDisk.


        :param name: The name of this FullDisk.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this FullDisk.  # noqa: E501


        :return: The id of this FullDisk.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FullDisk.


        :param id: The id of this FullDisk.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_additional_disk(self):
        """Gets the is_additional_disk of this FullDisk.  # noqa: E501


        :return: The is_additional_disk of this FullDisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_additional_disk

    @is_additional_disk.setter
    def is_additional_disk(self, is_additional_disk):
        """Sets the is_additional_disk of this FullDisk.


        :param is_additional_disk: The is_additional_disk of this FullDisk.  # noqa: E501
        :type: bool
        """

        self._is_additional_disk = is_additional_disk

    @property
    def is_boot_disk(self):
        """Gets the is_boot_disk of this FullDisk.  # noqa: E501


        :return: The is_boot_disk of this FullDisk.  # noqa: E501
        :rtype: bool
        """
        return self._is_boot_disk

    @is_boot_disk.setter
    def is_boot_disk(self, is_boot_disk):
        """Sets the is_boot_disk of this FullDisk.


        :param is_boot_disk: The is_boot_disk of this FullDisk.  # noqa: E501
        :type: bool
        """

        self._is_boot_disk = is_boot_disk

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
        if not isinstance(other, FullDisk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullDisk):
            return True

        return self.to_dict() != other.to_dict()
