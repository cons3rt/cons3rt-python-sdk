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


class AbstractProviderClientConfiguration(object):
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
        'debug': 'bool',
        'account_id': 'str',
        'password': 'str',
        'username': 'str',
        'subtype': 'str'
    }

    attribute_map = {
        'debug': 'debug',
        'account_id': 'accountId',
        'password': 'password',
        'username': 'username',
        'subtype': 'subtype'
    }

    discriminator_value_class_map = {
        'AwsClientConfiguration': 'AwsClientConfiguration'
    }

    def __init__(self, debug=None, account_id=None, password=None, username=None, subtype=None, local_vars_configuration=None):  # noqa: E501
        """AbstractProviderClientConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._debug = None
        self._account_id = None
        self._password = None
        self._username = None
        self._subtype = None
        self.discriminator = 'subtype'

        if debug is not None:
            self.debug = debug
        self.account_id = account_id
        self.password = password
        self.username = username
        self.subtype = subtype

    @property
    def debug(self):
        """Gets the debug of this AbstractProviderClientConfiguration.  # noqa: E501


        :return: The debug of this AbstractProviderClientConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._debug

    @debug.setter
    def debug(self, debug):
        """Sets the debug of this AbstractProviderClientConfiguration.


        :param debug: The debug of this AbstractProviderClientConfiguration.  # noqa: E501
        :type: bool
        """

        self._debug = debug

    @property
    def account_id(self):
        """Gets the account_id of this AbstractProviderClientConfiguration.  # noqa: E501


        :return: The account_id of this AbstractProviderClientConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AbstractProviderClientConfiguration.


        :param account_id: The account_id of this AbstractProviderClientConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_id is not None and len(account_id) > 255):
            raise ValueError("Invalid value for `account_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                account_id is not None and len(account_id) < 1):
            raise ValueError("Invalid value for `account_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._account_id = account_id

    @property
    def password(self):
        """Gets the password of this AbstractProviderClientConfiguration.  # noqa: E501


        :return: The password of this AbstractProviderClientConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AbstractProviderClientConfiguration.


        :param password: The password of this AbstractProviderClientConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) > 255):
            raise ValueError("Invalid value for `password`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                password is not None and len(password) < 1):
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `1`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this AbstractProviderClientConfiguration.  # noqa: E501


        :return: The username of this AbstractProviderClientConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AbstractProviderClientConfiguration.


        :param username: The username of this AbstractProviderClientConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) > 255):
            raise ValueError("Invalid value for `username`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                username is not None and len(username) < 1):
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

    @property
    def subtype(self):
        """Gets the subtype of this AbstractProviderClientConfiguration.  # noqa: E501


        :return: The subtype of this AbstractProviderClientConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this AbstractProviderClientConfiguration.


        :param subtype: The subtype of this AbstractProviderClientConfiguration.  # noqa: E501
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
        if not isinstance(other, AbstractProviderClientConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AbstractProviderClientConfiguration):
            return True

        return self.to_dict() != other.to_dict()
