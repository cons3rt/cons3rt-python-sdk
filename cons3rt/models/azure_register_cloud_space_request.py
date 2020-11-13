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


class AzureRegisterCloudSpaceRequest(object):
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
        'environment': 'str',
        'local_storage_resource_group_name': 'str',
        'local_storage_key': 'str',
        'region': 'str',
        'resource_group_name': 'str',
        'tenant_id': 'str',
        'virtual_network_name': 'str',
        'local_storage_name': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'environment': 'environment',
        'local_storage_resource_group_name': 'localStorageResourceGroupName',
        'local_storage_key': 'localStorageKey',
        'region': 'region',
        'resource_group_name': 'resourceGroupName',
        'tenant_id': 'tenantId',
        'virtual_network_name': 'virtualNetworkName',
        'local_storage_name': 'localStorageName'
    }

    def __init__(self, account_id=None, environment=None, local_storage_resource_group_name=None, local_storage_key=None, region=None, resource_group_name=None, tenant_id=None, virtual_network_name=None, local_storage_name=None, local_vars_configuration=None):  # noqa: E501
        """AzureRegisterCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._environment = None
        self._local_storage_resource_group_name = None
        self._local_storage_key = None
        self._region = None
        self._resource_group_name = None
        self._tenant_id = None
        self._virtual_network_name = None
        self._local_storage_name = None
        self.discriminator = None

        self.account_id = account_id
        self.environment = environment
        if local_storage_resource_group_name is not None:
            self.local_storage_resource_group_name = local_storage_resource_group_name
        if local_storage_key is not None:
            self.local_storage_key = local_storage_key
        self.region = region
        self.resource_group_name = resource_group_name
        self.tenant_id = tenant_id
        self.virtual_network_name = virtual_network_name
        if local_storage_name is not None:
            self.local_storage_name = local_storage_name

    @property
    def account_id(self):
        """Gets the account_id of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The account_id of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AzureRegisterCloudSpaceRequest.


        :param account_id: The account_id of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def environment(self):
        """Gets the environment of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The environment of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this AzureRegisterCloudSpaceRequest.


        :param environment: The environment of this AzureRegisterCloudSpaceRequest.  # noqa: E501
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
    def local_storage_resource_group_name(self):
        """Gets the local_storage_resource_group_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The local_storage_resource_group_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_storage_resource_group_name

    @local_storage_resource_group_name.setter
    def local_storage_resource_group_name(self, local_storage_resource_group_name):
        """Sets the local_storage_resource_group_name of this AzureRegisterCloudSpaceRequest.


        :param local_storage_resource_group_name: The local_storage_resource_group_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._local_storage_resource_group_name = local_storage_resource_group_name

    @property
    def local_storage_key(self):
        """Gets the local_storage_key of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The local_storage_key of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_storage_key

    @local_storage_key.setter
    def local_storage_key(self, local_storage_key):
        """Sets the local_storage_key of this AzureRegisterCloudSpaceRequest.


        :param local_storage_key: The local_storage_key of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._local_storage_key = local_storage_key

    @property
    def region(self):
        """Gets the region of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The region of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AzureRegisterCloudSpaceRequest.


        :param region: The region of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501
        allowed_values = ["US_EAST", "DOD_US_CENTRAL", "DOD_US_EAST", "GOV_US_VIRGINIA", "GOV_US_TEXAS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and region not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `region` ({0}), must be one of {1}"  # noqa: E501
                .format(region, allowed_values)
            )

        self._region = region

    @property
    def resource_group_name(self):
        """Gets the resource_group_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The resource_group_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this AzureRegisterCloudSpaceRequest.


        :param resource_group_name: The resource_group_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_group_name`, must not be `None`")  # noqa: E501

        self._resource_group_name = resource_group_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The tenant_id of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AzureRegisterCloudSpaceRequest.


        :param tenant_id: The tenant_id of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def virtual_network_name(self):
        """Gets the virtual_network_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The virtual_network_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtual_network_name

    @virtual_network_name.setter
    def virtual_network_name(self, virtual_network_name):
        """Sets the virtual_network_name of this AzureRegisterCloudSpaceRequest.


        :param virtual_network_name: The virtual_network_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and virtual_network_name is None:  # noqa: E501
            raise ValueError("Invalid value for `virtual_network_name`, must not be `None`")  # noqa: E501

        self._virtual_network_name = virtual_network_name

    @property
    def local_storage_name(self):
        """Gets the local_storage_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501


        :return: The local_storage_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_storage_name

    @local_storage_name.setter
    def local_storage_name(self, local_storage_name):
        """Sets the local_storage_name of this AzureRegisterCloudSpaceRequest.


        :param local_storage_name: The local_storage_name of this AzureRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._local_storage_name = local_storage_name

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
        if not isinstance(other, AzureRegisterCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureRegisterCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
