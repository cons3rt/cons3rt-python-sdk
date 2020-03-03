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


class ContainerPortMapping(object):
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
        'external_ip': 'str',
        'external_port': 'int',
        'internal_port': 'int',
        'protocol': 'str'
    }

    attribute_map = {
        'external_ip': 'externalIp',
        'external_port': 'externalPort',
        'internal_port': 'internalPort',
        'protocol': 'protocol'
    }

    def __init__(self, external_ip=None, external_port=None, internal_port=None, protocol=None, local_vars_configuration=None):  # noqa: E501
        """ContainerPortMapping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._external_ip = None
        self._external_port = None
        self._internal_port = None
        self._protocol = None
        self.discriminator = None

        self.external_ip = external_ip
        self.external_port = external_port
        self.internal_port = internal_port
        self.protocol = protocol

    @property
    def external_ip(self):
        """Gets the external_ip of this ContainerPortMapping.  # noqa: E501


        :return: The external_ip of this ContainerPortMapping.  # noqa: E501
        :rtype: str
        """
        return self._external_ip

    @external_ip.setter
    def external_ip(self, external_ip):
        """Sets the external_ip of this ContainerPortMapping.


        :param external_ip: The external_ip of this ContainerPortMapping.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `external_ip`, must not be `None`")  # noqa: E501

        self._external_ip = external_ip

    @property
    def external_port(self):
        """Gets the external_port of this ContainerPortMapping.  # noqa: E501


        :return: The external_port of this ContainerPortMapping.  # noqa: E501
        :rtype: int
        """
        return self._external_port

    @external_port.setter
    def external_port(self, external_port):
        """Sets the external_port of this ContainerPortMapping.


        :param external_port: The external_port of this ContainerPortMapping.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and external_port is None:  # noqa: E501
            raise ValueError("Invalid value for `external_port`, must not be `None`")  # noqa: E501

        self._external_port = external_port

    @property
    def internal_port(self):
        """Gets the internal_port of this ContainerPortMapping.  # noqa: E501


        :return: The internal_port of this ContainerPortMapping.  # noqa: E501
        :rtype: int
        """
        return self._internal_port

    @internal_port.setter
    def internal_port(self, internal_port):
        """Sets the internal_port of this ContainerPortMapping.


        :param internal_port: The internal_port of this ContainerPortMapping.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and internal_port is None:  # noqa: E501
            raise ValueError("Invalid value for `internal_port`, must not be `None`")  # noqa: E501

        self._internal_port = internal_port

    @property
    def protocol(self):
        """Gets the protocol of this ContainerPortMapping.  # noqa: E501


        :return: The protocol of this ContainerPortMapping.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ContainerPortMapping.


        :param protocol: The protocol of this ContainerPortMapping.  # noqa: E501
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
        if not isinstance(other, ContainerPortMapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerPortMapping):
            return True

        return self.to_dict() != other.to_dict()
