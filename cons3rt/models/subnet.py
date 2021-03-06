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


class Subnet(object):
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
        'cidr': 'str',
        'id': 'int',
        'identifier': 'str',
        'name': 'str',
        'nat_instance': 'NatInstance',
        'security_group': 'SecurityGroup'
    }

    attribute_map = {
        'cidr': 'cidr',
        'id': 'id',
        'identifier': 'identifier',
        'name': 'name',
        'nat_instance': 'natInstance',
        'security_group': 'securityGroup'
    }

    def __init__(self, cidr=None, id=None, identifier=None, name=None, nat_instance=None, security_group=None, local_vars_configuration=None):  # noqa: E501
        """Subnet - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cidr = None
        self._id = None
        self._identifier = None
        self._name = None
        self._nat_instance = None
        self._security_group = None
        self.discriminator = None

        self.cidr = cidr
        if id is not None:
            self.id = id
        self.identifier = identifier
        self.name = name
        self.nat_instance = nat_instance
        self.security_group = security_group

    @property
    def cidr(self):
        """Gets the cidr of this Subnet.  # noqa: E501


        :return: The cidr of this Subnet.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this Subnet.


        :param cidr: The cidr of this Subnet.  # noqa: E501
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
    def id(self):
        """Gets the id of this Subnet.  # noqa: E501


        :return: The id of this Subnet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subnet.


        :param id: The id of this Subnet.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def identifier(self):
        """Gets the identifier of this Subnet.  # noqa: E501


        :return: The identifier of this Subnet.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Subnet.


        :param identifier: The identifier of this Subnet.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and identifier is None:  # noqa: E501
            raise ValueError("Invalid value for `identifier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                identifier is not None and len(identifier) > 255):
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                identifier is not None and len(identifier) < 1):
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `1`")  # noqa: E501

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this Subnet.  # noqa: E501


        :return: The name of this Subnet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Subnet.


        :param name: The name of this Subnet.  # noqa: E501
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

    @property
    def nat_instance(self):
        """Gets the nat_instance of this Subnet.  # noqa: E501


        :return: The nat_instance of this Subnet.  # noqa: E501
        :rtype: NatInstance
        """
        return self._nat_instance

    @nat_instance.setter
    def nat_instance(self, nat_instance):
        """Sets the nat_instance of this Subnet.


        :param nat_instance: The nat_instance of this Subnet.  # noqa: E501
        :type: NatInstance
        """
        if self.local_vars_configuration.client_side_validation and nat_instance is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_instance`, must not be `None`")  # noqa: E501

        self._nat_instance = nat_instance

    @property
    def security_group(self):
        """Gets the security_group of this Subnet.  # noqa: E501


        :return: The security_group of this Subnet.  # noqa: E501
        :rtype: SecurityGroup
        """
        return self._security_group

    @security_group.setter
    def security_group(self, security_group):
        """Sets the security_group of this Subnet.


        :param security_group: The security_group of this Subnet.  # noqa: E501
        :type: SecurityGroup
        """
        if self.local_vars_configuration.client_side_validation and security_group is None:  # noqa: E501
            raise ValueError("Invalid value for `security_group`, must not be `None`")  # noqa: E501

        self._security_group = security_group

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
        if not isinstance(other, Subnet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Subnet):
            return True

        return self.to_dict() != other.to_dict()
