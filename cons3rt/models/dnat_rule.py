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


class DnatRule(object):
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
        'dnat_enabled': 'bool',
        'dnat_port': 'str',
        'dnat_protocol': 'str',
        'dnat_target_ip': 'str',
        'dnat_target_port': 'str',
        'id': 'int'
    }

    attribute_map = {
        'dnat_enabled': 'dnatEnabled',
        'dnat_port': 'dnatPort',
        'dnat_protocol': 'dnatProtocol',
        'dnat_target_ip': 'dnatTargetIp',
        'dnat_target_port': 'dnatTargetPort',
        'id': 'id'
    }

    def __init__(self, dnat_enabled=None, dnat_port=None, dnat_protocol=None, dnat_target_ip=None, dnat_target_port=None, id=None, local_vars_configuration=None):  # noqa: E501
        """DnatRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._dnat_enabled = None
        self._dnat_port = None
        self._dnat_protocol = None
        self._dnat_target_ip = None
        self._dnat_target_port = None
        self._id = None
        self.discriminator = None

        self.dnat_enabled = dnat_enabled
        self.dnat_port = dnat_port
        self.dnat_protocol = dnat_protocol
        self.dnat_target_ip = dnat_target_ip
        self.dnat_target_port = dnat_target_port
        if id is not None:
            self.id = id

    @property
    def dnat_enabled(self):
        """Gets the dnat_enabled of this DnatRule.  # noqa: E501


        :return: The dnat_enabled of this DnatRule.  # noqa: E501
        :rtype: bool
        """
        return self._dnat_enabled

    @dnat_enabled.setter
    def dnat_enabled(self, dnat_enabled):
        """Sets the dnat_enabled of this DnatRule.


        :param dnat_enabled: The dnat_enabled of this DnatRule.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and dnat_enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `dnat_enabled`, must not be `None`")  # noqa: E501

        self._dnat_enabled = dnat_enabled

    @property
    def dnat_port(self):
        """Gets the dnat_port of this DnatRule.  # noqa: E501


        :return: The dnat_port of this DnatRule.  # noqa: E501
        :rtype: str
        """
        return self._dnat_port

    @dnat_port.setter
    def dnat_port(self, dnat_port):
        """Sets the dnat_port of this DnatRule.


        :param dnat_port: The dnat_port of this DnatRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dnat_port is None:  # noqa: E501
            raise ValueError("Invalid value for `dnat_port`, must not be `None`")  # noqa: E501

        self._dnat_port = dnat_port

    @property
    def dnat_protocol(self):
        """Gets the dnat_protocol of this DnatRule.  # noqa: E501


        :return: The dnat_protocol of this DnatRule.  # noqa: E501
        :rtype: str
        """
        return self._dnat_protocol

    @dnat_protocol.setter
    def dnat_protocol(self, dnat_protocol):
        """Sets the dnat_protocol of this DnatRule.


        :param dnat_protocol: The dnat_protocol of this DnatRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dnat_protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `dnat_protocol`, must not be `None`")  # noqa: E501
        allowed_values = ["ANY", "ICMP", "TCP", "UDP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and dnat_protocol not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `dnat_protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(dnat_protocol, allowed_values)
            )

        self._dnat_protocol = dnat_protocol

    @property
    def dnat_target_ip(self):
        """Gets the dnat_target_ip of this DnatRule.  # noqa: E501


        :return: The dnat_target_ip of this DnatRule.  # noqa: E501
        :rtype: str
        """
        return self._dnat_target_ip

    @dnat_target_ip.setter
    def dnat_target_ip(self, dnat_target_ip):
        """Sets the dnat_target_ip of this DnatRule.


        :param dnat_target_ip: The dnat_target_ip of this DnatRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dnat_target_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `dnat_target_ip`, must not be `None`")  # noqa: E501

        self._dnat_target_ip = dnat_target_ip

    @property
    def dnat_target_port(self):
        """Gets the dnat_target_port of this DnatRule.  # noqa: E501


        :return: The dnat_target_port of this DnatRule.  # noqa: E501
        :rtype: str
        """
        return self._dnat_target_port

    @dnat_target_port.setter
    def dnat_target_port(self, dnat_target_port):
        """Sets the dnat_target_port of this DnatRule.


        :param dnat_target_port: The dnat_target_port of this DnatRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and dnat_target_port is None:  # noqa: E501
            raise ValueError("Invalid value for `dnat_target_port`, must not be `None`")  # noqa: E501

        self._dnat_target_port = dnat_target_port

    @property
    def id(self):
        """Gets the id of this DnatRule.  # noqa: E501


        :return: The id of this DnatRule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DnatRule.


        :param id: The id of this DnatRule.  # noqa: E501
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
        if not isinstance(other, DnatRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DnatRule):
            return True

        return self.to_dict() != other.to_dict()
