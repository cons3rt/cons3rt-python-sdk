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


class VirtualizationRealm(object):
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
        'virtualization_realm_type': 'str',
        'access_point': 'str',
        'account_id': 'str',
        'active_virtual_machines': 'int',
        'networks': 'list[Network]',
        'admin_users': 'list[User]',
        'allocated': 'bool',
        'cidr': 'str',
        'cloud': 'Cloud',
        'created_at': 'int',
        'date_last_reachable': 'int',
        'default_windows_domain_name': 'str',
        'description': 'str',
        'id': 'int',
        'local_storage_name': 'str',
        'maximum_num_cpus': 'int',
        'maximum_num_gpus': 'int',
        'maximum_ram_in_megabytes': 'int',
        'maximum_storage_in_megabytes': 'int',
        'maximum_virtual_machines': 'int',
        'name': 'str',
        'password': 'str',
        'power_on_delay_base': 'int',
        'power_on_initial_delay_base': 'int',
        'power_on_minimum_delay': 'int',
        'projects': 'list[Project]',
        'reachable': 'bool',
        'remote_access_config': 'RemoteAccessConfig',
        'remote_access_deployment_id': 'int',
        'remote_access_deployment_run_status': 'str',
        'remote_access_status': 'str',
        'state': 'str',
        'supported_features': 'list[str]',
        'template_registrations': 'list[TemplateRegistration]',
        'templates': 'list[Cons3rtTemplateData]',
        'template_subscriptions': 'list[TemplateSubscription]',
        'updated_at': 'int',
        'username': 'str',
        'zone_count': 'int'
    }

    attribute_map = {
        'virtualization_realm_type': 'virtualizationRealmType',
        'access_point': 'accessPoint',
        'account_id': 'accountId',
        'active_virtual_machines': 'activeVirtualMachines',
        'networks': 'networks',
        'admin_users': 'adminUsers',
        'allocated': 'allocated',
        'cidr': 'cidr',
        'cloud': 'cloud',
        'created_at': 'createdAt',
        'date_last_reachable': 'dateLastReachable',
        'default_windows_domain_name': 'defaultWindowsDomainName',
        'description': 'description',
        'id': 'id',
        'local_storage_name': 'localStorageName',
        'maximum_num_cpus': 'maximumNumCpus',
        'maximum_num_gpus': 'maximumNumGpus',
        'maximum_ram_in_megabytes': 'maximumRamInMegabytes',
        'maximum_storage_in_megabytes': 'maximumStorageInMegabytes',
        'maximum_virtual_machines': 'maximumVirtualMachines',
        'name': 'name',
        'password': 'password',
        'power_on_delay_base': 'powerOnDelayBase',
        'power_on_initial_delay_base': 'powerOnInitialDelayBase',
        'power_on_minimum_delay': 'powerOnMinimumDelay',
        'projects': 'projects',
        'reachable': 'reachable',
        'remote_access_config': 'remoteAccessConfig',
        'remote_access_deployment_id': 'remoteAccessDeploymentId',
        'remote_access_deployment_run_status': 'remoteAccessDeploymentRunStatus',
        'remote_access_status': 'remoteAccessStatus',
        'state': 'state',
        'supported_features': 'supportedFeatures',
        'template_registrations': 'templateRegistrations',
        'templates': 'templates',
        'template_subscriptions': 'templateSubscriptions',
        'updated_at': 'updatedAt',
        'username': 'username',
        'zone_count': 'zoneCount'
    }

    discriminator_value_class_map = {
        'AwsVirtualizationRealm': 'AwsVirtualizationRealm',
        'VCloudVirtualizationRealm': 'VCloudVirtualizationRealm',
        'OpenStackVirtualizationRealm': 'OpenStackVirtualizationRealm',
        'AzureVirtualizationRealm': 'AzureVirtualizationRealm'
    }

    def __init__(self, virtualization_realm_type=None, access_point=None, account_id=None, active_virtual_machines=None, networks=None, admin_users=None, allocated=None, cidr=None, cloud=None, created_at=None, date_last_reachable=None, default_windows_domain_name=None, description=None, id=None, local_storage_name=None, maximum_num_cpus=None, maximum_num_gpus=None, maximum_ram_in_megabytes=None, maximum_storage_in_megabytes=None, maximum_virtual_machines=None, name=None, password=None, power_on_delay_base=None, power_on_initial_delay_base=None, power_on_minimum_delay=None, projects=None, reachable=None, remote_access_config=None, remote_access_deployment_id=None, remote_access_deployment_run_status=None, remote_access_status=None, state=None, supported_features=None, template_registrations=None, templates=None, template_subscriptions=None, updated_at=None, username=None, zone_count=None, local_vars_configuration=None):  # noqa: E501
        """VirtualizationRealm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._virtualization_realm_type = None
        self._access_point = None
        self._account_id = None
        self._active_virtual_machines = None
        self._networks = None
        self._admin_users = None
        self._allocated = None
        self._cidr = None
        self._cloud = None
        self._created_at = None
        self._date_last_reachable = None
        self._default_windows_domain_name = None
        self._description = None
        self._id = None
        self._local_storage_name = None
        self._maximum_num_cpus = None
        self._maximum_num_gpus = None
        self._maximum_ram_in_megabytes = None
        self._maximum_storage_in_megabytes = None
        self._maximum_virtual_machines = None
        self._name = None
        self._password = None
        self._power_on_delay_base = None
        self._power_on_initial_delay_base = None
        self._power_on_minimum_delay = None
        self._projects = None
        self._reachable = None
        self._remote_access_config = None
        self._remote_access_deployment_id = None
        self._remote_access_deployment_run_status = None
        self._remote_access_status = None
        self._state = None
        self._supported_features = None
        self._template_registrations = None
        self._templates = None
        self._template_subscriptions = None
        self._updated_at = None
        self._username = None
        self._zone_count = None
        self.discriminator = 'virtualization_realm_type'

        if virtualization_realm_type is not None:
            self.virtualization_realm_type = virtualization_realm_type
        if access_point is not None:
            self.access_point = access_point
        self.account_id = account_id
        if active_virtual_machines is not None:
            self.active_virtual_machines = active_virtual_machines
        if networks is not None:
            self.networks = networks
        if admin_users is not None:
            self.admin_users = admin_users
        if allocated is not None:
            self.allocated = allocated
        self.cidr = cidr
        if cloud is not None:
            self.cloud = cloud
        if created_at is not None:
            self.created_at = created_at
        if date_last_reachable is not None:
            self.date_last_reachable = date_last_reachable
        if default_windows_domain_name is not None:
            self.default_windows_domain_name = default_windows_domain_name
        self.description = description
        if id is not None:
            self.id = id
        if local_storage_name is not None:
            self.local_storage_name = local_storage_name
        if maximum_num_cpus is not None:
            self.maximum_num_cpus = maximum_num_cpus
        if maximum_num_gpus is not None:
            self.maximum_num_gpus = maximum_num_gpus
        if maximum_ram_in_megabytes is not None:
            self.maximum_ram_in_megabytes = maximum_ram_in_megabytes
        if maximum_storage_in_megabytes is not None:
            self.maximum_storage_in_megabytes = maximum_storage_in_megabytes
        if maximum_virtual_machines is not None:
            self.maximum_virtual_machines = maximum_virtual_machines
        self.name = name
        self.password = password
        if power_on_delay_base is not None:
            self.power_on_delay_base = power_on_delay_base
        if power_on_initial_delay_base is not None:
            self.power_on_initial_delay_base = power_on_initial_delay_base
        if power_on_minimum_delay is not None:
            self.power_on_minimum_delay = power_on_minimum_delay
        if projects is not None:
            self.projects = projects
        if reachable is not None:
            self.reachable = reachable
        if remote_access_config is not None:
            self.remote_access_config = remote_access_config
        if remote_access_deployment_id is not None:
            self.remote_access_deployment_id = remote_access_deployment_id
        if remote_access_deployment_run_status is not None:
            self.remote_access_deployment_run_status = remote_access_deployment_run_status
        if remote_access_status is not None:
            self.remote_access_status = remote_access_status
        if state is not None:
            self.state = state
        if supported_features is not None:
            self.supported_features = supported_features
        if template_registrations is not None:
            self.template_registrations = template_registrations
        if templates is not None:
            self.templates = templates
        if template_subscriptions is not None:
            self.template_subscriptions = template_subscriptions
        if updated_at is not None:
            self.updated_at = updated_at
        self.username = username
        if zone_count is not None:
            self.zone_count = zone_count

    @property
    def virtualization_realm_type(self):
        """Gets the virtualization_realm_type of this VirtualizationRealm.  # noqa: E501


        :return: The virtualization_realm_type of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._virtualization_realm_type

    @virtualization_realm_type.setter
    def virtualization_realm_type(self, virtualization_realm_type):
        """Sets the virtualization_realm_type of this VirtualizationRealm.


        :param virtualization_realm_type: The virtualization_realm_type of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        allowed_values = ["Amazon", "Azure", "CloudStack", "Mock", "OpenStack", "VCloud"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and virtualization_realm_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `virtualization_realm_type` ({0}), must be one of {1}"  # noqa: E501
                .format(virtualization_realm_type, allowed_values)
            )

        self._virtualization_realm_type = virtualization_realm_type

    @property
    def access_point(self):
        """Gets the access_point of this VirtualizationRealm.  # noqa: E501


        :return: The access_point of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        """Sets the access_point of this VirtualizationRealm.


        :param access_point: The access_point of this VirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._access_point = access_point

    @property
    def account_id(self):
        """Gets the account_id of this VirtualizationRealm.  # noqa: E501


        :return: The account_id of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this VirtualizationRealm.


        :param account_id: The account_id of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def active_virtual_machines(self):
        """Gets the active_virtual_machines of this VirtualizationRealm.  # noqa: E501


        :return: The active_virtual_machines of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._active_virtual_machines

    @active_virtual_machines.setter
    def active_virtual_machines(self, active_virtual_machines):
        """Sets the active_virtual_machines of this VirtualizationRealm.


        :param active_virtual_machines: The active_virtual_machines of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._active_virtual_machines = active_virtual_machines

    @property
    def networks(self):
        """Gets the networks of this VirtualizationRealm.  # noqa: E501


        :return: The networks of this VirtualizationRealm.  # noqa: E501
        :rtype: list[Network]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this VirtualizationRealm.


        :param networks: The networks of this VirtualizationRealm.  # noqa: E501
        :type: list[Network]
        """

        self._networks = networks

    @property
    def admin_users(self):
        """Gets the admin_users of this VirtualizationRealm.  # noqa: E501


        :return: The admin_users of this VirtualizationRealm.  # noqa: E501
        :rtype: list[User]
        """
        return self._admin_users

    @admin_users.setter
    def admin_users(self, admin_users):
        """Sets the admin_users of this VirtualizationRealm.


        :param admin_users: The admin_users of this VirtualizationRealm.  # noqa: E501
        :type: list[User]
        """

        self._admin_users = admin_users

    @property
    def allocated(self):
        """Gets the allocated of this VirtualizationRealm.  # noqa: E501


        :return: The allocated of this VirtualizationRealm.  # noqa: E501
        :rtype: bool
        """
        return self._allocated

    @allocated.setter
    def allocated(self, allocated):
        """Sets the allocated of this VirtualizationRealm.


        :param allocated: The allocated of this VirtualizationRealm.  # noqa: E501
        :type: bool
        """

        self._allocated = allocated

    @property
    def cidr(self):
        """Gets the cidr of this VirtualizationRealm.  # noqa: E501


        :return: The cidr of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this VirtualizationRealm.


        :param cidr: The cidr of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cidr is None:  # noqa: E501
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cidr is not None and len(cidr) > 16):
            raise ValueError("Invalid value for `cidr`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cidr is not None and len(cidr) < 10):
            raise ValueError("Invalid value for `cidr`, length must be greater than or equal to `10`")  # noqa: E501

        self._cidr = cidr

    @property
    def cloud(self):
        """Gets the cloud of this VirtualizationRealm.  # noqa: E501


        :return: The cloud of this VirtualizationRealm.  # noqa: E501
        :rtype: Cloud
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this VirtualizationRealm.


        :param cloud: The cloud of this VirtualizationRealm.  # noqa: E501
        :type: Cloud
        """

        self._cloud = cloud

    @property
    def created_at(self):
        """Gets the created_at of this VirtualizationRealm.  # noqa: E501


        :return: The created_at of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this VirtualizationRealm.


        :param created_at: The created_at of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def date_last_reachable(self):
        """Gets the date_last_reachable of this VirtualizationRealm.  # noqa: E501


        :return: The date_last_reachable of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._date_last_reachable

    @date_last_reachable.setter
    def date_last_reachable(self, date_last_reachable):
        """Sets the date_last_reachable of this VirtualizationRealm.


        :param date_last_reachable: The date_last_reachable of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._date_last_reachable = date_last_reachable

    @property
    def default_windows_domain_name(self):
        """Gets the default_windows_domain_name of this VirtualizationRealm.  # noqa: E501


        :return: The default_windows_domain_name of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._default_windows_domain_name

    @default_windows_domain_name.setter
    def default_windows_domain_name(self, default_windows_domain_name):
        """Sets the default_windows_domain_name of this VirtualizationRealm.


        :param default_windows_domain_name: The default_windows_domain_name of this VirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._default_windows_domain_name = default_windows_domain_name

    @property
    def description(self):
        """Gets the description of this VirtualizationRealm.  # noqa: E501


        :return: The description of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualizationRealm.


        :param description: The description of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this VirtualizationRealm.  # noqa: E501


        :return: The id of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualizationRealm.


        :param id: The id of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def local_storage_name(self):
        """Gets the local_storage_name of this VirtualizationRealm.  # noqa: E501


        :return: The local_storage_name of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._local_storage_name

    @local_storage_name.setter
    def local_storage_name(self, local_storage_name):
        """Sets the local_storage_name of this VirtualizationRealm.


        :param local_storage_name: The local_storage_name of this VirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._local_storage_name = local_storage_name

    @property
    def maximum_num_cpus(self):
        """Gets the maximum_num_cpus of this VirtualizationRealm.  # noqa: E501


        :return: The maximum_num_cpus of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_num_cpus

    @maximum_num_cpus.setter
    def maximum_num_cpus(self, maximum_num_cpus):
        """Sets the maximum_num_cpus of this VirtualizationRealm.


        :param maximum_num_cpus: The maximum_num_cpus of this VirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_num_cpus is not None and maximum_num_cpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_num_cpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_num_cpus = maximum_num_cpus

    @property
    def maximum_num_gpus(self):
        """Gets the maximum_num_gpus of this VirtualizationRealm.  # noqa: E501


        :return: The maximum_num_gpus of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_num_gpus

    @maximum_num_gpus.setter
    def maximum_num_gpus(self, maximum_num_gpus):
        """Sets the maximum_num_gpus of this VirtualizationRealm.


        :param maximum_num_gpus: The maximum_num_gpus of this VirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_num_gpus is not None and maximum_num_gpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_num_gpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_num_gpus = maximum_num_gpus

    @property
    def maximum_ram_in_megabytes(self):
        """Gets the maximum_ram_in_megabytes of this VirtualizationRealm.  # noqa: E501


        :return: The maximum_ram_in_megabytes of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_ram_in_megabytes

    @maximum_ram_in_megabytes.setter
    def maximum_ram_in_megabytes(self, maximum_ram_in_megabytes):
        """Sets the maximum_ram_in_megabytes of this VirtualizationRealm.


        :param maximum_ram_in_megabytes: The maximum_ram_in_megabytes of this VirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_ram_in_megabytes is not None and maximum_ram_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_ram_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_ram_in_megabytes = maximum_ram_in_megabytes

    @property
    def maximum_storage_in_megabytes(self):
        """Gets the maximum_storage_in_megabytes of this VirtualizationRealm.  # noqa: E501


        :return: The maximum_storage_in_megabytes of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_storage_in_megabytes

    @maximum_storage_in_megabytes.setter
    def maximum_storage_in_megabytes(self, maximum_storage_in_megabytes):
        """Sets the maximum_storage_in_megabytes of this VirtualizationRealm.


        :param maximum_storage_in_megabytes: The maximum_storage_in_megabytes of this VirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_storage_in_megabytes is not None and maximum_storage_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_storage_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_storage_in_megabytes = maximum_storage_in_megabytes

    @property
    def maximum_virtual_machines(self):
        """Gets the maximum_virtual_machines of this VirtualizationRealm.  # noqa: E501


        :return: The maximum_virtual_machines of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_virtual_machines

    @maximum_virtual_machines.setter
    def maximum_virtual_machines(self, maximum_virtual_machines):
        """Sets the maximum_virtual_machines of this VirtualizationRealm.


        :param maximum_virtual_machines: The maximum_virtual_machines of this VirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_virtual_machines is not None and maximum_virtual_machines < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_virtual_machines`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_virtual_machines = maximum_virtual_machines

    @property
    def name(self):
        """Gets the name of this VirtualizationRealm.  # noqa: E501


        :return: The name of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualizationRealm.


        :param name: The name of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this VirtualizationRealm.  # noqa: E501


        :return: The password of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this VirtualizationRealm.


        :param password: The password of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def power_on_delay_base(self):
        """Gets the power_on_delay_base of this VirtualizationRealm.  # noqa: E501


        :return: The power_on_delay_base of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._power_on_delay_base

    @power_on_delay_base.setter
    def power_on_delay_base(self, power_on_delay_base):
        """Sets the power_on_delay_base of this VirtualizationRealm.


        :param power_on_delay_base: The power_on_delay_base of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._power_on_delay_base = power_on_delay_base

    @property
    def power_on_initial_delay_base(self):
        """Gets the power_on_initial_delay_base of this VirtualizationRealm.  # noqa: E501


        :return: The power_on_initial_delay_base of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._power_on_initial_delay_base

    @power_on_initial_delay_base.setter
    def power_on_initial_delay_base(self, power_on_initial_delay_base):
        """Sets the power_on_initial_delay_base of this VirtualizationRealm.


        :param power_on_initial_delay_base: The power_on_initial_delay_base of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._power_on_initial_delay_base = power_on_initial_delay_base

    @property
    def power_on_minimum_delay(self):
        """Gets the power_on_minimum_delay of this VirtualizationRealm.  # noqa: E501


        :return: The power_on_minimum_delay of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._power_on_minimum_delay

    @power_on_minimum_delay.setter
    def power_on_minimum_delay(self, power_on_minimum_delay):
        """Sets the power_on_minimum_delay of this VirtualizationRealm.


        :param power_on_minimum_delay: The power_on_minimum_delay of this VirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                power_on_minimum_delay is not None and power_on_minimum_delay < 0):  # noqa: E501
            raise ValueError("Invalid value for `power_on_minimum_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._power_on_minimum_delay = power_on_minimum_delay

    @property
    def projects(self):
        """Gets the projects of this VirtualizationRealm.  # noqa: E501


        :return: The projects of this VirtualizationRealm.  # noqa: E501
        :rtype: list[Project]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this VirtualizationRealm.


        :param projects: The projects of this VirtualizationRealm.  # noqa: E501
        :type: list[Project]
        """

        self._projects = projects

    @property
    def reachable(self):
        """Gets the reachable of this VirtualizationRealm.  # noqa: E501


        :return: The reachable of this VirtualizationRealm.  # noqa: E501
        :rtype: bool
        """
        return self._reachable

    @reachable.setter
    def reachable(self, reachable):
        """Sets the reachable of this VirtualizationRealm.


        :param reachable: The reachable of this VirtualizationRealm.  # noqa: E501
        :type: bool
        """

        self._reachable = reachable

    @property
    def remote_access_config(self):
        """Gets the remote_access_config of this VirtualizationRealm.  # noqa: E501


        :return: The remote_access_config of this VirtualizationRealm.  # noqa: E501
        :rtype: RemoteAccessConfig
        """
        return self._remote_access_config

    @remote_access_config.setter
    def remote_access_config(self, remote_access_config):
        """Sets the remote_access_config of this VirtualizationRealm.


        :param remote_access_config: The remote_access_config of this VirtualizationRealm.  # noqa: E501
        :type: RemoteAccessConfig
        """

        self._remote_access_config = remote_access_config

    @property
    def remote_access_deployment_id(self):
        """Gets the remote_access_deployment_id of this VirtualizationRealm.  # noqa: E501


        :return: The remote_access_deployment_id of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._remote_access_deployment_id

    @remote_access_deployment_id.setter
    def remote_access_deployment_id(self, remote_access_deployment_id):
        """Sets the remote_access_deployment_id of this VirtualizationRealm.


        :param remote_access_deployment_id: The remote_access_deployment_id of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._remote_access_deployment_id = remote_access_deployment_id

    @property
    def remote_access_deployment_run_status(self):
        """Gets the remote_access_deployment_run_status of this VirtualizationRealm.  # noqa: E501


        :return: The remote_access_deployment_run_status of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._remote_access_deployment_run_status

    @remote_access_deployment_run_status.setter
    def remote_access_deployment_run_status(self, remote_access_deployment_run_status):
        """Sets the remote_access_deployment_run_status of this VirtualizationRealm.


        :param remote_access_deployment_run_status: The remote_access_deployment_run_status of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "SCHEDULED", "SUBMITTED", "PROVISIONING_HOSTS", "HOSTS_PROVISIONED", "RESERVED", "RELEASE_REQUESTED", "RELEASING", "TESTING", "TESTED", "COMPLETED", "CANCELED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and remote_access_deployment_run_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `remote_access_deployment_run_status` ({0}), must be one of {1}"  # noqa: E501
                .format(remote_access_deployment_run_status, allowed_values)
            )

        self._remote_access_deployment_run_status = remote_access_deployment_run_status

    @property
    def remote_access_status(self):
        """Gets the remote_access_status of this VirtualizationRealm.  # noqa: E501


        :return: The remote_access_status of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._remote_access_status

    @remote_access_status.setter
    def remote_access_status(self, remote_access_status):
        """Sets the remote_access_status of this VirtualizationRealm.


        :param remote_access_status: The remote_access_status of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENABLING", "ENABLED", "DISABLING", "DISABLED", "ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and remote_access_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `remote_access_status` ({0}), must be one of {1}"  # noqa: E501
                .format(remote_access_status, allowed_values)
            )

        self._remote_access_status = remote_access_status

    @property
    def state(self):
        """Gets the state of this VirtualizationRealm.  # noqa: E501


        :return: The state of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this VirtualizationRealm.


        :param state: The state of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "ENTERING_MAINTENANCE", "INACTIVE", "MAINTENANCE", "PENDING", "REQUESTED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def supported_features(self):
        """Gets the supported_features of this VirtualizationRealm.  # noqa: E501


        :return: The supported_features of this VirtualizationRealm.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this VirtualizationRealm.


        :param supported_features: The supported_features of this VirtualizationRealm.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["USER_PASSWORD_UPDATE", "VIRT_MACHINE_NESTED_VIRTUALIZATION", "VIRT_MACHINE_SNAPSHOT", "VIRT_MACHINE_SUSPEND", "VIRT_REALM_ADD_NETWORK", "VIRT_REALM_ALLOCATION", "VIRT_REALM_APPLY_SECURITY", "VIRT_REALM_DEALLOCATION", "VIRT_REALM_DELETE_NETWORK", "VIRT_REALM_INSTANCE_TYPE_DRIVEN", "VIRT_REALM_REDEPLOY_BOUNDARY_PROTECTION", "VIRT_REALM_REFRESH_BOUNDARY_PROTECTION"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(supported_features).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `supported_features` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(supported_features) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._supported_features = supported_features

    @property
    def template_registrations(self):
        """Gets the template_registrations of this VirtualizationRealm.  # noqa: E501


        :return: The template_registrations of this VirtualizationRealm.  # noqa: E501
        :rtype: list[TemplateRegistration]
        """
        return self._template_registrations

    @template_registrations.setter
    def template_registrations(self, template_registrations):
        """Sets the template_registrations of this VirtualizationRealm.


        :param template_registrations: The template_registrations of this VirtualizationRealm.  # noqa: E501
        :type: list[TemplateRegistration]
        """

        self._template_registrations = template_registrations

    @property
    def templates(self):
        """Gets the templates of this VirtualizationRealm.  # noqa: E501


        :return: The templates of this VirtualizationRealm.  # noqa: E501
        :rtype: list[Cons3rtTemplateData]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this VirtualizationRealm.


        :param templates: The templates of this VirtualizationRealm.  # noqa: E501
        :type: list[Cons3rtTemplateData]
        """

        self._templates = templates

    @property
    def template_subscriptions(self):
        """Gets the template_subscriptions of this VirtualizationRealm.  # noqa: E501


        :return: The template_subscriptions of this VirtualizationRealm.  # noqa: E501
        :rtype: list[TemplateSubscription]
        """
        return self._template_subscriptions

    @template_subscriptions.setter
    def template_subscriptions(self, template_subscriptions):
        """Sets the template_subscriptions of this VirtualizationRealm.


        :param template_subscriptions: The template_subscriptions of this VirtualizationRealm.  # noqa: E501
        :type: list[TemplateSubscription]
        """

        self._template_subscriptions = template_subscriptions

    @property
    def updated_at(self):
        """Gets the updated_at of this VirtualizationRealm.  # noqa: E501


        :return: The updated_at of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this VirtualizationRealm.


        :param updated_at: The updated_at of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def username(self):
        """Gets the username of this VirtualizationRealm.  # noqa: E501


        :return: The username of this VirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this VirtualizationRealm.


        :param username: The username of this VirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def zone_count(self):
        """Gets the zone_count of this VirtualizationRealm.  # noqa: E501


        :return: The zone_count of this VirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._zone_count

    @zone_count.setter
    def zone_count(self, zone_count):
        """Sets the zone_count of this VirtualizationRealm.


        :param zone_count: The zone_count of this VirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._zone_count = zone_count

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, VirtualizationRealm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualizationRealm):
            return True

        return self.to_dict() != other.to_dict()
