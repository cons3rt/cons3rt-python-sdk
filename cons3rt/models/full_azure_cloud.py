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


class FullAzureCloud(object):
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
        'client_id': 'str',
        'environment': 'str',
        'region_name': 'str',
        'subscription_id': 'str',
        'tenant': 'str',
        'public_container_url': 'str'
    }

    attribute_map = {
        'client_id': 'clientId',
        'environment': 'environment',
        'region_name': 'regionName',
        'subscription_id': 'subscriptionId',
        'tenant': 'tenant',
        'public_container_url': 'publicContainerUrl'
    }

    def __init__(self, client_id=None, environment=None, region_name=None, subscription_id=None, tenant=None, public_container_url=None, local_vars_configuration=None):  # noqa: E501
        """FullAzureCloud - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client_id = None
        self._environment = None
        self._region_name = None
        self._subscription_id = None
        self._tenant = None
        self._public_container_url = None
        self.discriminator = None

        self.client_id = client_id
        self.environment = environment
        self.region_name = region_name
        self.subscription_id = subscription_id
        self.tenant = tenant
        if public_container_url is not None:
            self.public_container_url = public_container_url

    @property
    def client_id(self):
        """Gets the client_id of this FullAzureCloud.  # noqa: E501


        :return: The client_id of this FullAzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this FullAzureCloud.


        :param client_id: The client_id of this FullAzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def environment(self):
        """Gets the environment of this FullAzureCloud.  # noqa: E501


        :return: The environment of this FullAzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this FullAzureCloud.


        :param environment: The environment of this FullAzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and environment is None:  # noqa: E501
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501
        allowed_values = ["AZURE", "AZURE_US_GOVERNMENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and environment not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `environment` ({0}), must be one of {1}"  # noqa: E501
                .format(environment, allowed_values)
            )

        self._environment = environment

    @property
    def region_name(self):
        """Gets the region_name of this FullAzureCloud.  # noqa: E501


        :return: The region_name of this FullAzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this FullAzureCloud.


        :param region_name: The region_name of this FullAzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and region_name is None:  # noqa: E501
            raise ValueError("Invalid value for `region_name`, must not be `None`")  # noqa: E501
        allowed_values = ["US_EAST", "DOD_US_CENTRAL", "DOD_US_EAST", "GOV_US_VIRGINIA", "GOV_US_TEXAS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and region_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `region_name` ({0}), must be one of {1}"  # noqa: E501
                .format(region_name, allowed_values)
            )

        self._region_name = region_name

    @property
    def subscription_id(self):
        """Gets the subscription_id of this FullAzureCloud.  # noqa: E501


        :return: The subscription_id of this FullAzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this FullAzureCloud.


        :param subscription_id: The subscription_id of this FullAzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subscription_id is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def tenant(self):
        """Gets the tenant of this FullAzureCloud.  # noqa: E501


        :return: The tenant of this FullAzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this FullAzureCloud.


        :param tenant: The tenant of this FullAzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

    @property
    def public_container_url(self):
        """Gets the public_container_url of this FullAzureCloud.  # noqa: E501


        :return: The public_container_url of this FullAzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._public_container_url

    @public_container_url.setter
    def public_container_url(self, public_container_url):
        """Sets the public_container_url of this FullAzureCloud.


        :param public_container_url: The public_container_url of this FullAzureCloud.  # noqa: E501
        :type: str
        """

        self._public_container_url = public_container_url

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
        if not isinstance(other, FullAzureCloud):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullAzureCloud):
            return True

        return self.to_dict() != other.to_dict()
