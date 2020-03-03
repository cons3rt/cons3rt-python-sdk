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


class InputDisk(object):
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
        'capacity_in_megabytes': 'int',
        'create_order': 'int'
    }

    attribute_map = {
        'capacity_in_megabytes': 'capacityInMegabytes',
        'create_order': 'createOrder'
    }

    def __init__(self, capacity_in_megabytes=None, create_order=None, local_vars_configuration=None):  # noqa: E501
        """InputDisk - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._capacity_in_megabytes = None
        self._create_order = None
        self.discriminator = None

        self.capacity_in_megabytes = capacity_in_megabytes
        self.create_order = create_order

    @property
    def capacity_in_megabytes(self):
        """Gets the capacity_in_megabytes of this InputDisk.  # noqa: E501


        :return: The capacity_in_megabytes of this InputDisk.  # noqa: E501
        :rtype: int
        """
        return self._capacity_in_megabytes

    @capacity_in_megabytes.setter
    def capacity_in_megabytes(self, capacity_in_megabytes):
        """Sets the capacity_in_megabytes of this InputDisk.


        :param capacity_in_megabytes: The capacity_in_megabytes of this InputDisk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and capacity_in_megabytes is None:  # noqa: E501
            raise ValueError("Invalid value for `capacity_in_megabytes`, must not be `None`")  # noqa: E501

        self._capacity_in_megabytes = capacity_in_megabytes

    @property
    def create_order(self):
        """Gets the create_order of this InputDisk.  # noqa: E501


        :return: The create_order of this InputDisk.  # noqa: E501
        :rtype: int
        """
        return self._create_order

    @create_order.setter
    def create_order(self, create_order):
        """Sets the create_order of this InputDisk.


        :param create_order: The create_order of this InputDisk.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and create_order is None:  # noqa: E501
            raise ValueError("Invalid value for `create_order`, must not be `None`")  # noqa: E501

        self._create_order = create_order

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
        if not isinstance(other, InputDisk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputDisk):
            return True

        return self.to_dict() != other.to_dict()
