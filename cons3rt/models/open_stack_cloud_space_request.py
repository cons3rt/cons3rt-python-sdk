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


class OpenStackCloudSpaceRequest(object):
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
        'nat_flavor_type': 'str',
        'nat_image_id': 'str',
        'dns_server_ip_addresses': 'str',
        'external_network_name': 'str'
    }

    attribute_map = {
        'nat_flavor_type': 'natFlavorType',
        'nat_image_id': 'natImageId',
        'dns_server_ip_addresses': 'dnsServerIpAddresses',
        'external_network_name': 'externalNetworkName'
    }

    def __init__(self, nat_flavor_type=None, nat_image_id=None, dns_server_ip_addresses=None, external_network_name=None, local_vars_configuration=None):  # noqa: E501
        """OpenStackCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nat_flavor_type = None
        self._nat_image_id = None
        self._dns_server_ip_addresses = None
        self._external_network_name = None
        self.discriminator = None

        self.nat_flavor_type = nat_flavor_type
        self.nat_image_id = nat_image_id
        if dns_server_ip_addresses is not None:
            self.dns_server_ip_addresses = dns_server_ip_addresses
        self.external_network_name = external_network_name

    @property
    def nat_flavor_type(self):
        """Gets the nat_flavor_type of this OpenStackCloudSpaceRequest.  # noqa: E501


        :return: The nat_flavor_type of this OpenStackCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_flavor_type

    @nat_flavor_type.setter
    def nat_flavor_type(self, nat_flavor_type):
        """Sets the nat_flavor_type of this OpenStackCloudSpaceRequest.


        :param nat_flavor_type: The nat_flavor_type of this OpenStackCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nat_flavor_type is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_flavor_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                nat_flavor_type is not None and len(nat_flavor_type) > 255):
            raise ValueError("Invalid value for `nat_flavor_type`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                nat_flavor_type is not None and len(nat_flavor_type) < 1):
            raise ValueError("Invalid value for `nat_flavor_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._nat_flavor_type = nat_flavor_type

    @property
    def nat_image_id(self):
        """Gets the nat_image_id of this OpenStackCloudSpaceRequest.  # noqa: E501


        :return: The nat_image_id of this OpenStackCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_image_id

    @nat_image_id.setter
    def nat_image_id(self, nat_image_id):
        """Sets the nat_image_id of this OpenStackCloudSpaceRequest.


        :param nat_image_id: The nat_image_id of this OpenStackCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nat_image_id is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_image_id`, must not be `None`")  # noqa: E501

        self._nat_image_id = nat_image_id

    @property
    def dns_server_ip_addresses(self):
        """Gets the dns_server_ip_addresses of this OpenStackCloudSpaceRequest.  # noqa: E501


        :return: The dns_server_ip_addresses of this OpenStackCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._dns_server_ip_addresses

    @dns_server_ip_addresses.setter
    def dns_server_ip_addresses(self, dns_server_ip_addresses):
        """Sets the dns_server_ip_addresses of this OpenStackCloudSpaceRequest.


        :param dns_server_ip_addresses: The dns_server_ip_addresses of this OpenStackCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._dns_server_ip_addresses = dns_server_ip_addresses

    @property
    def external_network_name(self):
        """Gets the external_network_name of this OpenStackCloudSpaceRequest.  # noqa: E501


        :return: The external_network_name of this OpenStackCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_network_name

    @external_network_name.setter
    def external_network_name(self, external_network_name):
        """Sets the external_network_name of this OpenStackCloudSpaceRequest.


        :param external_network_name: The external_network_name of this OpenStackCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_network_name is None:  # noqa: E501
            raise ValueError("Invalid value for `external_network_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_network_name is not None and len(external_network_name) > 255):
            raise ValueError("Invalid value for `external_network_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_network_name is not None and len(external_network_name) < 1):
            raise ValueError("Invalid value for `external_network_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._external_network_name = external_network_name

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
        if not isinstance(other, OpenStackCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenStackCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
