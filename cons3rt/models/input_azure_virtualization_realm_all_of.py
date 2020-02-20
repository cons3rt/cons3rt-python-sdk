# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputAzureVirtualizationRealmAllOf(object):
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
        """InputAzureVirtualizationRealmAllOf - a model defined in OpenAPI"""  # noqa: E501
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
        if resource_group_name is not None:
            self.resource_group_name = resource_group_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if virtual_network_name is not None:
            self.virtual_network_name = virtual_network_name

    @property
    def public_container_url(self):
        """Gets the public_container_url of this InputAzureVirtualizationRealmAllOf.  # noqa: E501


        :return: The public_container_url of this InputAzureVirtualizationRealmAllOf.  # noqa: E501
        :rtype: str
        """
        return self._public_container_url

    @public_container_url.setter
    def public_container_url(self, public_container_url):
        """Sets the public_container_url of this InputAzureVirtualizationRealmAllOf.


        :param public_container_url: The public_container_url of this InputAzureVirtualizationRealmAllOf.  # noqa: E501
        :type: str
        """

        self._public_container_url = public_container_url

    @property
    def resource_group_name(self):
        """Gets the resource_group_name of this InputAzureVirtualizationRealmAllOf.  # noqa: E501


        :return: The resource_group_name of this InputAzureVirtualizationRealmAllOf.  # noqa: E501
        :rtype: str
        """
        return self._resource_group_name

    @resource_group_name.setter
    def resource_group_name(self, resource_group_name):
        """Sets the resource_group_name of this InputAzureVirtualizationRealmAllOf.


        :param resource_group_name: The resource_group_name of this InputAzureVirtualizationRealmAllOf.  # noqa: E501
        :type: str
        """

        self._resource_group_name = resource_group_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this InputAzureVirtualizationRealmAllOf.  # noqa: E501


        :return: The tenant_id of this InputAzureVirtualizationRealmAllOf.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this InputAzureVirtualizationRealmAllOf.


        :param tenant_id: The tenant_id of this InputAzureVirtualizationRealmAllOf.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def virtual_network_name(self):
        """Gets the virtual_network_name of this InputAzureVirtualizationRealmAllOf.  # noqa: E501


        :return: The virtual_network_name of this InputAzureVirtualizationRealmAllOf.  # noqa: E501
        :rtype: str
        """
        return self._virtual_network_name

    @virtual_network_name.setter
    def virtual_network_name(self, virtual_network_name):
        """Sets the virtual_network_name of this InputAzureVirtualizationRealmAllOf.


        :param virtual_network_name: The virtual_network_name of this InputAzureVirtualizationRealmAllOf.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, InputAzureVirtualizationRealmAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputAzureVirtualizationRealmAllOf):
            return True

        return self.to_dict() != other.to_dict()
