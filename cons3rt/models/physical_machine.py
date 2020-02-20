# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class PhysicalMachine(object):
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
        'id': 'str',
        'trusted_projects': 'list[Project]',
        'creator': 'User',
        'dependent_asset_count': 'int',
        'description': 'str',
        'metadata': 'Metadata',
        'name': 'str',
        'offline': 'bool',
        'owning_project': 'Project',
        'state': 'str',
        'visibility': 'str',
        'impact_level': 'str',
        'categories': 'list[Category]',
        'architecture': 'str',
        'bits': 'str',
        'operating_system': 'str',
        'base_disks': 'list[Disk]',
        'remote_access_templates': 'list[RemoteAccessTemplate]',
        'host_name': 'str',
        'ip_address': 'str',
        'mac_address': 'str',
        'cpu_count': 'int',
        'ram': 'int'
    }

    attribute_map = {
        'id': 'id',
        'trusted_projects': 'trustedProjects',
        'creator': 'creator',
        'dependent_asset_count': 'dependentAssetCount',
        'description': 'description',
        'metadata': 'metadata',
        'name': 'name',
        'offline': 'offline',
        'owning_project': 'owningProject',
        'state': 'state',
        'visibility': 'visibility',
        'impact_level': 'impactLevel',
        'categories': 'categories',
        'architecture': 'architecture',
        'bits': 'bits',
        'operating_system': 'operatingSystem',
        'base_disks': 'baseDisks',
        'remote_access_templates': 'remoteAccessTemplates',
        'host_name': 'hostName',
        'ip_address': 'ipAddress',
        'mac_address': 'macAddress',
        'cpu_count': 'cpuCount',
        'ram': 'ram'
    }

    def __init__(self, id=None, trusted_projects=None, creator=None, dependent_asset_count=None, description=None, metadata=None, name=None, offline=None, owning_project=None, state=None, visibility=None, impact_level=None, categories=None, architecture=None, bits=None, operating_system=None, base_disks=None, remote_access_templates=None, host_name=None, ip_address=None, mac_address=None, cpu_count=None, ram=None, local_vars_configuration=None):  # noqa: E501
        """PhysicalMachine - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._trusted_projects = None
        self._creator = None
        self._dependent_asset_count = None
        self._description = None
        self._metadata = None
        self._name = None
        self._offline = None
        self._owning_project = None
        self._state = None
        self._visibility = None
        self._impact_level = None
        self._categories = None
        self._architecture = None
        self._bits = None
        self._operating_system = None
        self._base_disks = None
        self._remote_access_templates = None
        self._host_name = None
        self._ip_address = None
        self._mac_address = None
        self._cpu_count = None
        self._ram = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if trusted_projects is not None:
            self.trusted_projects = trusted_projects
        if creator is not None:
            self.creator = creator
        if dependent_asset_count is not None:
            self.dependent_asset_count = dependent_asset_count
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata
        if name is not None:
            self.name = name
        if offline is not None:
            self.offline = offline
        if owning_project is not None:
            self.owning_project = owning_project
        if state is not None:
            self.state = state
        if visibility is not None:
            self.visibility = visibility
        if impact_level is not None:
            self.impact_level = impact_level
        if categories is not None:
            self.categories = categories
        if architecture is not None:
            self.architecture = architecture
        if bits is not None:
            self.bits = bits
        if operating_system is not None:
            self.operating_system = operating_system
        if base_disks is not None:
            self.base_disks = base_disks
        if remote_access_templates is not None:
            self.remote_access_templates = remote_access_templates
        if host_name is not None:
            self.host_name = host_name
        if ip_address is not None:
            self.ip_address = ip_address
        if mac_address is not None:
            self.mac_address = mac_address
        if cpu_count is not None:
            self.cpu_count = cpu_count
        if ram is not None:
            self.ram = ram

    @property
    def id(self):
        """Gets the id of this PhysicalMachine.  # noqa: E501


        :return: The id of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhysicalMachine.


        :param id: The id of this PhysicalMachine.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def trusted_projects(self):
        """Gets the trusted_projects of this PhysicalMachine.  # noqa: E501


        :return: The trusted_projects of this PhysicalMachine.  # noqa: E501
        :rtype: list[Project]
        """
        return self._trusted_projects

    @trusted_projects.setter
    def trusted_projects(self, trusted_projects):
        """Sets the trusted_projects of this PhysicalMachine.


        :param trusted_projects: The trusted_projects of this PhysicalMachine.  # noqa: E501
        :type: list[Project]
        """

        self._trusted_projects = trusted_projects

    @property
    def creator(self):
        """Gets the creator of this PhysicalMachine.  # noqa: E501


        :return: The creator of this PhysicalMachine.  # noqa: E501
        :rtype: User
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PhysicalMachine.


        :param creator: The creator of this PhysicalMachine.  # noqa: E501
        :type: User
        """

        self._creator = creator

    @property
    def dependent_asset_count(self):
        """Gets the dependent_asset_count of this PhysicalMachine.  # noqa: E501


        :return: The dependent_asset_count of this PhysicalMachine.  # noqa: E501
        :rtype: int
        """
        return self._dependent_asset_count

    @dependent_asset_count.setter
    def dependent_asset_count(self, dependent_asset_count):
        """Sets the dependent_asset_count of this PhysicalMachine.


        :param dependent_asset_count: The dependent_asset_count of this PhysicalMachine.  # noqa: E501
        :type: int
        """

        self._dependent_asset_count = dependent_asset_count

    @property
    def description(self):
        """Gets the description of this PhysicalMachine.  # noqa: E501


        :return: The description of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PhysicalMachine.


        :param description: The description of this PhysicalMachine.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this PhysicalMachine.  # noqa: E501


        :return: The metadata of this PhysicalMachine.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PhysicalMachine.


        :param metadata: The metadata of this PhysicalMachine.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PhysicalMachine.  # noqa: E501


        :return: The name of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhysicalMachine.


        :param name: The name of this PhysicalMachine.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def offline(self):
        """Gets the offline of this PhysicalMachine.  # noqa: E501


        :return: The offline of this PhysicalMachine.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this PhysicalMachine.


        :param offline: The offline of this PhysicalMachine.  # noqa: E501
        :type: bool
        """

        self._offline = offline

    @property
    def owning_project(self):
        """Gets the owning_project of this PhysicalMachine.  # noqa: E501


        :return: The owning_project of this PhysicalMachine.  # noqa: E501
        :rtype: Project
        """
        return self._owning_project

    @owning_project.setter
    def owning_project(self, owning_project):
        """Sets the owning_project of this PhysicalMachine.


        :param owning_project: The owning_project of this PhysicalMachine.  # noqa: E501
        :type: Project
        """

        self._owning_project = owning_project

    @property
    def state(self):
        """Gets the state of this PhysicalMachine.  # noqa: E501


        :return: The state of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PhysicalMachine.


        :param state: The state of this PhysicalMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_DEVELOPMENT", "CERTIFIED", "DEPRECATED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def visibility(self):
        """Gets the visibility of this PhysicalMachine.  # noqa: E501


        :return: The visibility of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this PhysicalMachine.


        :param visibility: The visibility of this PhysicalMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["OWNER", "OWNING_PROJECT", "TRUSTED_PROJECTS", "COMMUNITY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and visibility not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def impact_level(self):
        """Gets the impact_level of this PhysicalMachine.  # noqa: E501


        :return: The impact_level of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._impact_level

    @impact_level.setter
    def impact_level(self, impact_level):
        """Sets the impact_level of this PhysicalMachine.


        :param impact_level: The impact_level of this PhysicalMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "FEDRAMP_LOW", "FEDRAMP_MODERATE_DOD_LEVEL_2", "FEDRAMP_HIGH_DOD_LEVEL_4", "DOD_LEVEL_5", "DOD_LEVEL_6"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and impact_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `impact_level` ({0}), must be one of {1}"  # noqa: E501
                .format(impact_level, allowed_values)
            )

        self._impact_level = impact_level

    @property
    def categories(self):
        """Gets the categories of this PhysicalMachine.  # noqa: E501


        :return: The categories of this PhysicalMachine.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this PhysicalMachine.


        :param categories: The categories of this PhysicalMachine.  # noqa: E501
        :type: list[Category]
        """

        self._categories = categories

    @property
    def architecture(self):
        """Gets the architecture of this PhysicalMachine.  # noqa: E501


        :return: The architecture of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this PhysicalMachine.


        :param architecture: The architecture of this PhysicalMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["X86", "X64", "ARM", "SPARC", "PPCLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and architecture not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `architecture` ({0}), must be one of {1}"  # noqa: E501
                .format(architecture, allowed_values)
            )

        self._architecture = architecture

    @property
    def bits(self):
        """Gets the bits of this PhysicalMachine.  # noqa: E501


        :return: The bits of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._bits

    @bits.setter
    def bits(self, bits):
        """Sets the bits of this PhysicalMachine.


        :param bits: The bits of this PhysicalMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["BITS32", "BITS64"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and bits not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `bits` ({0}), must be one of {1}"  # noqa: E501
                .format(bits, allowed_values)
            )

        self._bits = bits

    @property
    def operating_system(self):
        """Gets the operating_system of this PhysicalMachine.  # noqa: E501


        :return: The operating_system of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this PhysicalMachine.


        :param operating_system: The operating_system of this PhysicalMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["AMAZON_LINUX_LATEST_X64", "CENTOS_6_X64", "CENTOS_6_X86", "CENTOS_7_X64", "CORE_OS_1221_X64", "F5_BIGIP_X64", "FORTISIEM", "PALO_ALTO_NETWORKS_PAN_OS_X64", "FEDORA_23_X64", "GENERIC_LINUX_X64", "GENERIC_WINDOWS_X64", "KALI_ROLLING_X64", "ORACLE_LINUX_6_X64", "ORACLE_LINUX_7_X64", "OS_X_10", "OS_X_11", "RASPBIAN", "RHEL_5_X64", "RHEL_5_X86", "RHEL_6_X64", "RHEL_6_X86", "RHEL_7_ATOMIC_HOST", "RHEL_7_PPCLE", "RHEL_7_X64", "SOLARIS_11_X64", "UBUNTU_12_X64", "UBUNTU_14_X64", "UBUNTU_16_X64", "UBUNTU_18_X64", "UBUNTU_CORE", "VYOS_117_X64", "VYOS_118_X64", "WINDOWS_10_X64", "WINDOWS_7_X64", "WINDOWS_7_X86", "WINDOWS_8_X64", "WINDOWS_SERVER_2008_R2_X64", "WINDOWS_SERVER_2008_X64", "WINDOWS_SERVER_2012_R2_X64", "WINDOWS_SERVER_2012_X64", "WINDOWS_SERVER_2016_X64", "WINDOWS_SERVER_2019_X64", "WINDOWS_XP_X86"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operating_system not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

    @property
    def base_disks(self):
        """Gets the base_disks of this PhysicalMachine.  # noqa: E501


        :return: The base_disks of this PhysicalMachine.  # noqa: E501
        :rtype: list[Disk]
        """
        return self._base_disks

    @base_disks.setter
    def base_disks(self, base_disks):
        """Sets the base_disks of this PhysicalMachine.


        :param base_disks: The base_disks of this PhysicalMachine.  # noqa: E501
        :type: list[Disk]
        """

        self._base_disks = base_disks

    @property
    def remote_access_templates(self):
        """Gets the remote_access_templates of this PhysicalMachine.  # noqa: E501


        :return: The remote_access_templates of this PhysicalMachine.  # noqa: E501
        :rtype: list[RemoteAccessTemplate]
        """
        return self._remote_access_templates

    @remote_access_templates.setter
    def remote_access_templates(self, remote_access_templates):
        """Sets the remote_access_templates of this PhysicalMachine.


        :param remote_access_templates: The remote_access_templates of this PhysicalMachine.  # noqa: E501
        :type: list[RemoteAccessTemplate]
        """

        self._remote_access_templates = remote_access_templates

    @property
    def host_name(self):
        """Gets the host_name of this PhysicalMachine.  # noqa: E501


        :return: The host_name of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """Sets the host_name of this PhysicalMachine.


        :param host_name: The host_name of this PhysicalMachine.  # noqa: E501
        :type: str
        """

        self._host_name = host_name

    @property
    def ip_address(self):
        """Gets the ip_address of this PhysicalMachine.  # noqa: E501


        :return: The ip_address of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PhysicalMachine.


        :param ip_address: The ip_address of this PhysicalMachine.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def mac_address(self):
        """Gets the mac_address of this PhysicalMachine.  # noqa: E501


        :return: The mac_address of this PhysicalMachine.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this PhysicalMachine.


        :param mac_address: The mac_address of this PhysicalMachine.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def cpu_count(self):
        """Gets the cpu_count of this PhysicalMachine.  # noqa: E501


        :return: The cpu_count of this PhysicalMachine.  # noqa: E501
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """Sets the cpu_count of this PhysicalMachine.


        :param cpu_count: The cpu_count of this PhysicalMachine.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                cpu_count is not None and cpu_count < 1):  # noqa: E501
            raise ValueError("Invalid value for `cpu_count`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cpu_count = cpu_count

    @property
    def ram(self):
        """Gets the ram of this PhysicalMachine.  # noqa: E501


        :return: The ram of this PhysicalMachine.  # noqa: E501
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this PhysicalMachine.


        :param ram: The ram of this PhysicalMachine.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                ram is not None and ram < 1):  # noqa: E501
            raise ValueError("Invalid value for `ram`, must be a value greater than or equal to `1`")  # noqa: E501

        self._ram = ram

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
        if not isinstance(other, PhysicalMachine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhysicalMachine):
            return True

        return self.to_dict() != other.to_dict()
