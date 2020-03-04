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


class AwsCloudAllOf1(object):
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
        'access_key': 'str',
        'owner_id': 'str',
        'region_name': 'str',
        'secret_access_key': 'str'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'owner_id': 'ownerId',
        'region_name': 'regionName',
        'secret_access_key': 'secretAccessKey'
    }

    def __init__(self, access_key=None, owner_id=None, region_name=None, secret_access_key=None, local_vars_configuration=None):  # noqa: E501
        """AwsCloudAllOf1 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key = None
        self._owner_id = None
        self._region_name = None
        self._secret_access_key = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if owner_id is not None:
            self.owner_id = owner_id
        if region_name is not None:
            self.region_name = region_name
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key

    @property
    def access_key(self):
        """Gets the access_key of this AwsCloudAllOf1.  # noqa: E501


        :return: The access_key of this AwsCloudAllOf1.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this AwsCloudAllOf1.


        :param access_key: The access_key of this AwsCloudAllOf1.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def owner_id(self):
        """Gets the owner_id of this AwsCloudAllOf1.  # noqa: E501


        :return: The owner_id of this AwsCloudAllOf1.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this AwsCloudAllOf1.


        :param owner_id: The owner_id of this AwsCloudAllOf1.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def region_name(self):
        """Gets the region_name of this AwsCloudAllOf1.  # noqa: E501


        :return: The region_name of this AwsCloudAllOf1.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this AwsCloudAllOf1.


        :param region_name: The region_name of this AwsCloudAllOf1.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this AwsCloudAllOf1.  # noqa: E501


        :return: The secret_access_key of this AwsCloudAllOf1.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this AwsCloudAllOf1.


        :param secret_access_key: The secret_access_key of this AwsCloudAllOf1.  # noqa: E501
        :type: str
        """

        self._secret_access_key = secret_access_key

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
        if not isinstance(other, AwsCloudAllOf1):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsCloudAllOf1):
            return True

        return self.to_dict() != other.to_dict()
