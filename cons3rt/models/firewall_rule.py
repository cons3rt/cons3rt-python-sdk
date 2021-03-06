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


class FirewallRule(object):
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
        'rule_order': 'int',
        'protocol': 'str',
        'rule_action': 'str',
        'rule_destination': 'str',
        'rule_dest_port': 'str',
        'rule_enabled': 'bool',
        'rule_source': 'str',
        'rule_source_port': 'str'
    }

    attribute_map = {
        'id': 'id',
        'rule_order': 'ruleOrder',
        'protocol': 'protocol',
        'rule_action': 'ruleAction',
        'rule_destination': 'ruleDestination',
        'rule_dest_port': 'ruleDestPort',
        'rule_enabled': 'ruleEnabled',
        'rule_source': 'ruleSource',
        'rule_source_port': 'ruleSourcePort'
    }

    def __init__(self, id=None, rule_order=None, protocol=None, rule_action=None, rule_destination=None, rule_dest_port=None, rule_enabled=None, rule_source=None, rule_source_port=None, local_vars_configuration=None):  # noqa: E501
        """FirewallRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._rule_order = None
        self._protocol = None
        self._rule_action = None
        self._rule_destination = None
        self._rule_dest_port = None
        self._rule_enabled = None
        self._rule_source = None
        self._rule_source_port = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.rule_order = rule_order
        self.protocol = protocol
        self.rule_action = rule_action
        self.rule_destination = rule_destination
        if rule_dest_port is not None:
            self.rule_dest_port = rule_dest_port
        self.rule_enabled = rule_enabled
        self.rule_source = rule_source
        if rule_source_port is not None:
            self.rule_source_port = rule_source_port

    @property
    def id(self):
        """Gets the id of this FirewallRule.  # noqa: E501


        :return: The id of this FirewallRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirewallRule.


        :param id: The id of this FirewallRule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def rule_order(self):
        """Gets the rule_order of this FirewallRule.  # noqa: E501


        :return: The rule_order of this FirewallRule.  # noqa: E501
        :rtype: int
        """
        return self._rule_order

    @rule_order.setter
    def rule_order(self, rule_order):
        """Sets the rule_order of this FirewallRule.


        :param rule_order: The rule_order of this FirewallRule.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and rule_order is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_order`, must not be `None`")  # noqa: E501

        self._rule_order = rule_order

    @property
    def protocol(self):
        """Gets the protocol of this FirewallRule.  # noqa: E501


        :return: The protocol of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FirewallRule.


        :param protocol: The protocol of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["ANY", "ICMP", "TCP", "UDP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and protocol not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def rule_action(self):
        """Gets the rule_action of this FirewallRule.  # noqa: E501


        :return: The rule_action of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_action

    @rule_action.setter
    def rule_action(self, rule_action):
        """Sets the rule_action of this FirewallRule.


        :param rule_action: The rule_action of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_action is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_action`, must not be `None`")  # noqa: E501
        allowed_values = ["ALLOW", "DENY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and rule_action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `rule_action` ({0}), must be one of {1}"  # noqa: E501
                .format(rule_action, allowed_values)
            )

        self._rule_action = rule_action

    @property
    def rule_destination(self):
        """Gets the rule_destination of this FirewallRule.  # noqa: E501


        :return: The rule_destination of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_destination

    @rule_destination.setter
    def rule_destination(self, rule_destination):
        """Sets the rule_destination of this FirewallRule.


        :param rule_destination: The rule_destination of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_destination is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_destination`, must not be `None`")  # noqa: E501

        self._rule_destination = rule_destination

    @property
    def rule_dest_port(self):
        """Gets the rule_dest_port of this FirewallRule.  # noqa: E501


        :return: The rule_dest_port of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_dest_port

    @rule_dest_port.setter
    def rule_dest_port(self, rule_dest_port):
        """Sets the rule_dest_port of this FirewallRule.


        :param rule_dest_port: The rule_dest_port of this FirewallRule.  # noqa: E501
        :type: str
        """

        self._rule_dest_port = rule_dest_port

    @property
    def rule_enabled(self):
        """Gets the rule_enabled of this FirewallRule.  # noqa: E501


        :return: The rule_enabled of this FirewallRule.  # noqa: E501
        :rtype: bool
        """
        return self._rule_enabled

    @rule_enabled.setter
    def rule_enabled(self, rule_enabled):
        """Sets the rule_enabled of this FirewallRule.


        :param rule_enabled: The rule_enabled of this FirewallRule.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and rule_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_enabled`, must not be `None`")  # noqa: E501

        self._rule_enabled = rule_enabled

    @property
    def rule_source(self):
        """Gets the rule_source of this FirewallRule.  # noqa: E501


        :return: The rule_source of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_source

    @rule_source.setter
    def rule_source(self, rule_source):
        """Sets the rule_source of this FirewallRule.


        :param rule_source: The rule_source of this FirewallRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and rule_source is None:  # noqa: E501
            raise ValueError("Invalid value for `rule_source`, must not be `None`")  # noqa: E501

        self._rule_source = rule_source

    @property
    def rule_source_port(self):
        """Gets the rule_source_port of this FirewallRule.  # noqa: E501


        :return: The rule_source_port of this FirewallRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_source_port

    @rule_source_port.setter
    def rule_source_port(self, rule_source_port):
        """Sets the rule_source_port of this FirewallRule.


        :param rule_source_port: The rule_source_port of this FirewallRule.  # noqa: E501
        :type: str
        """

        self._rule_source_port = rule_source_port

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
        if not isinstance(other, FirewallRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FirewallRule):
            return True

        return self.to_dict() != other.to_dict()
