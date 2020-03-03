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


class Network(object):
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
        'cidr': 'str',
        'description': 'str',
        'dnat_rules': 'list[DnatRule]',
        'firewall_rules': 'list[FirewallRule]',
        'network_function': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'isolated': 'isolated',
        'cidr': 'cidr',
        'description': 'description',
        'dnat_rules': 'dnatRules',
        'firewall_rules': 'firewallRules',
        'network_function': 'networkFunction',
        'name': 'name'
    }

    def __init__(self, id=None, isolated=None, cidr=None, description=None, dnat_rules=None, firewall_rules=None, network_function=None, name=None, local_vars_configuration=None):  # noqa: E501
        """Network - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._isolated = None
        self._cidr = None
        self._description = None
        self._dnat_rules = None
        self._firewall_rules = None
        self._network_function = None
        self._name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if isolated is not None:
            self.isolated = isolated
        self.cidr = cidr
        if description is not None:
            self.description = description
        self.dnat_rules = dnat_rules
        self.firewall_rules = firewall_rules
        if network_function is not None:
            self.network_function = network_function
        self.name = name

    @property
    def id(self):
        """Gets the id of this Network.  # noqa: E501


        :return: The id of this Network.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Network.


        :param id: The id of this Network.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def isolated(self):
        """Gets the isolated of this Network.  # noqa: E501


        :return: The isolated of this Network.  # noqa: E501
        :rtype: bool
        """
        return self._isolated

    @isolated.setter
    def isolated(self, isolated):
        """Sets the isolated of this Network.


        :param isolated: The isolated of this Network.  # noqa: E501
        :type: bool
        """

        self._isolated = isolated

    @property
    def cidr(self):
        """Gets the cidr of this Network.  # noqa: E501


        :return: The cidr of this Network.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Network.


        :param cidr: The cidr of this Network.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cidr is None:  # noqa: E501
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cidr is not None and len(cidr) > 16):
            raise ValueError("Invalid value for `cidr`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cidr is not None and len(cidr) < 10):
            raise ValueError("Invalid value for `cidr`, length must be greater than or equal to `10`")  # noqa: E501

        self._cidr = cidr

    @property
    def description(self):
        """Gets the description of this Network.  # noqa: E501


        :return: The description of this Network.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Network.


        :param description: The description of this Network.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dnat_rules(self):
        """Gets the dnat_rules of this Network.  # noqa: E501


        :return: The dnat_rules of this Network.  # noqa: E501
        :rtype: list[DnatRule]
        """
        return self._dnat_rules

    @dnat_rules.setter
    def dnat_rules(self, dnat_rules):
        """Sets the dnat_rules of this Network.


        :param dnat_rules: The dnat_rules of this Network.  # noqa: E501
        :type: list[DnatRule]
        """
        if self.local_vars_configuration.client_side_validation and dnat_rules is None:  # noqa: E501
            raise ValueError("Invalid value for `dnat_rules`, must not be `None`")  # noqa: E501

        self._dnat_rules = dnat_rules

    @property
    def firewall_rules(self):
        """Gets the firewall_rules of this Network.  # noqa: E501


        :return: The firewall_rules of this Network.  # noqa: E501
        :rtype: list[FirewallRule]
        """
        return self._firewall_rules

    @firewall_rules.setter
    def firewall_rules(self, firewall_rules):
        """Sets the firewall_rules of this Network.


        :param firewall_rules: The firewall_rules of this Network.  # noqa: E501
        :type: list[FirewallRule]
        """
        if self.local_vars_configuration.client_side_validation and firewall_rules is None:  # noqa: E501
            raise ValueError("Invalid value for `firewall_rules`, must not be `None`")  # noqa: E501

        self._firewall_rules = firewall_rules

    @property
    def network_function(self):
        """Gets the network_function of this Network.  # noqa: E501


        :return: The network_function of this Network.  # noqa: E501
        :rtype: str
        """
        return self._network_function

    @network_function.setter
    def network_function(self, network_function):
        """Sets the network_function of this Network.


        :param network_function: The network_function of this Network.  # noqa: E501
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
        """Gets the name of this Network.  # noqa: E501


        :return: The name of this Network.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Network.


        :param name: The name of this Network.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

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
        if not isinstance(other, Network):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Network):
            return True

        return self.to_dict() != other.to_dict()
