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


class InputAzureVirtualizationRealm(object):
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
        'public_container_url': 'str',
        'resource_group_name': 'str',
        'tenant_id': 'str',
        'virtual_network_name': 'str'
    }

    attribute_map = {
        'public_container_url': 'publicContainerUrl',
        'resource_group_name': 'resourceGroupName',
        'tenant_id': 'tenantId',
        'virtual_network_name': 'virtualNetworkName'
    }

    def __init__(self, public_container_url=None, resource_group_name=None, tenant_id=None, virtual_network_name=None, local_vars_configuration=None):  # noqa: E501
        """InputAzureVirtualizationRealm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._public_container_url = None
        self._resource_group_name = None
        self._tenant_id = None
        self._virtual_network_name = None
        self.discriminator = None

        if public_container_url is not None:
            self.public_container_url = public_container_url
        self.resource_group_name = resource_group_name
        self.tenant_id = tenant_id
        self.virtual_network_name = virtual_network_name

    @property
    def public_container_url(self):
        """Gets the public_container_url of this InputAzureVirtualizationRealm.  # noqa: E501


        :return: The public_container_url of this InputAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._public_container_url

    @public_container_url.setter
    def public_container_url(self, public_container_url):
        """Sets the public_container_url of this InputAzureVirtualizationRealm.


        :param public_container_url: The public_container_url of this InputAzureVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._public_container_url = public_container_url

    @property
    def resource_group_name(self):
        """Gets the resource_group_name of this InputAzureVirtualizationRealm.  # noqa: E501


        :return: The resource_group_name of this InputAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this InputAzureVirtualizationRealm.


        :param resource_group_name: The resource_group_name of this InputAzureVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_group_name`, must not be `None`")  # noqa: E501

        self._resource_group_name = resource_group_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this InputAzureVirtualizationRealm.  # noqa: E501


        :return: The tenant_id of this InputAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this InputAzureVirtualizationRealm.


        :param tenant_id: The tenant_id of this InputAzureVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def virtual_network_name(self):
        """Gets the virtual_network_name of this InputAzureVirtualizationRealm.  # noqa: E501


        :return: The virtual_network_name of this InputAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._virtual_network_name

    @virtual_network_name.setter
    def virtual_network_name(self, virtual_network_name):
        """Sets the virtual_network_name of this InputAzureVirtualizationRealm.


        :param virtual_network_name: The virtual_network_name of this InputAzureVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and virtual_network_name is None:  # noqa: E501
            raise ValueError("Invalid value for `virtual_network_name`, must not be `None`")  # noqa: E501

        self._virtual_network_name = virtual_network_name

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
        if not isinstance(other, InputAzureVirtualizationRealm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputAzureVirtualizationRealm):
            return True

        return self.to_dict() != other.to_dict()
