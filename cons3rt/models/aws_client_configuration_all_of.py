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


class AwsClientConfigurationAllOf(object):
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
        'session_token': 'str',
        'region_name': 'str'
    }

    attribute_map = {
        'session_token': 'sessionToken',
        'region_name': 'regionName'
    }

    def __init__(self, session_token=None, region_name=None, local_vars_configuration=None):  # noqa: E501
        """AwsClientConfigurationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._session_token = None
        self._region_name = None
        self.discriminator = None

        if session_token is not None:
            self.session_token = session_token
        if region_name is not None:
            self.region_name = region_name

    @property
    def session_token(self):
        """Gets the session_token of this AwsClientConfigurationAllOf.  # noqa: E501


        :return: The session_token of this AwsClientConfigurationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._session_token

    @session_token.setter
    def session_token(self, session_token):
        """Sets the session_token of this AwsClientConfigurationAllOf.


        :param session_token: The session_token of this AwsClientConfigurationAllOf.  # noqa: E501
        :type: str
        """

        self._session_token = session_token

    @property
    def region_name(self):
        """Gets the region_name of this AwsClientConfigurationAllOf.  # noqa: E501


        :return: The region_name of this AwsClientConfigurationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this AwsClientConfigurationAllOf.


        :param region_name: The region_name of this AwsClientConfigurationAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                region_name is not None and len(region_name) > 15):
            raise ValueError("Invalid value for `region_name`, length must be less than or equal to `15`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                region_name is not None and len(region_name) < 9):
            raise ValueError("Invalid value for `region_name`, length must be greater than or equal to `9`")  # noqa: E501

        self._region_name = region_name

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
        if not isinstance(other, AwsClientConfigurationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsClientConfigurationAllOf):
            return True

        return self.to_dict() != other.to_dict()
