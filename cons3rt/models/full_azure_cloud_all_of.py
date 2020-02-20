# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class FullAzureCloudAllOf(object):
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
        """FullAzureCloudAllOf - a model defined in OpenAPI"""  # noqa: E501
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

        if client_id is not None:
            self.client_id = client_id
        if environment is not None:
            self.environment = environment
        if region_name is not None:
            self.region_name = region_name
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if tenant is not None:
            self.tenant = tenant
        if public_container_url is not None:
            self.public_container_url = public_container_url

    @property
    def client_id(self):
        """Gets the client_id of this FullAzureCloudAllOf.  # noqa: E501


        :return: The client_id of this FullAzureCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this FullAzureCloudAllOf.


        :param client_id: The client_id of this FullAzureCloudAllOf.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def environment(self):
        """Gets the environment of this FullAzureCloudAllOf.  # noqa: E501


        :return: The environment of this FullAzureCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this FullAzureCloudAllOf.


        :param environment: The environment of this FullAzureCloudAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["AZURE", "AZURE_US_GOVERNMENT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and environment not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `environment` ({0}), must be one of {1}"  # noqa: E501
                .format(environment, allowed_values)
            )

        self._environment = environment

    @property
    def region_name(self):
        """Gets the region_name of this FullAzureCloudAllOf.  # noqa: E501


        :return: The region_name of this FullAzureCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this FullAzureCloudAllOf.


        :param region_name: The region_name of this FullAzureCloudAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["US_EAST", "DOD_US_CENTRAL", "DOD_US_EAST", "GOV_US_VIRGINIA", "GOV_US_TEXAS"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and region_name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `region_name` ({0}), must be one of {1}"  # noqa: E501
                .format(region_name, allowed_values)
            )

        self._region_name = region_name

    @property
    def subscription_id(self):
        """Gets the subscription_id of this FullAzureCloudAllOf.  # noqa: E501


        :return: The subscription_id of this FullAzureCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this FullAzureCloudAllOf.


        :param subscription_id: The subscription_id of this FullAzureCloudAllOf.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def tenant(self):
        """Gets the tenant of this FullAzureCloudAllOf.  # noqa: E501


        :return: The tenant of this FullAzureCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this FullAzureCloudAllOf.


        :param tenant: The tenant of this FullAzureCloudAllOf.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

    @property
    def public_container_url(self):
        """Gets the public_container_url of this FullAzureCloudAllOf.  # noqa: E501


        :return: The public_container_url of this FullAzureCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._public_container_url

    @public_container_url.setter
    def public_container_url(self, public_container_url):
        """Sets the public_container_url of this FullAzureCloudAllOf.


        :param public_container_url: The public_container_url of this FullAzureCloudAllOf.  # noqa: E501
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
        if not isinstance(other, FullAzureCloudAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullAzureCloudAllOf):
            return True

        return self.to_dict() != other.to_dict()
