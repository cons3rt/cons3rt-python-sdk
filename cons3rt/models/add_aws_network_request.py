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


class AddAwsNetworkRequest(object):
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
        'nat_instance_type': 'str',
        'nat_image_id': 'str'
    }

    attribute_map = {
        'nat_instance_type': 'natInstanceType',
        'nat_image_id': 'natImageId'
    }

    def __init__(self, nat_instance_type=None, nat_image_id=None, local_vars_configuration=None):  # noqa: E501
        """AddAwsNetworkRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nat_instance_type = None
        self._nat_image_id = None
        self.discriminator = None

        self.nat_instance_type = nat_instance_type
        self.nat_image_id = nat_image_id

    @property
    def nat_instance_type(self):
        """Gets the nat_instance_type of this AddAwsNetworkRequest.  # noqa: E501


        :return: The nat_instance_type of this AddAwsNetworkRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_instance_type

    @nat_instance_type.setter
    def nat_instance_type(self, nat_instance_type):
        """Sets the nat_instance_type of this AddAwsNetworkRequest.


        :param nat_instance_type: The nat_instance_type of this AddAwsNetworkRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nat_instance_type is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_instance_type`, must not be `None`")  # noqa: E501

        self._nat_instance_type = nat_instance_type

    @property
    def nat_image_id(self):
        """Gets the nat_image_id of this AddAwsNetworkRequest.  # noqa: E501


        :return: The nat_image_id of this AddAwsNetworkRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_image_id

    @nat_image_id.setter
    def nat_image_id(self, nat_image_id):
        """Sets the nat_image_id of this AddAwsNetworkRequest.


        :param nat_image_id: The nat_image_id of this AddAwsNetworkRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nat_image_id is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_image_id`, must not be `None`")  # noqa: E501

        self._nat_image_id = nat_image_id

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
        if not isinstance(other, AddAwsNetworkRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddAwsNetworkRequest):
            return True

        return self.to_dict() != other.to_dict()
