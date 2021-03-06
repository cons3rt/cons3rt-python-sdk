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


class NatInstance(object):
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
        'identifier': 'str',
        'internal_ip': 'str',
        'password': 'str',
        'nat_security_group_identifier': 'str',
        'ssh_key_name': 'str',
        'ssh_key_pem': 'str',
        'username': 'str'
    }

    attribute_map = {
        'external_ip': 'externalIp',
        'identifier': 'identifier',
        'internal_ip': 'internalIp',
        'password': 'password',
        'nat_security_group_identifier': 'natSecurityGroupIdentifier',
        'ssh_key_name': 'sshKeyName',
        'ssh_key_pem': 'sshKeyPem',
        'username': 'username'
    }

    def __init__(self, external_ip=None, identifier=None, internal_ip=None, password=None, nat_security_group_identifier=None, ssh_key_name=None, ssh_key_pem=None, username=None, local_vars_configuration=None):  # noqa: E501
        """NatInstance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._external_ip = None
        self._identifier = None
        self._internal_ip = None
        self._password = None
        self._nat_security_group_identifier = None
        self._ssh_key_name = None
        self._ssh_key_pem = None
        self._username = None
        self.discriminator = None

        self.external_ip = external_ip
        if identifier is not None:
            self.identifier = identifier
        if internal_ip is not None:
            self.internal_ip = internal_ip
        if password is not None:
            self.password = password
        if nat_security_group_identifier is not None:
            self.nat_security_group_identifier = nat_security_group_identifier
        if ssh_key_name is not None:
            self.ssh_key_name = ssh_key_name
        if ssh_key_pem is not None:
            self.ssh_key_pem = ssh_key_pem
        if username is not None:
            self.username = username

    @property
    def external_ip(self):
        """Gets the external_ip of this NatInstance.  # noqa: E501


        :return: The external_ip of this NatInstance.  # noqa: E501
        :rtype: str
        """
        return self._external_ip

    @external_ip.setter
    def external_ip(self, external_ip):
        """Sets the external_ip of this NatInstance.


        :param external_ip: The external_ip of this NatInstance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_ip is None:  # noqa: E501
            raise ValueError("Invalid value for `external_ip`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_ip is not None and len(external_ip) > 15):
            raise ValueError("Invalid value for `external_ip`, length must be less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                external_ip is not None and len(external_ip) < 1):
            raise ValueError("Invalid value for `external_ip`, length must be greater than or equal to `1`")  # noqa: E501

        self._external_ip = external_ip

    @property
    def identifier(self):
        """Gets the identifier of this NatInstance.  # noqa: E501


        :return: The identifier of this NatInstance.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this NatInstance.


        :param identifier: The identifier of this NatInstance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                identifier is not None and len(identifier) > 255):
            raise ValueError("Invalid value for `identifier`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                identifier is not None and len(identifier) < 1):
            raise ValueError("Invalid value for `identifier`, length must be greater than or equal to `1`")  # noqa: E501

        self._identifier = identifier

    @property
    def internal_ip(self):
        """Gets the internal_ip of this NatInstance.  # noqa: E501


        :return: The internal_ip of this NatInstance.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this NatInstance.


        :param internal_ip: The internal_ip of this NatInstance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                internal_ip is not None and len(internal_ip) > 15):
            raise ValueError("Invalid value for `internal_ip`, length must be less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                internal_ip is not None and len(internal_ip) < 1):
            raise ValueError("Invalid value for `internal_ip`, length must be greater than or equal to `1`")  # noqa: E501

        self._internal_ip = internal_ip

    @property
    def password(self):
        """Gets the password of this NatInstance.  # noqa: E501


        :return: The password of this NatInstance.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this NatInstance.


        :param password: The password of this NatInstance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) > 255):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 1):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

    @property
    def nat_security_group_identifier(self):
        """Gets the nat_security_group_identifier of this NatInstance.  # noqa: E501


        :return: The nat_security_group_identifier of this NatInstance.  # noqa: E501
        :rtype: str
        """
        return self._nat_security_group_identifier

    @nat_security_group_identifier.setter
    def nat_security_group_identifier(self, nat_security_group_identifier):
        """Sets the nat_security_group_identifier of this NatInstance.


        :param nat_security_group_identifier: The nat_security_group_identifier of this NatInstance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                nat_security_group_identifier is not None and len(nat_security_group_identifier) > 255):
            raise ValueError("Invalid value for `nat_security_group_identifier`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                nat_security_group_identifier is not None and len(nat_security_group_identifier) < 1):
            raise ValueError("Invalid value for `nat_security_group_identifier`, length must be greater than or equal to `1`")  # noqa: E501

        self._nat_security_group_identifier = nat_security_group_identifier

    @property
    def ssh_key_name(self):
        """Gets the ssh_key_name of this NatInstance.  # noqa: E501


        :return: The ssh_key_name of this NatInstance.  # noqa: E501
        :rtype: str
        """
        return self._ssh_key_name

    @ssh_key_name.setter
    def ssh_key_name(self, ssh_key_name):
        """Sets the ssh_key_name of this NatInstance.


        :param ssh_key_name: The ssh_key_name of this NatInstance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ssh_key_name is not None and len(ssh_key_name) > 255):
            raise ValueError("Invalid value for `ssh_key_name`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ssh_key_name is not None and len(ssh_key_name) < 1):
            raise ValueError("Invalid value for `ssh_key_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._ssh_key_name = ssh_key_name

    @property
    def ssh_key_pem(self):
        """Gets the ssh_key_pem of this NatInstance.  # noqa: E501


        :return: The ssh_key_pem of this NatInstance.  # noqa: E501
        :rtype: str
        """
        return self._ssh_key_pem

    @ssh_key_pem.setter
    def ssh_key_pem(self, ssh_key_pem):
        """Sets the ssh_key_pem of this NatInstance.


        :param ssh_key_pem: The ssh_key_pem of this NatInstance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                ssh_key_pem is not None and len(ssh_key_pem) > 255):
            raise ValueError("Invalid value for `ssh_key_pem`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ssh_key_pem is not None and len(ssh_key_pem) < 1):
            raise ValueError("Invalid value for `ssh_key_pem`, length must be greater than or equal to `1`")  # noqa: E501

        self._ssh_key_pem = ssh_key_pem

    @property
    def username(self):
        """Gets the username of this NatInstance.  # noqa: E501


        :return: The username of this NatInstance.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this NatInstance.


        :param username: The username of this NatInstance.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 255):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, NatInstance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NatInstance):
            return True

        return self.to_dict() != other.to_dict()
