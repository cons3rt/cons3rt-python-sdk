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


class AbstractAddNetworkCloudSpaceRequest(object):
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
        'network': 'Network',
        'subtype': 'str'
    }

    attribute_map = {
        'network': 'network',
        'subtype': 'subtype'
    }

    discriminator_value_class_map = {
        'AddAzureNetworkRequest': 'AddAzureNetworkRequest',
        'AddVcloudNetworkRequest': 'AddVcloudNetworkRequest',
        'AddOpenStackNetworkRequest': 'AddOpenStackNetworkRequest',
        'AddAwsNetworkRequest': 'AddAwsNetworkRequest',
        'AddVcloudRestNetworkRequest': 'AddVcloudRestNetworkRequest'
    }

    def __init__(self, network=None, subtype=None, local_vars_configuration=None):  # noqa: E501
        """AbstractAddNetworkCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._network = None
        self._subtype = None
        self.discriminator = 'subtype'

        self.network = network
        self.subtype = subtype

    @property
    def network(self):
        """Gets the network of this AbstractAddNetworkCloudSpaceRequest.  # noqa: E501


        :return: The network of this AbstractAddNetworkCloudSpaceRequest.  # noqa: E501
        :rtype: Network
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this AbstractAddNetworkCloudSpaceRequest.


        :param network: The network of this AbstractAddNetworkCloudSpaceRequest.  # noqa: E501
        :type: Network
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def subtype(self):
        """Gets the subtype of this AbstractAddNetworkCloudSpaceRequest.  # noqa: E501


        :return: The subtype of this AbstractAddNetworkCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this AbstractAddNetworkCloudSpaceRequest.


        :param subtype: The subtype of this AbstractAddNetworkCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, AbstractAddNetworkCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AbstractAddNetworkCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
