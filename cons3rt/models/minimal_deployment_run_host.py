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


class MinimalDeploymentRunHost(object):
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
        'build_order': 'int',
        'created_password': 'str',
        'created_username': 'str',
        'default_password': 'str',
        'default_username': 'str',
        'disks': 'list[Disk]',
        'fap_status': 'str',
        'has_gpu': 'bool',
        'host_action_in_process': 'bool',
        'hostname': 'str',
        'id': 'int',
        'installations': 'list[AbstractInstallation]',
        'instance_type_name': 'str',
        'nested_virtualization': 'bool',
        'network_interfaces': 'list[NetworkInterface]',
        'num_cpus': 'int',
        'physical_machine_data_or_template_uuid': 'str',
        'physical_machine_or_template_name': 'str',
        'published': 'bool',
        'ram': 'int',
        'snapshot_available': 'bool',
        'snapshot_date': 'int',
        'system_module_id': 'int',
        'system_module_type': 'str',
        'system_role': 'str',
        'virtualization_realm_status': 'str',
        'virtual': 'bool',
        'provisionable': 'bool'
    }

    attribute_map = {
        'build_order': 'buildOrder',
        'created_password': 'createdPassword',
        'created_username': 'createdUsername',
        'default_password': 'defaultPassword',
        'default_username': 'defaultUsername',
        'disks': 'disks',
        'fap_status': 'fapStatus',
        'has_gpu': 'hasGpu',
        'host_action_in_process': 'hostActionInProcess',
        'hostname': 'hostname',
        'id': 'id',
        'installations': 'installations',
        'instance_type_name': 'instanceTypeName',
        'nested_virtualization': 'nestedVirtualization',
        'network_interfaces': 'networkInterfaces',
        'num_cpus': 'numCpus',
        'physical_machine_data_or_template_uuid': 'physicalMachineDataOrTemplateUuid',
        'physical_machine_or_template_name': 'physicalMachineOrTemplateName',
        'published': 'published',
        'ram': 'ram',
        'snapshot_available': 'snapshotAvailable',
        'snapshot_date': 'snapshotDate',
        'system_module_id': 'systemModuleId',
        'system_module_type': 'systemModuleType',
        'system_role': 'systemRole',
        'virtualization_realm_status': 'VirtualizationRealmStatus',
        'virtual': 'virtual',
        'provisionable': 'provisionable'
    }

    def __init__(self, build_order=None, created_password=None, created_username=None, default_password=None, default_username=None, disks=None, fap_status=None, has_gpu=None, host_action_in_process=None, hostname=None, id=None, installations=None, instance_type_name=None, nested_virtualization=None, network_interfaces=None, num_cpus=None, physical_machine_data_or_template_uuid=None, physical_machine_or_template_name=None, published=None, ram=None, snapshot_available=None, snapshot_date=None, system_module_id=None, system_module_type=None, system_role=None, virtualization_realm_status=None, virtual=None, provisionable=None, local_vars_configuration=None):  # noqa: E501
        """MinimalDeploymentRunHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._build_order = None
        self._created_password = None
        self._created_username = None
        self._default_password = None
        self._default_username = None
        self._disks = None
        self._fap_status = None
        self._has_gpu = None
        self._host_action_in_process = None
        self._hostname = None
        self._id = None
        self._installations = None
        self._instance_type_name = None
        self._nested_virtualization = None
        self._network_interfaces = None
        self._num_cpus = None
        self._physical_machine_data_or_template_uuid = None
        self._physical_machine_or_template_name = None
        self._published = None
        self._ram = None
        self._snapshot_available = None
        self._snapshot_date = None
        self._system_module_id = None
        self._system_module_type = None
        self._system_role = None
        self._virtualization_realm_status = None
        self._virtual = None
        self._provisionable = None
        self.discriminator = None

        if build_order is not None:
            self.build_order = build_order
        if created_password is not None:
            self.created_password = created_password
        if created_username is not None:
            self.created_username = created_username
        if default_password is not None:
            self.default_password = default_password
        if default_username is not None:
            self.default_username = default_username
        if disks is not None:
            self.disks = disks
        if fap_status is not None:
            self.fap_status = fap_status
        if has_gpu is not None:
            self.has_gpu = has_gpu
        if host_action_in_process is not None:
            self.host_action_in_process = host_action_in_process
        if hostname is not None:
            self.hostname = hostname
        if id is not None:
            self.id = id
        if installations is not None:
            self.installations = installations
        if instance_type_name is not None:
            self.instance_type_name = instance_type_name
        if nested_virtualization is not None:
            self.nested_virtualization = nested_virtualization
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        if num_cpus is not None:
            self.num_cpus = num_cpus
        if physical_machine_data_or_template_uuid is not None:
            self.physical_machine_data_or_template_uuid = physical_machine_data_or_template_uuid
        if physical_machine_or_template_name is not None:
            self.physical_machine_or_template_name = physical_machine_or_template_name
        if published is not None:
            self.published = published
        if ram is not None:
            self.ram = ram
        if snapshot_available is not None:
            self.snapshot_available = snapshot_available
        if snapshot_date is not None:
            self.snapshot_date = snapshot_date
        if system_module_id is not None:
            self.system_module_id = system_module_id
        if system_module_type is not None:
            self.system_module_type = system_module_type
        if system_role is not None:
            self.system_role = system_role
        if virtualization_realm_status is not None:
            self.virtualization_realm_status = virtualization_realm_status
        if virtual is not None:
            self.virtual = virtual
        if provisionable is not None:
            self.provisionable = provisionable

    @property
    def build_order(self):
        """Gets the build_order of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The build_order of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: int
        """
        return self._build_order

    @build_order.setter
    def build_order(self, build_order):
        """Sets the build_order of this MinimalDeploymentRunHost.


        :param build_order: The build_order of this MinimalDeploymentRunHost.  # noqa: E501
        :type: int
        """

        self._build_order = build_order

    @property
    def created_password(self):
        """Gets the created_password of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The created_password of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._created_password

    @created_password.setter
    def created_password(self, created_password):
        """Sets the created_password of this MinimalDeploymentRunHost.


        :param created_password: The created_password of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._created_password = created_password

    @property
    def created_username(self):
        """Gets the created_username of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The created_username of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._created_username

    @created_username.setter
    def created_username(self, created_username):
        """Sets the created_username of this MinimalDeploymentRunHost.


        :param created_username: The created_username of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._created_username = created_username

    @property
    def default_password(self):
        """Gets the default_password of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The default_password of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._default_password

    @default_password.setter
    def default_password(self, default_password):
        """Sets the default_password of this MinimalDeploymentRunHost.


        :param default_password: The default_password of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._default_password = default_password

    @property
    def default_username(self):
        """Gets the default_username of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The default_username of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._default_username

    @default_username.setter
    def default_username(self, default_username):
        """Sets the default_username of this MinimalDeploymentRunHost.


        :param default_username: The default_username of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._default_username = default_username

    @property
    def disks(self):
        """Gets the disks of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The disks of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: list[Disk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this MinimalDeploymentRunHost.


        :param disks: The disks of this MinimalDeploymentRunHost.  # noqa: E501
        :type: list[Disk]
        """

        self._disks = disks

    @property
    def fap_status(self):
        """Gets the fap_status of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The fap_status of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._fap_status

    @fap_status.setter
    def fap_status(self, fap_status):
        """Sets the fap_status of this MinimalDeploymentRunHost.


        :param fap_status: The fap_status of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUESTED", "BUILDING_HOSTSET", "BUILDING_HOSTSET_ERROR", "HOSTSET_BUILT_POWERED_OFF", "POWERING_ON", "POWERING_ON_ERROR", "POWERED_ON", "AWAITING_AGENT_CHECK_IN", "AGENT_CHECK_IN_ERROR", "AGENT_CHECK_IN_SUCCESS", "BUILDING_SOURCE", "SOURCE_BUILT", "BUILDING_SOURCE_ERROR", "BUILDING_SYSTEMS", "BUILDING_SYSTEMS_ERROR", "SYSTEMS_BUILT", "BUILDING_SCENARIO", "BUILDING_SCENARIO_ERROR", "SCENARIO_BUILT", "REBOOTING", "REBOOTING_ERROR", "RESERVED", "RELEASE_REQUESTED", "RELEASING", "RELEASING_SCENARIO_ERROR", "COMPLETE", "UNKNOWN", "CANCELED", "INVALID_STATE_ERROR", "FAP_SERVICE_COMMUNICATIONS_ERROR", "INVALID_REQUEST_ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fap_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fap_status` ({0}), must be one of {1}"  # noqa: E501
                .format(fap_status, allowed_values)
            )

        self._fap_status = fap_status

    @property
    def has_gpu(self):
        """Gets the has_gpu of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The has_gpu of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: bool
        """
        return self._has_gpu

    @has_gpu.setter
    def has_gpu(self, has_gpu):
        """Sets the has_gpu of this MinimalDeploymentRunHost.


        :param has_gpu: The has_gpu of this MinimalDeploymentRunHost.  # noqa: E501
        :type: bool
        """

        self._has_gpu = has_gpu

    @property
    def host_action_in_process(self):
        """Gets the host_action_in_process of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The host_action_in_process of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: bool
        """
        return self._host_action_in_process

    @host_action_in_process.setter
    def host_action_in_process(self, host_action_in_process):
        """Sets the host_action_in_process of this MinimalDeploymentRunHost.


        :param host_action_in_process: The host_action_in_process of this MinimalDeploymentRunHost.  # noqa: E501
        :type: bool
        """

        self._host_action_in_process = host_action_in_process

    @property
    def hostname(self):
        """Gets the hostname of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The hostname of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this MinimalDeploymentRunHost.


        :param hostname: The hostname of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def id(self):
        """Gets the id of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The id of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalDeploymentRunHost.


        :param id: The id of this MinimalDeploymentRunHost.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def installations(self):
        """Gets the installations of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The installations of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: list[AbstractInstallation]
        """
        return self._installations

    @installations.setter
    def installations(self, installations):
        """Sets the installations of this MinimalDeploymentRunHost.


        :param installations: The installations of this MinimalDeploymentRunHost.  # noqa: E501
        :type: list[AbstractInstallation]
        """

        self._installations = installations

    @property
    def instance_type_name(self):
        """Gets the instance_type_name of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The instance_type_name of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._instance_type_name

    @instance_type_name.setter
    def instance_type_name(self, instance_type_name):
        """Sets the instance_type_name of this MinimalDeploymentRunHost.


        :param instance_type_name: The instance_type_name of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._instance_type_name = instance_type_name

    @property
    def nested_virtualization(self):
        """Gets the nested_virtualization of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The nested_virtualization of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: bool
        """
        return self._nested_virtualization

    @nested_virtualization.setter
    def nested_virtualization(self, nested_virtualization):
        """Sets the nested_virtualization of this MinimalDeploymentRunHost.


        :param nested_virtualization: The nested_virtualization of this MinimalDeploymentRunHost.  # noqa: E501
        :type: bool
        """

        self._nested_virtualization = nested_virtualization

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The network_interfaces of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: list[NetworkInterface]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this MinimalDeploymentRunHost.


        :param network_interfaces: The network_interfaces of this MinimalDeploymentRunHost.  # noqa: E501
        :type: list[NetworkInterface]
        """

        self._network_interfaces = network_interfaces

    @property
    def num_cpus(self):
        """Gets the num_cpus of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The num_cpus of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: int
        """
        return self._num_cpus

    @num_cpus.setter
    def num_cpus(self, num_cpus):
        """Sets the num_cpus of this MinimalDeploymentRunHost.


        :param num_cpus: The num_cpus of this MinimalDeploymentRunHost.  # noqa: E501
        :type: int
        """

        self._num_cpus = num_cpus

    @property
    def physical_machine_data_or_template_uuid(self):
        """Gets the physical_machine_data_or_template_uuid of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The physical_machine_data_or_template_uuid of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._physical_machine_data_or_template_uuid

    @physical_machine_data_or_template_uuid.setter
    def physical_machine_data_or_template_uuid(self, physical_machine_data_or_template_uuid):
        """Sets the physical_machine_data_or_template_uuid of this MinimalDeploymentRunHost.


        :param physical_machine_data_or_template_uuid: The physical_machine_data_or_template_uuid of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._physical_machine_data_or_template_uuid = physical_machine_data_or_template_uuid

    @property
    def physical_machine_or_template_name(self):
        """Gets the physical_machine_or_template_name of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The physical_machine_or_template_name of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._physical_machine_or_template_name

    @physical_machine_or_template_name.setter
    def physical_machine_or_template_name(self, physical_machine_or_template_name):
        """Sets the physical_machine_or_template_name of this MinimalDeploymentRunHost.


        :param physical_machine_or_template_name: The physical_machine_or_template_name of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._physical_machine_or_template_name = physical_machine_or_template_name

    @property
    def published(self):
        """Gets the published of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The published of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this MinimalDeploymentRunHost.


        :param published: The published of this MinimalDeploymentRunHost.  # noqa: E501
        :type: bool
        """

        self._published = published

    @property
    def ram(self):
        """Gets the ram of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The ram of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this MinimalDeploymentRunHost.


        :param ram: The ram of this MinimalDeploymentRunHost.  # noqa: E501
        :type: int
        """

        self._ram = ram

    @property
    def snapshot_available(self):
        """Gets the snapshot_available of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The snapshot_available of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: bool
        """
        return self._snapshot_available

    @snapshot_available.setter
    def snapshot_available(self, snapshot_available):
        """Sets the snapshot_available of this MinimalDeploymentRunHost.


        :param snapshot_available: The snapshot_available of this MinimalDeploymentRunHost.  # noqa: E501
        :type: bool
        """

        self._snapshot_available = snapshot_available

    @property
    def snapshot_date(self):
        """Gets the snapshot_date of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The snapshot_date of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: int
        """
        return self._snapshot_date

    @snapshot_date.setter
    def snapshot_date(self, snapshot_date):
        """Sets the snapshot_date of this MinimalDeploymentRunHost.


        :param snapshot_date: The snapshot_date of this MinimalDeploymentRunHost.  # noqa: E501
        :type: int
        """

        self._snapshot_date = snapshot_date

    @property
    def system_module_id(self):
        """Gets the system_module_id of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The system_module_id of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: int
        """
        return self._system_module_id

    @system_module_id.setter
    def system_module_id(self, system_module_id):
        """Sets the system_module_id of this MinimalDeploymentRunHost.


        :param system_module_id: The system_module_id of this MinimalDeploymentRunHost.  # noqa: E501
        :type: int
        """

        self._system_module_id = system_module_id

    @property
    def system_module_type(self):
        """Gets the system_module_type of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The system_module_type of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._system_module_type

    @system_module_type.setter
    def system_module_type(self, system_module_type):
        """Sets the system_module_type of this MinimalDeploymentRunHost.


        :param system_module_type: The system_module_type of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """
        allowed_values = ["Appliance", "ContainerApplication", "ContainerAsset", "Deployment", "Device", "PhysicalHost", "Scenario", "SoftwareAsset", "SoftwareAssetBundle", "TestAsset", "TestBundle", "VirtualHost"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and system_module_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `system_module_type` ({0}), must be one of {1}"  # noqa: E501
                .format(system_module_type, allowed_values)
            )

        self._system_module_type = system_module_type

    @property
    def system_role(self):
        """Gets the system_role of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The system_role of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this MinimalDeploymentRunHost.


        :param system_role: The system_role of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """

        self._system_role = system_role

    @property
    def virtualization_realm_status(self):
        """Gets the virtualization_realm_status of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The virtualization_realm_status of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: str
        """
        return self._virtualization_realm_status

    @virtualization_realm_status.setter
    def virtualization_realm_status(self, virtualization_realm_status):
        """Sets the virtualization_realm_status of this MinimalDeploymentRunHost.


        :param virtualization_realm_status: The virtualization_realm_status of this MinimalDeploymentRunHost.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "STOPPED", "RUNNING", "SUSPENDED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and virtualization_realm_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `virtualization_realm_status` ({0}), must be one of {1}"  # noqa: E501
                .format(virtualization_realm_status, allowed_values)
            )

        self._virtualization_realm_status = virtualization_realm_status

    @property
    def virtual(self):
        """Gets the virtual of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The virtual of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: bool
        """
        return self._virtual

    @virtual.setter
    def virtual(self, virtual):
        """Sets the virtual of this MinimalDeploymentRunHost.


        :param virtual: The virtual of this MinimalDeploymentRunHost.  # noqa: E501
        :type: bool
        """

        self._virtual = virtual

    @property
    def provisionable(self):
        """Gets the provisionable of this MinimalDeploymentRunHost.  # noqa: E501


        :return: The provisionable of this MinimalDeploymentRunHost.  # noqa: E501
        :rtype: bool
        """
        return self._provisionable

    @provisionable.setter
    def provisionable(self, provisionable):
        """Sets the provisionable of this MinimalDeploymentRunHost.


        :param provisionable: The provisionable of this MinimalDeploymentRunHost.  # noqa: E501
        :type: bool
        """

        self._provisionable = provisionable

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
        if not isinstance(other, MinimalDeploymentRunHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalDeploymentRunHost):
            return True

        return self.to_dict() != other.to_dict()
