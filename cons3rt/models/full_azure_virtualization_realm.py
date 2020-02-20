# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class FullAzureVirtualizationRealm(object):
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
        'environment': 'str',
        'public_container_url': 'str',
        'region': 'str',
        'resource_group_name': 'str',
        'tenant_id': 'str',
        'virtual_network_name': 'str'
    }

    attribute_map = {
        'environment': 'environment',
        'public_container_url': 'publicContainerUrl',
        'region': 'region',
        'resource_group_name': 'resourceGroupName',
        'tenant_id': 'tenantId',
        'virtual_network_name': 'virtualNetworkName'
    }

    def __init__(self, environment=None, public_container_url=None, region=None, resource_group_name=None, tenant_id=None, virtual_network_name=None, local_vars_configuration=None):  # noqa: E501
        """FullAzureVirtualizationRealm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._environment = None
        self._public_container_url = None
        self._region = None
        self._resource_group_name = None
        self._tenant_id = None
        self._virtual_network_name = None
        self.discriminator = None

        self.environment = environment
        if public_container_url is not None:
            self.public_container_url = public_container_url
        self.region = region
        self.resource_group_name = resource_group_name
        self.tenant_id = tenant_id
        self.virtual_network_name = virtual_network_name

    @property
    def environment(self):
        """Gets the environment of this FullAzureVirtualizationRealm.  # noqa: E501


        :return: The environment of this FullAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this FullAzureVirtualizationRealm.


        :param environment: The environment of this FullAzureVirtualizationRealm.  # noqa: E501
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
    def public_container_url(self):
        """Gets the public_container_url of this FullAzureVirtualizationRealm.  # noqa: E501


        :return: The public_container_url of this FullAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._public_container_url

    @public_container_url.setter
    def public_container_url(self, public_container_url):
        """Sets the public_container_url of this FullAzureVirtualizationRealm.


        :param public_container_url: The public_container_url of this FullAzureVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._public_container_url = public_container_url

    @property
    def region(self):
        """Gets the region of this FullAzureVirtualizationRealm.  # noqa: E501


        :return: The region of this FullAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this FullAzureVirtualizationRealm.


        :param region: The region of this FullAzureVirtualizationRealm.  # noqa: E501
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
        """Gets the resource_group_name of this FullAzureVirtualizationRealm.  # noqa: E501


        :return: The resource_group_name of this FullAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this FullAzureVirtualizationRealm.


        :param resource_group_name: The resource_group_name of this FullAzureVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_group_name`, must not be `None`")  # noqa: E501

        self._resource_group_name = resource_group_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this FullAzureVirtualizationRealm.  # noqa: E501


        :return: The tenant_id of this FullAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this FullAzureVirtualizationRealm.


        :param tenant_id: The tenant_id of this FullAzureVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def virtual_network_name(self):
        """Gets the virtual_network_name of this FullAzureVirtualizationRealm.  # noqa: E501


        :return: The virtual_network_name of this FullAzureVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._virtual_network_name

    @virtual_network_name.setter
    def virtual_network_name(self, virtual_network_name):
        """Sets the virtual_network_name of this FullAzureVirtualizationRealm.


        :param virtual_network_name: The virtual_network_name of this FullAzureVirtualizationRealm.  # noqa: E501
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
        if not isinstance(other, FullAzureVirtualizationRealm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullAzureVirtualizationRealm):
            return True

        return self.to_dict() != other.to_dict()
