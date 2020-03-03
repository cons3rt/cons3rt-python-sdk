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


class InputSoftwareComponent(object):
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
        'asset': 'InputAsset',
        'reboot_delay': 'int',
        'reboot_required': 'bool',
        'id': 'int',
        'load_order': 'int'
    }

    attribute_map = {
        'asset': 'asset',
        'reboot_delay': 'rebootDelay',
        'reboot_required': 'rebootRequired',
        'id': 'id',
        'load_order': 'loadOrder'
    }

    def __init__(self, asset=None, reboot_delay=None, reboot_required=None, id=None, load_order=None, local_vars_configuration=None):  # noqa: E501
        """InputSoftwareComponent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset = None
        self._reboot_delay = None
        self._reboot_required = None
        self._id = None
        self._load_order = None
        self.discriminator = None

        self.asset = asset
        if reboot_delay is not None:
            self.reboot_delay = reboot_delay
        if reboot_required is not None:
            self.reboot_required = reboot_required
        if id is not None:
            self.id = id
        if load_order is not None:
            self.load_order = load_order

    @property
    def asset(self):
        """Gets the asset of this InputSoftwareComponent.  # noqa: E501


        :return: The asset of this InputSoftwareComponent.  # noqa: E501
        :rtype: InputAsset
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this InputSoftwareComponent.


        :param asset: The asset of this InputSoftwareComponent.  # noqa: E501
        :type: InputAsset
        """
        if self.local_vars_configuration.client_side_validation and asset is None:  # noqa: E501
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def reboot_delay(self):
        """Gets the reboot_delay of this InputSoftwareComponent.  # noqa: E501


        :return: The reboot_delay of this InputSoftwareComponent.  # noqa: E501
        :rtype: int
        """
        return self._reboot_delay

    @reboot_delay.setter
    def reboot_delay(self, reboot_delay):
        """Sets the reboot_delay of this InputSoftwareComponent.


        :param reboot_delay: The reboot_delay of this InputSoftwareComponent.  # noqa: E501
        :type: int
        """

        self._reboot_delay = reboot_delay

    @property
    def reboot_required(self):
        """Gets the reboot_required of this InputSoftwareComponent.  # noqa: E501


        :return: The reboot_required of this InputSoftwareComponent.  # noqa: E501
        :rtype: bool
        """
        return self._reboot_required

    @reboot_required.setter
    def reboot_required(self, reboot_required):
        """Sets the reboot_required of this InputSoftwareComponent.


        :param reboot_required: The reboot_required of this InputSoftwareComponent.  # noqa: E501
        :type: bool
        """

        self._reboot_required = reboot_required

    @property
    def id(self):
        """Gets the id of this InputSoftwareComponent.  # noqa: E501


        :return: The id of this InputSoftwareComponent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InputSoftwareComponent.


        :param id: The id of this InputSoftwareComponent.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def load_order(self):
        """Gets the load_order of this InputSoftwareComponent.  # noqa: E501


        :return: The load_order of this InputSoftwareComponent.  # noqa: E501
        :rtype: int
        """
        return self._load_order

    @load_order.setter
    def load_order(self, load_order):
        """Sets the load_order of this InputSoftwareComponent.


        :param load_order: The load_order of this InputSoftwareComponent.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                load_order is not None and load_order < 0):  # noqa: E501
            raise ValueError("Invalid value for `load_order`, must be a value greater than or equal to `0`")  # noqa: E501

        self._load_order = load_order

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
        if not isinstance(other, InputSoftwareComponent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputSoftwareComponent):
            return True

        return self.to_dict() != other.to_dict()
