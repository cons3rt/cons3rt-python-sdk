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


class VCloudRestCloudSpaceRequestAllOf(object):
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
        'provider_vdc_name': 'str',
        'vdc_network_pool_name': 'str',
        'username': 'str',
        'password': 'str',
        'email_address': 'str',
        'external_network_name': 'str',
        'local_catalog_name': 'str',
        'vdc_network_quota': 'int'
    }

    attribute_map = {
        'provider_vdc_name': 'providerVdcName',
        'vdc_network_pool_name': 'vdcNetworkPoolName',
        'username': 'username',
        'password': 'password',
        'email_address': 'emailAddress',
        'external_network_name': 'externalNetworkName',
        'local_catalog_name': 'localCatalogName',
        'vdc_network_quota': 'vdcNetworkQuota'
    }

    def __init__(self, provider_vdc_name=None, vdc_network_pool_name=None, username=None, password=None, email_address=None, external_network_name=None, local_catalog_name=None, vdc_network_quota=None, local_vars_configuration=None):  # noqa: E501
        """VCloudRestCloudSpaceRequestAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._provider_vdc_name = None
        self._vdc_network_pool_name = None
        self._username = None
        self._password = None
        self._email_address = None
        self._external_network_name = None
        self._local_catalog_name = None
        self._vdc_network_quota = None
        self.discriminator = None

        if provider_vdc_name is not None:
            self.provider_vdc_name = provider_vdc_name
        if vdc_network_pool_name is not None:
            self.vdc_network_pool_name = vdc_network_pool_name
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if email_address is not None:
            self.email_address = email_address
        if external_network_name is not None:
            self.external_network_name = external_network_name
        if local_catalog_name is not None:
            self.local_catalog_name = local_catalog_name
        if vdc_network_quota is not None:
            self.vdc_network_quota = vdc_network_quota

    @property
    def provider_vdc_name(self):
        """Gets the provider_vdc_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501


        :return: The provider_vdc_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._provider_vdc_name

    @provider_vdc_name.setter
    def provider_vdc_name(self, provider_vdc_name):
        """Sets the provider_vdc_name of this VCloudRestCloudSpaceRequestAllOf.


        :param provider_vdc_name: The provider_vdc_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._provider_vdc_name = provider_vdc_name

    @property
    def vdc_network_pool_name(self):
        """Gets the vdc_network_pool_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501


        :return: The vdc_network_pool_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._vdc_network_pool_name

    @vdc_network_pool_name.setter
    def vdc_network_pool_name(self, vdc_network_pool_name):
        """Sets the vdc_network_pool_name of this VCloudRestCloudSpaceRequestAllOf.


        :param vdc_network_pool_name: The vdc_network_pool_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._vdc_network_pool_name = vdc_network_pool_name

    @property
    def username(self):
        """Gets the username of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501


        :return: The username of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this VCloudRestCloudSpaceRequestAllOf.


        :param username: The username of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501


        :return: The password of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this VCloudRestCloudSpaceRequestAllOf.


        :param password: The password of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def email_address(self):
        """Gets the email_address of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501


        :return: The email_address of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this VCloudRestCloudSpaceRequestAllOf.


        :param email_address: The email_address of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def external_network_name(self):
        """Gets the external_network_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501


        :return: The external_network_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._external_network_name

    @external_network_name.setter
    def external_network_name(self, external_network_name):
        """Sets the external_network_name of this VCloudRestCloudSpaceRequestAllOf.


        :param external_network_name: The external_network_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._external_network_name = external_network_name

    @property
    def local_catalog_name(self):
        """Gets the local_catalog_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501


        :return: The local_catalog_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._local_catalog_name

    @local_catalog_name.setter
    def local_catalog_name(self, local_catalog_name):
        """Sets the local_catalog_name of this VCloudRestCloudSpaceRequestAllOf.


        :param local_catalog_name: The local_catalog_name of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._local_catalog_name = local_catalog_name

    @property
    def vdc_network_quota(self):
        """Gets the vdc_network_quota of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501


        :return: The vdc_network_quota of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: int
        """
        return self._vdc_network_quota

    @vdc_network_quota.setter
    def vdc_network_quota(self, vdc_network_quota):
        """Sets the vdc_network_quota of this VCloudRestCloudSpaceRequestAllOf.


        :param vdc_network_quota: The vdc_network_quota of this VCloudRestCloudSpaceRequestAllOf.  # noqa: E501
        :type: int
        """

        self._vdc_network_quota = vdc_network_quota

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
        if not isinstance(other, VCloudRestCloudSpaceRequestAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VCloudRestCloudSpaceRequestAllOf):
            return True

        return self.to_dict() != other.to_dict()
