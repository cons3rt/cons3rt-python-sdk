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


class AwsRegisterCloudSpaceRequestAllOf(object):
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
        'account_id': 'str',
        'region': 'str',
        'vpc_id': 'str',
        'user_key_name': 'str',
        'network_security_group_map': 'dict(str, str)'
    }

    attribute_map = {
        'account_id': 'accountId',
        'region': 'region',
        'vpc_id': 'vpcId',
        'user_key_name': 'userKeyName',
        'network_security_group_map': 'networkSecurityGroupMap'
    }

    def __init__(self, account_id=None, region=None, vpc_id=None, user_key_name=None, network_security_group_map=None, local_vars_configuration=None):  # noqa: E501
        """AwsRegisterCloudSpaceRequestAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._region = None
        self._vpc_id = None
        self._user_key_name = None
        self._network_security_group_map = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if region is not None:
            self.region = region
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if user_key_name is not None:
            self.user_key_name = user_key_name
        if network_security_group_map is not None:
            self.network_security_group_map = network_security_group_map

    @property
    def account_id(self):
        """Gets the account_id of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501


        :return: The account_id of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AwsRegisterCloudSpaceRequestAllOf.


        :param account_id: The account_id of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def region(self):
        """Gets the region of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501


        :return: The region of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AwsRegisterCloudSpaceRequestAllOf.


        :param region: The region of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501


        :return: The vpc_id of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AwsRegisterCloudSpaceRequestAllOf.


        :param vpc_id: The vpc_id of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def user_key_name(self):
        """Gets the user_key_name of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501


        :return: The user_key_name of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._user_key_name

    @user_key_name.setter
    def user_key_name(self, user_key_name):
        """Sets the user_key_name of this AwsRegisterCloudSpaceRequestAllOf.


        :param user_key_name: The user_key_name of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._user_key_name = user_key_name

    @property
    def network_security_group_map(self):
        """Gets the network_security_group_map of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501


        :return: The network_security_group_map of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._network_security_group_map

    @network_security_group_map.setter
    def network_security_group_map(self, network_security_group_map):
        """Sets the network_security_group_map of this AwsRegisterCloudSpaceRequestAllOf.


        :param network_security_group_map: The network_security_group_map of this AwsRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :type: dict(str, str)
        """

        self._network_security_group_map = network_security_group_map

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
        if not isinstance(other, AwsRegisterCloudSpaceRequestAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsRegisterCloudSpaceRequestAllOf):
            return True

        return self.to_dict() != other.to_dict()
