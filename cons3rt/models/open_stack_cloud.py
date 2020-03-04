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


class OpenStackCloud(object):
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
        'domain_name': 'str',
        'keystone_hostname': 'str',
        'keystone_password': 'str',
        'keystone_port': 'int',
        'keystone_protocol': 'str',
        'keystone_username': 'str',
        'keystone_version': 'str',
        'nat_image_id': 'str',
        'nat_instance_type': 'str',
        'tenant': 'str',
        'tenant_id': 'str'
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
        'domain_name': 'domainName',
        'keystone_hostname': 'keystoneHostname',
        'keystone_password': 'keystonePassword',
        'keystone_port': 'keystonePort',
        'keystone_protocol': 'keystoneProtocol',
        'keystone_username': 'keystoneUsername',
        'keystone_version': 'keystoneVersion',
        'nat_image_id': 'natImageId',
        'nat_instance_type': 'natInstanceType',
        'tenant': 'tenant',
        'tenant_id': 'tenantId'
    }

    def __init__(self, cloud_type=None, description=None, name=None, external_ip_addresses=None, external_ip_source=None, features=None, id=None, linux_repository_url=None, maximum_impact_level=None, networks=None, owning_team=None, state=None, template_virtualization_realm=None, virtualization_realms=None, subtype=None, domain_name=None, keystone_hostname=None, keystone_password=None, keystone_port=None, keystone_protocol=None, keystone_username=None, keystone_version=None, nat_image_id=None, nat_instance_type=None, tenant=None, tenant_id=None, local_vars_configuration=None):  # noqa: E501
        """OpenStackCloud - a model defined in OpenAPI"""  # noqa: E501
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
        self._domain_name = None
        self._keystone_hostname = None
        self._keystone_password = None
        self._keystone_port = None
        self._keystone_protocol = None
        self._keystone_username = None
        self._keystone_version = None
        self._nat_image_id = None
        self._nat_instance_type = None
        self._tenant = None
        self._tenant_id = None
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
        if domain_name is not None:
            self.domain_name = domain_name
        self.keystone_hostname = keystone_hostname
        self.keystone_password = keystone_password
        self.keystone_port = keystone_port
        self.keystone_protocol = keystone_protocol
        self.keystone_username = keystone_username
        self.keystone_version = keystone_version
        self.nat_image_id = nat_image_id
        self.nat_instance_type = nat_instance_type
        self.tenant = tenant
        self.tenant_id = tenant_id

    @property
    def cloud_type(self):
        """Gets the cloud_type of this OpenStackCloud.  # noqa: E501


        :return: The cloud_type of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._cloud_type

    @cloud_type.setter
    def cloud_type(self, cloud_type):
        """Sets the cloud_type of this OpenStackCloud.


        :param cloud_type: The cloud_type of this OpenStackCloud.  # noqa: E501
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
        """Gets the description of this OpenStackCloud.  # noqa: E501


        :return: The description of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this OpenStackCloud.


        :param description: The description of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this OpenStackCloud.  # noqa: E501


        :return: The name of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenStackCloud.


        :param name: The name of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def external_ip_addresses(self):
        """Gets the external_ip_addresses of this OpenStackCloud.  # noqa: E501


        :return: The external_ip_addresses of this OpenStackCloud.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_ip_addresses

    @external_ip_addresses.setter
    def external_ip_addresses(self, external_ip_addresses):
        """Sets the external_ip_addresses of this OpenStackCloud.


        :param external_ip_addresses: The external_ip_addresses of this OpenStackCloud.  # noqa: E501
        :type: list[str]
        """

        self._external_ip_addresses = external_ip_addresses

    @property
    def external_ip_source(self):
        """Gets the external_ip_source of this OpenStackCloud.  # noqa: E501


        :return: The external_ip_source of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._external_ip_source

    @external_ip_source.setter
    def external_ip_source(self, external_ip_source):
        """Sets the external_ip_source of this OpenStackCloud.


        :param external_ip_source: The external_ip_source of this OpenStackCloud.  # noqa: E501
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
        """Gets the features of this OpenStackCloud.  # noqa: E501


        :return: The features of this OpenStackCloud.  # noqa: E501
        :rtype: CloudFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this OpenStackCloud.


        :param features: The features of this OpenStackCloud.  # noqa: E501
        :type: CloudFeatures
        """

        self._features = features

    @property
    def id(self):
        """Gets the id of this OpenStackCloud.  # noqa: E501


        :return: The id of this OpenStackCloud.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OpenStackCloud.


        :param id: The id of this OpenStackCloud.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def linux_repository_url(self):
        """Gets the linux_repository_url of this OpenStackCloud.  # noqa: E501


        :return: The linux_repository_url of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._linux_repository_url

    @linux_repository_url.setter
    def linux_repository_url(self, linux_repository_url):
        """Sets the linux_repository_url of this OpenStackCloud.


        :param linux_repository_url: The linux_repository_url of this OpenStackCloud.  # noqa: E501
        :type: str
        """

        self._linux_repository_url = linux_repository_url

    @property
    def maximum_impact_level(self):
        """Gets the maximum_impact_level of this OpenStackCloud.  # noqa: E501


        :return: The maximum_impact_level of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._maximum_impact_level

    @maximum_impact_level.setter
    def maximum_impact_level(self, maximum_impact_level):
        """Sets the maximum_impact_level of this OpenStackCloud.


        :param maximum_impact_level: The maximum_impact_level of this OpenStackCloud.  # noqa: E501
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
        """Gets the networks of this OpenStackCloud.  # noqa: E501


        :return: The networks of this OpenStackCloud.  # noqa: E501
        :rtype: list[Network]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this OpenStackCloud.


        :param networks: The networks of this OpenStackCloud.  # noqa: E501
        :type: list[Network]
        """

        self._networks = networks

    @property
    def owning_team(self):
        """Gets the owning_team of this OpenStackCloud.  # noqa: E501


        :return: The owning_team of this OpenStackCloud.  # noqa: E501
        :rtype: Team
        """
        return self._owning_team

    @owning_team.setter
    def owning_team(self, owning_team):
        """Sets the owning_team of this OpenStackCloud.


        :param owning_team: The owning_team of this OpenStackCloud.  # noqa: E501
        :type: Team
        """
        if self.local_vars_configuration.client_side_validation and owning_team is None:  # noqa: E501
            raise ValueError("Invalid value for `owning_team`, must not be `None`")  # noqa: E501

        self._owning_team = owning_team

    @property
    def state(self):
        """Gets the state of this OpenStackCloud.  # noqa: E501


        :return: The state of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this OpenStackCloud.


        :param state: The state of this OpenStackCloud.  # noqa: E501
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
        """Gets the template_virtualization_realm of this OpenStackCloud.  # noqa: E501


        :return: The template_virtualization_realm of this OpenStackCloud.  # noqa: E501
        :rtype: VirtualizationRealm
        """
        return self._template_virtualization_realm

    @template_virtualization_realm.setter
    def template_virtualization_realm(self, template_virtualization_realm):
        """Sets the template_virtualization_realm of this OpenStackCloud.


        :param template_virtualization_realm: The template_virtualization_realm of this OpenStackCloud.  # noqa: E501
        :type: VirtualizationRealm
        """

        self._template_virtualization_realm = template_virtualization_realm

    @property
    def virtualization_realms(self):
        """Gets the virtualization_realms of this OpenStackCloud.  # noqa: E501


        :return: The virtualization_realms of this OpenStackCloud.  # noqa: E501
        :rtype: list[VirtualizationRealm]
        """
        return self._virtualization_realms

    @virtualization_realms.setter
    def virtualization_realms(self, virtualization_realms):
        """Sets the virtualization_realms of this OpenStackCloud.


        :param virtualization_realms: The virtualization_realms of this OpenStackCloud.  # noqa: E501
        :type: list[VirtualizationRealm]
        """

        self._virtualization_realms = virtualization_realms

    @property
    def subtype(self):
        """Gets the subtype of this OpenStackCloud.  # noqa: E501


        :return: The subtype of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this OpenStackCloud.


        :param subtype: The subtype of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def domain_name(self):
        """Gets the domain_name of this OpenStackCloud.  # noqa: E501


        :return: The domain_name of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this OpenStackCloud.


        :param domain_name: The domain_name of this OpenStackCloud.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def keystone_hostname(self):
        """Gets the keystone_hostname of this OpenStackCloud.  # noqa: E501


        :return: The keystone_hostname of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._keystone_hostname

    @keystone_hostname.setter
    def keystone_hostname(self, keystone_hostname):
        """Sets the keystone_hostname of this OpenStackCloud.


        :param keystone_hostname: The keystone_hostname of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and keystone_hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `keystone_hostname`, must not be `None`")  # noqa: E501

        self._keystone_hostname = keystone_hostname

    @property
    def keystone_password(self):
        """Gets the keystone_password of this OpenStackCloud.  # noqa: E501


        :return: The keystone_password of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._keystone_password

    @keystone_password.setter
    def keystone_password(self, keystone_password):
        """Sets the keystone_password of this OpenStackCloud.


        :param keystone_password: The keystone_password of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and keystone_password is None:  # noqa: E501
            raise ValueError("Invalid value for `keystone_password`, must not be `None`")  # noqa: E501

        self._keystone_password = keystone_password

    @property
    def keystone_port(self):
        """Gets the keystone_port of this OpenStackCloud.  # noqa: E501


        :return: The keystone_port of this OpenStackCloud.  # noqa: E501
        :rtype: int
        """
        return self._keystone_port

    @keystone_port.setter
    def keystone_port(self, keystone_port):
        """Sets the keystone_port of this OpenStackCloud.


        :param keystone_port: The keystone_port of this OpenStackCloud.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and keystone_port is None:  # noqa: E501
            raise ValueError("Invalid value for `keystone_port`, must not be `None`")  # noqa: E501

        self._keystone_port = keystone_port

    @property
    def keystone_protocol(self):
        """Gets the keystone_protocol of this OpenStackCloud.  # noqa: E501


        :return: The keystone_protocol of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._keystone_protocol

    @keystone_protocol.setter
    def keystone_protocol(self, keystone_protocol):
        """Sets the keystone_protocol of this OpenStackCloud.


        :param keystone_protocol: The keystone_protocol of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and keystone_protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `keystone_protocol`, must not be `None`")  # noqa: E501

        self._keystone_protocol = keystone_protocol

    @property
    def keystone_username(self):
        """Gets the keystone_username of this OpenStackCloud.  # noqa: E501


        :return: The keystone_username of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._keystone_username

    @keystone_username.setter
    def keystone_username(self, keystone_username):
        """Sets the keystone_username of this OpenStackCloud.


        :param keystone_username: The keystone_username of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and keystone_username is None:  # noqa: E501
            raise ValueError("Invalid value for `keystone_username`, must not be `None`")  # noqa: E501

        self._keystone_username = keystone_username

    @property
    def keystone_version(self):
        """Gets the keystone_version of this OpenStackCloud.  # noqa: E501


        :return: The keystone_version of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._keystone_version

    @keystone_version.setter
    def keystone_version(self, keystone_version):
        """Sets the keystone_version of this OpenStackCloud.


        :param keystone_version: The keystone_version of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and keystone_version is None:  # noqa: E501
            raise ValueError("Invalid value for `keystone_version`, must not be `None`")  # noqa: E501

        self._keystone_version = keystone_version

    @property
    def nat_image_id(self):
        """Gets the nat_image_id of this OpenStackCloud.  # noqa: E501


        :return: The nat_image_id of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._nat_image_id

    @nat_image_id.setter
    def nat_image_id(self, nat_image_id):
        """Sets the nat_image_id of this OpenStackCloud.


        :param nat_image_id: The nat_image_id of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nat_image_id is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_image_id`, must not be `None`")  # noqa: E501

        self._nat_image_id = nat_image_id

    @property
    def nat_instance_type(self):
        """Gets the nat_instance_type of this OpenStackCloud.  # noqa: E501


        :return: The nat_instance_type of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._nat_instance_type

    @nat_instance_type.setter
    def nat_instance_type(self, nat_instance_type):
        """Sets the nat_instance_type of this OpenStackCloud.


        :param nat_instance_type: The nat_instance_type of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nat_instance_type is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_instance_type`, must not be `None`")  # noqa: E501

        self._nat_instance_type = nat_instance_type

    @property
    def tenant(self):
        """Gets the tenant of this OpenStackCloud.  # noqa: E501


        :return: The tenant of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this OpenStackCloud.


        :param tenant: The tenant of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant`, must not be `None`")  # noqa: E501

        self._tenant = tenant

    @property
    def tenant_id(self):
        """Gets the tenant_id of this OpenStackCloud.  # noqa: E501


        :return: The tenant_id of this OpenStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this OpenStackCloud.


        :param tenant_id: The tenant_id of this OpenStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and tenant_id is None:  # noqa: E501
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) > 255):
            raise ValueError("Invalid value for `tenant_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) < 1):
            raise ValueError("Invalid value for `tenant_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._tenant_id = tenant_id

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
        if not isinstance(other, OpenStackCloud):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenStackCloud):
            return True

        return self.to_dict() != other.to_dict()
