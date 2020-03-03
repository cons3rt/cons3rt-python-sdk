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


class Disk(object):
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
        'additional_disk': 'bool',
        'boot_disk': 'bool',
        'capacity_in_megabytes': 'int',
        'create_order': 'int',
        'is_additional_disk': 'bool',
        'is_boot_disk': 'bool',
        'id': 'int'
    }

    attribute_map = {
        'additional_disk': 'additionalDisk',
        'boot_disk': 'bootDisk',
        'capacity_in_megabytes': 'capacityInMegabytes',
        'create_order': 'createOrder',
        'is_additional_disk': 'isAdditionalDisk',
        'is_boot_disk': 'isBootDisk',
        'id': 'id'
    }

    def __init__(self, additional_disk=None, boot_disk=None, capacity_in_megabytes=None, create_order=None, is_additional_disk=None, is_boot_disk=None, id=None, local_vars_configuration=None):  # noqa: E501
        """Disk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._additional_disk = None
        self._boot_disk = None
        self._capacity_in_megabytes = None
        self._create_order = None
        self._is_additional_disk = None
        self._is_boot_disk = None
        self._id = None
        self.discriminator = None

        if additional_disk is not None:
            self.additional_disk = additional_disk
        if boot_disk is not None:
            self.boot_disk = boot_disk
        self.capacity_in_megabytes = capacity_in_megabytes
        if create_order is not None:
            self.create_order = create_order
        if is_additional_disk is not None:
            self.is_additional_disk = is_additional_disk
        if is_boot_disk is not None:
            self.is_boot_disk = is_boot_disk
        if id is not None:
            self.id = id

    @property
    def additional_disk(self):
        """Gets the additional_disk of this Disk.  # noqa: E501


        :return: The additional_disk of this Disk.  # noqa: E501
        :rtype: bool
        """
        return self._additional_disk

    @additional_disk.setter
    def additional_disk(self, additional_disk):
        """Sets the additional_disk of this Disk.


        :param additional_disk: The additional_disk of this Disk.  # noqa: E501
        :type: bool
        """

        self._additional_disk = additional_disk

    @property
    def boot_disk(self):
        """Gets the boot_disk of this Disk.  # noqa: E501


        :return: The boot_disk of this Disk.  # noqa: E501
        :rtype: bool
        """
        return self._boot_disk

    @boot_disk.setter
    def boot_disk(self, boot_disk):
        """Sets the boot_disk of this Disk.


        :param boot_disk: The boot_disk of this Disk.  # noqa: E501
        :type: bool
        """

        self._boot_disk = boot_disk

    @property
    def capacity_in_megabytes(self):
        """Gets the capacity_in_megabytes of this Disk.  # noqa: E501


        :return: The capacity_in_megabytes of this Disk.  # noqa: E501
        :rtype: int
        """
        return self._capacity_in_megabytes

    @capacity_in_megabytes.setter
    def capacity_in_megabytes(self, capacity_in_megabytes):
        """Sets the capacity_in_megabytes of this Disk.


        :param capacity_in_megabytes: The capacity_in_megabytes of this Disk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and capacity_in_megabytes is None:  # noqa: E501
            raise ValueError("Invalid value for `capacity_in_megabytes`, must not be `None`")  # noqa: E501

        self._capacity_in_megabytes = capacity_in_megabytes

    @property
    def create_order(self):
        """Gets the create_order of this Disk.  # noqa: E501


        :return: The create_order of this Disk.  # noqa: E501
        :rtype: int
        """
        return self._create_order

    @create_order.setter
    def create_order(self, create_order):
        """Sets the create_order of this Disk.


        :param create_order: The create_order of this Disk.  # noqa: E501
        :type: int
        """

        self._create_order = create_order

    @property
    def is_additional_disk(self):
        """Gets the is_additional_disk of this Disk.  # noqa: E501


        :return: The is_additional_disk of this Disk.  # noqa: E501
        :rtype: bool
        """
        return self._is_additional_disk

    @is_additional_disk.setter
    def is_additional_disk(self, is_additional_disk):
        """Sets the is_additional_disk of this Disk.


        :param is_additional_disk: The is_additional_disk of this Disk.  # noqa: E501
        :type: bool
        """

        self._is_additional_disk = is_additional_disk

    @property
    def is_boot_disk(self):
        """Gets the is_boot_disk of this Disk.  # noqa: E501


        :return: The is_boot_disk of this Disk.  # noqa: E501
        :rtype: bool
        """
        return self._is_boot_disk

    @is_boot_disk.setter
    def is_boot_disk(self, is_boot_disk):
        """Sets the is_boot_disk of this Disk.


        :param is_boot_disk: The is_boot_disk of this Disk.  # noqa: E501
        :type: bool
        """

        self._is_boot_disk = is_boot_disk

    @property
    def id(self):
        """Gets the id of this Disk.  # noqa: E501


        :return: The id of this Disk.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Disk.


        :param id: The id of this Disk.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, Disk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Disk):
            return True

        return self.to_dict() != other.to_dict()
