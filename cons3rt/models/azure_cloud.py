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


class AzureCloud(object):
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
        'cloud_type': 'str',
        'description': 'str',
        'name': 'str',
        'external_ip_addresses': 'list[str]',
        'external_ip_source': 'str',
        'features': 'CloudFeatures',
        'id': 'int',
        'linux_repository_url': 'str',
        'maximum_impact_level': 'str',
        'networks': 'list[Network]',
        'owning_team': 'Team',
        'state': 'str',
        'template_virtualization_realm': 'VirtualizationRealm',
        'virtualization_realms': 'list[VirtualizationRealm]',
        'subtype': 'str',
        'client_id': 'str',
        'environment': 'str',
        'region_name': 'str',
        'secret_access_key': 'str',
        'subscription_id': 'str',
        'tenant': 'str',
        'public_container_url': 'str'
    }

    attribute_map = {
        'cloud_type': 'cloudType',
        'description': 'description',
        'name': 'name',
        'external_ip_addresses': 'externalIpAddresses',
        'external_ip_source': 'externalIpSource',
        'features': 'features',
        'id': 'id',
        'linux_repository_url': 'linuxRepositoryUrl',
        'maximum_impact_level': 'maximumImpactLevel',
        'networks': 'networks',
        'owning_team': 'owningTeam',
        'state': 'state',
        'template_virtualization_realm': 'templateVirtualizationRealm',
        'virtualization_realms': 'virtualizationRealms',
        'subtype': 'subtype',
        'client_id': 'clientId',
        'environment': 'environment',
        'region_name': 'regionName',
        'secret_access_key': 'secretAccessKey',
        'subscription_id': 'subscriptionId',
        'tenant': 'tenant',
        'public_container_url': 'publicContainerUrl'
    }

    def __init__(self, cloud_type=None, description=None, name=None, external_ip_addresses=None, external_ip_source=None, features=None, id=None, linux_repository_url=None, maximum_impact_level=None, networks=None, owning_team=None, state=None, template_virtualization_realm=None, virtualization_realms=None, subtype=None, client_id=None, environment=None, region_name=None, secret_access_key=None, subscription_id=None, tenant=None, public_container_url=None, local_vars_configuration=None):  # noqa: E501
        """AzureCloud - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_type = None
        self._description = None
        self._name = None
        self._external_ip_addresses = None
        self._external_ip_source = None
        self._features = None
        self._id = None
        self._linux_repository_url = None
        self._maximum_impact_level = None
        self._networks = None
        self._owning_team = None
        self._state = None
        self._template_virtualization_realm = None
        self._virtualization_realms = None
        self._subtype = None
        self._client_id = None
        self._environment = None
        self._region_name = None
        self._secret_access_key = None
        self._subscription_id = None
        self._tenant = None
        self._public_container_url = None
        self.discriminator = None

        if cloud_type is not None:
            self.cloud_type = cloud_type
        self.description = description
        self.name = name
        if external_ip_addresses is not None:
            self.external_ip_addresses = external_ip_addresses
        self.external_ip_source = external_ip_source
        if features is not None:
            self.features = features
        if id is not None:
            self.id = id
        if linux_repository_url is not None:
            self.linux_repository_url = linux_repository_url
        self.maximum_impact_level = maximum_impact_level
        if networks is not None:
            self.networks = networks
        self.owning_team = owning_team
        if state is not None:
            self.state = state
        if template_virtualization_realm is not None:
            self.template_virtualization_realm = template_virtualization_realm
        if virtualization_realms is not None:
            self.virtualization_realms = virtualization_realms
        self.subtype = subtype
        self.client_id = client_id
        self.environment = environment
        self.region_name = region_name
        self.secret_access_key = secret_access_key
        self.subscription_id = subscription_id
        self.tenant = tenant
        if public_container_url is not None:
            self.public_container_url = public_container_url

    @property
    def cloud_type(self):
        """Gets the cloud_type of this AzureCloud.  # noqa: E501


        :return: The cloud_type of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this AzureCloud.


        :param cloud_type: The cloud_type of this AzureCloud.  # noqa: E501
        :type: str
        """
        allowed_values = ["AwsCloud", "AzureCloud", "CloudStackCloud", "OpenStackCloud", "VCloudCloud"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cloud_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cloud_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud_type, allowed_values)
            )

        self._cloud_type = cloud_type

    @property
    def description(self):
        """Gets the description of this AzureCloud.  # noqa: E501


        :return: The description of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AzureCloud.


        :param description: The description of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this AzureCloud.  # noqa: E501


        :return: The name of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AzureCloud.


        :param name: The name of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def external_ip_addresses(self):
        """Gets the external_ip_addresses of this AzureCloud.  # noqa: E501


        :return: The external_ip_addresses of this AzureCloud.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_ip_addresses

    @external_ip_addresses.setter
    def external_ip_addresses(self, external_ip_addresses):
        """Sets the external_ip_addresses of this AzureCloud.


        :param external_ip_addresses: The external_ip_addresses of this AzureCloud.  # noqa: E501
        :type: list[str]
        """

        self._external_ip_addresses = external_ip_addresses

    @property
    def external_ip_source(self):
        """Gets the external_ip_source of this AzureCloud.  # noqa: E501


        :return: The external_ip_source of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_source

    @external_ip_source.setter
    def external_ip_source(self, external_ip_source):
        """Sets the external_ip_source of this AzureCloud.


        :param external_ip_source: The external_ip_source of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_ip_source is None:  # noqa: E501
            raise ValueError("Invalid value for `external_ip_source`, must not be `None`")  # noqa: E501
        allowed_values = ["ON_DEMAND", "POOL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and external_ip_source not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `external_ip_source` ({0}), must be one of {1}"  # noqa: E501
                .format(external_ip_source, allowed_values)
            )

        self._external_ip_source = external_ip_source

    @property
    def features(self):
        """Gets the features of this AzureCloud.  # noqa: E501


        :return: The features of this AzureCloud.  # noqa: E501
        :rtype: CloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this AzureCloud.


        :param features: The features of this AzureCloud.  # noqa: E501
        :type: CloudFeatures
        """

        self._features = features

    @property
    def id(self):
        """Gets the id of this AzureCloud.  # noqa: E501


        :return: The id of this AzureCloud.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AzureCloud.


        :param id: The id of this AzureCloud.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def linux_repository_url(self):
        """Gets the linux_repository_url of this AzureCloud.  # noqa: E501


        :return: The linux_repository_url of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._linux_repository_url

    @linux_repository_url.setter
    def linux_repository_url(self, linux_repository_url):
        """Sets the linux_repository_url of this AzureCloud.


        :param linux_repository_url: The linux_repository_url of this AzureCloud.  # noqa: E501
        :type: str
        """

        self._linux_repository_url = linux_repository_url

    @property
    def maximum_impact_level(self):
        """Gets the maximum_impact_level of this AzureCloud.  # noqa: E501


        :return: The maximum_impact_level of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._maximum_impact_level

    @maximum_impact_level.setter
    def maximum_impact_level(self, maximum_impact_level):
        """Sets the maximum_impact_level of this AzureCloud.


        :param maximum_impact_level: The maximum_impact_level of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and maximum_impact_level is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_impact_level`, must not be `None`")  # noqa: E501
        allowed_values = ["NONE", "FEDRAMP_LOW", "FEDRAMP_MODERATE_DOD_LEVEL_2", "FEDRAMP_HIGH_DOD_LEVEL_4", "DOD_LEVEL_5", "DOD_LEVEL_6"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and maximum_impact_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `maximum_impact_level` ({0}), must be one of {1}"  # noqa: E501
                .format(maximum_impact_level, allowed_values)
            )

        self._maximum_impact_level = maximum_impact_level

    @property
    def networks(self):
        """Gets the networks of this AzureCloud.  # noqa: E501


        :return: The networks of this AzureCloud.  # noqa: E501
        :rtype: list[Network]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this AzureCloud.


        :param networks: The networks of this AzureCloud.  # noqa: E501
        :type: list[Network]
        """

        self._networks = networks

    @property
    def owning_team(self):
        """Gets the owning_team of this AzureCloud.  # noqa: E501


        :return: The owning_team of this AzureCloud.  # noqa: E501
        :rtype: Team
        """
        return self._owning_team

    @owning_team.setter
    def owning_team(self, owning_team):
        """Sets the owning_team of this AzureCloud.


        :param owning_team: The owning_team of this AzureCloud.  # noqa: E501
        :type: Team
        """
        if self.local_vars_configuration.client_side_validation and owning_team is None:  # noqa: E501
            raise ValueError("Invalid value for `owning_team`, must not be `None`")  # noqa: E501

        self._owning_team = owning_team

    @property
    def state(self):
        """Gets the state of this AzureCloud.  # noqa: E501


        :return: The state of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AzureCloud.


        :param state: The state of this AzureCloud.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "ENTERING_MAINTENANCE", "MAINTENANCE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def template_virtualization_realm(self):
        """Gets the template_virtualization_realm of this AzureCloud.  # noqa: E501


        :return: The template_virtualization_realm of this AzureCloud.  # noqa: E501
        :rtype: VirtualizationRealm
        """
        return self._template_virtualization_realm

    @template_virtualization_realm.setter
    def template_virtualization_realm(self, template_virtualization_realm):
        """Sets the template_virtualization_realm of this AzureCloud.


        :param template_virtualization_realm: The template_virtualization_realm of this AzureCloud.  # noqa: E501
        :type: VirtualizationRealm
        """

        self._template_virtualization_realm = template_virtualization_realm

    @property
    def virtualization_realms(self):
        """Gets the virtualization_realms of this AzureCloud.  # noqa: E501


        :return: The virtualization_realms of this AzureCloud.  # noqa: E501
        :rtype: list[VirtualizationRealm]
        """
        return self._virtualization_realms

    @virtualization_realms.setter
    def virtualization_realms(self, virtualization_realms):
        """Sets the virtualization_realms of this AzureCloud.


        :param virtualization_realms: The virtualization_realms of this AzureCloud.  # noqa: E501
        :type: list[VirtualizationRealm]
        """

        self._virtualization_realms = virtualization_realms

    @property
    def subtype(self):
        """Gets the subtype of this AzureCloud.  # noqa: E501


        :return: The subtype of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this AzureCloud.


        :param subtype: The subtype of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def client_id(self):
        """Gets the client_id of this AzureCloud.  # noqa: E501


        :return: The client_id of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this AzureCloud.


        :param client_id: The client_id of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501

        self._client_id = client_id

    @property
    def environment(self):
        """Gets the environment of this AzureCloud.  # noqa: E501


        :return: The environment of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this AzureCloud.


        :param environment: The environment of this AzureCloud.  # noqa: E501
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
        """Gets the region_name of this AzureCloud.  # noqa: E501


        :return: The region_name of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this AzureCloud.


        :param region_name: The region_name of this AzureCloud.  # noqa: E501
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
    def secret_access_key(self):
        """Gets the secret_access_key of this AzureCloud.  # noqa: E501


        :return: The secret_access_key of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this AzureCloud.


        :param secret_access_key: The secret_access_key of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secret_access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `secret_access_key`, must not be `None`")  # noqa: E501

        self._secret_access_key = secret_access_key

    @property
    def subscription_id(self):
        """Gets the subscription_id of this AzureCloud.  # noqa: E501


        :return: The subscription_id of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this AzureCloud.


        :param subscription_id: The subscription_id of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subscription_id is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def tenant(self):
        """Gets the tenant of this AzureCloud.  # noqa: E501


        :return: The tenant of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this AzureCloud.


        :param tenant: The tenant of this AzureCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

    @property
    def public_container_url(self):
        """Gets the public_container_url of this AzureCloud.  # noqa: E501


        :return: The public_container_url of this AzureCloud.  # noqa: E501
        :rtype: str
        """
        return self._public_container_url

    @public_container_url.setter
    def public_container_url(self, public_container_url):
        """Sets the public_container_url of this AzureCloud.


        :param public_container_url: The public_container_url of this AzureCloud.  # noqa: E501
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
        if not isinstance(other, AzureCloud):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureCloud):
            return True

        return self.to_dict() != other.to_dict()
