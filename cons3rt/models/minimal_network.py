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


class MinimalNetwork(object):
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
        'id': 'int',
        'isolated': 'bool',
        'boundary_ip_address': 'str',
        'cidr': 'str',
        'gateway': 'str',
        'identifier': 'str',
        'network_function': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'isolated': 'isolated',
        'boundary_ip_address': 'boundaryIpAddress',
        'cidr': 'cidr',
        'gateway': 'gateway',
        'identifier': 'identifier',
        'network_function': 'networkFunction',
        'name': 'name'
    }

    def __init__(self, id=None, isolated=None, boundary_ip_address=None, cidr=None, gateway=None, identifier=None, network_function=None, name=None, local_vars_configuration=None):  # noqa: E501
        """MinimalNetwork - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._isolated = None
        self._boundary_ip_address = None
        self._cidr = None
        self._gateway = None
        self._identifier = None
        self._network_function = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if isolated is not None:
            self.isolated = isolated
        if boundary_ip_address is not None:
            self.boundary_ip_address = boundary_ip_address
        if cidr is not None:
            self.cidr = cidr
        if gateway is not None:
            self.gateway = gateway
        if identifier is not None:
            self.identifier = identifier
        if network_function is not None:
            self.network_function = network_function
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this MinimalNetwork.  # noqa: E501


        :return: The id of this MinimalNetwork.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalNetwork.


        :param id: The id of this MinimalNetwork.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def isolated(self):
        """Gets the isolated of this MinimalNetwork.  # noqa: E501


        :return: The isolated of this MinimalNetwork.  # noqa: E501
        :rtype: bool
        """
        return self._isolated

    @isolated.setter
    def isolated(self, isolated):
        """Sets the isolated of this MinimalNetwork.


        :param isolated: The isolated of this MinimalNetwork.  # noqa: E501
        :type: bool
        """

        self._isolated = isolated

    @property
    def boundary_ip_address(self):
        """Gets the boundary_ip_address of this MinimalNetwork.  # noqa: E501


        :return: The boundary_ip_address of this MinimalNetwork.  # noqa: E501
        :rtype: str
        """
        return self._boundary_ip_address

    @boundary_ip_address.setter
    def boundary_ip_address(self, boundary_ip_address):
        """Sets the boundary_ip_address of this MinimalNetwork.


        :param boundary_ip_address: The boundary_ip_address of this MinimalNetwork.  # noqa: E501
        :type: str
        """

        self._boundary_ip_address = boundary_ip_address

    @property
    def cidr(self):
        """Gets the cidr of this MinimalNetwork.  # noqa: E501


        :return: The cidr of this MinimalNetwork.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this MinimalNetwork.


        :param cidr: The cidr of this MinimalNetwork.  # noqa: E501
        :type: str
        """

        self._cidr = cidr

    @property
    def gateway(self):
        """Gets the gateway of this MinimalNetwork.  # noqa: E501


        :return: The gateway of this MinimalNetwork.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this MinimalNetwork.


        :param gateway: The gateway of this MinimalNetwork.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def identifier(self):
        """Gets the identifier of this MinimalNetwork.  # noqa: E501


        :return: The identifier of this MinimalNetwork.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this MinimalNetwork.


        :param identifier: The identifier of this MinimalNetwork.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def network_function(self):
        """Gets the network_function of this MinimalNetwork.  # noqa: E501


        :return: The network_function of this MinimalNetwork.  # noqa: E501
        :rtype: str
        """
        return self._network_function

    @network_function.setter
    def network_function(self, network_function):
        """Sets the network_function of this MinimalNetwork.


        :param network_function: The network_function of this MinimalNetwork.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONS3RT", "ADDITIONAL", "PRIMARY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and network_function not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `network_function` ({0}), must be one of {1}"  # noqa: E501
                .format(network_function, allowed_values)
            )

        self._network_function = network_function

    @property
    def name(self):
        """Gets the name of this MinimalNetwork.  # noqa: E501


        :return: The name of this MinimalNetwork.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MinimalNetwork.


        :param name: The name of this MinimalNetwork.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, MinimalNetwork):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalNetwork):
            return True

        return self.to_dict() != other.to_dict()
