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


class PhysicalHost(object):
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
        'components': 'list[AbstractComponent]',
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
        'physical_machine_uuid': 'str',
        'template_profile': 'TemplateProfile',
        'subtype': 'str',
        'physical_machine': 'PhysicalMachine',
        'mac_address': 'str',
        'ip_address': 'str',
        'hostname': 'str'
    }

    attribute_map = {
        'components': 'components',
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
        'physical_machine_uuid': 'physicalMachineUuid',
        'template_profile': 'templateProfile',
        'subtype': 'subtype',
        'physical_machine': 'physicalMachine',
        'mac_address': 'macAddress',
        'ip_address': 'ipAddress',
        'hostname': 'hostname'
    }

    def __init__(self, components=None, id=None, trusted_projects=None, creator=None, dependent_asset_count=None, description=None, metadata=None, name=None, offline=None, owning_project=None, state=None, visibility=None, impact_level=None, categories=None, physical_machine_uuid=None, template_profile=None, subtype=None, physical_machine=None, mac_address=None, ip_address=None, hostname=None, local_vars_configuration=None):  # noqa: E501
        """PhysicalHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._components = None
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
        self._physical_machine_uuid = None
        self._template_profile = None
        self._subtype = None
        self._physical_machine = None
        self._mac_address = None
        self._ip_address = None
        self._hostname = None
        self.discriminator = None

        if components is not None:
            self.components = components
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
        if physical_machine_uuid is not None:
            self.physical_machine_uuid = physical_machine_uuid
        if template_profile is not None:
            self.template_profile = template_profile
        self.subtype = subtype
        if physical_machine is not None:
            self.physical_machine = physical_machine
        if mac_address is not None:
            self.mac_address = mac_address
        if ip_address is not None:
            self.ip_address = ip_address
        if hostname is not None:
            self.hostname = hostname

    @property
    def components(self):
        """Gets the components of this PhysicalHost.  # noqa: E501


        :return: The components of this PhysicalHost.  # noqa: E501
        :rtype: list[AbstractComponent]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this PhysicalHost.


        :param components: The components of this PhysicalHost.  # noqa: E501
        :type: list[AbstractComponent]
        """

        self._components = components

    @property
    def id(self):
        """Gets the id of this PhysicalHost.  # noqa: E501


        :return: The id of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PhysicalHost.


        :param id: The id of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def trusted_projects(self):
        """Gets the trusted_projects of this PhysicalHost.  # noqa: E501


        :return: The trusted_projects of this PhysicalHost.  # noqa: E501
        :rtype: list[Project]
        """
        return self._trusted_projects

    @trusted_projects.setter
    def trusted_projects(self, trusted_projects):
        """Sets the trusted_projects of this PhysicalHost.


        :param trusted_projects: The trusted_projects of this PhysicalHost.  # noqa: E501
        :type: list[Project]
        """

        self._trusted_projects = trusted_projects

    @property
    def creator(self):
        """Gets the creator of this PhysicalHost.  # noqa: E501


        :return: The creator of this PhysicalHost.  # noqa: E501
        :rtype: User
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this PhysicalHost.


        :param creator: The creator of this PhysicalHost.  # noqa: E501
        :type: User
        """

        self._creator = creator

    @property
    def dependent_asset_count(self):
        """Gets the dependent_asset_count of this PhysicalHost.  # noqa: E501


        :return: The dependent_asset_count of this PhysicalHost.  # noqa: E501
        :rtype: int
        """
        return self._dependent_asset_count

    @dependent_asset_count.setter
    def dependent_asset_count(self, dependent_asset_count):
        """Sets the dependent_asset_count of this PhysicalHost.


        :param dependent_asset_count: The dependent_asset_count of this PhysicalHost.  # noqa: E501
        :type: int
        """

        self._dependent_asset_count = dependent_asset_count

    @property
    def description(self):
        """Gets the description of this PhysicalHost.  # noqa: E501


        :return: The description of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PhysicalHost.


        :param description: The description of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this PhysicalHost.  # noqa: E501


        :return: The metadata of this PhysicalHost.  # noqa: E501
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PhysicalHost.


        :param metadata: The metadata of this PhysicalHost.  # noqa: E501
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """Gets the name of this PhysicalHost.  # noqa: E501


        :return: The name of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PhysicalHost.


        :param name: The name of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def offline(self):
        """Gets the offline of this PhysicalHost.  # noqa: E501


        :return: The offline of this PhysicalHost.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this PhysicalHost.


        :param offline: The offline of this PhysicalHost.  # noqa: E501
        :type: bool
        """

        self._offline = offline

    @property
    def owning_project(self):
        """Gets the owning_project of this PhysicalHost.  # noqa: E501


        :return: The owning_project of this PhysicalHost.  # noqa: E501
        :rtype: Project
        """
        return self._owning_project

    @owning_project.setter
    def owning_project(self, owning_project):
        """Sets the owning_project of this PhysicalHost.


        :param owning_project: The owning_project of this PhysicalHost.  # noqa: E501
        :type: Project
        """

        self._owning_project = owning_project

    @property
    def state(self):
        """Gets the state of this PhysicalHost.  # noqa: E501


        :return: The state of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PhysicalHost.


        :param state: The state of this PhysicalHost.  # noqa: E501
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
        """Gets the visibility of this PhysicalHost.  # noqa: E501


        :return: The visibility of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this PhysicalHost.


        :param visibility: The visibility of this PhysicalHost.  # noqa: E501
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
        """Gets the impact_level of this PhysicalHost.  # noqa: E501


        :return: The impact_level of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._impact_level

    @impact_level.setter
    def impact_level(self, impact_level):
        """Sets the impact_level of this PhysicalHost.


        :param impact_level: The impact_level of this PhysicalHost.  # noqa: E501
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
        """Gets the categories of this PhysicalHost.  # noqa: E501


        :return: The categories of this PhysicalHost.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this PhysicalHost.


        :param categories: The categories of this PhysicalHost.  # noqa: E501
        :type: list[Category]
        """

        self._categories = categories

    @property
    def physical_machine_uuid(self):
        """Gets the physical_machine_uuid of this PhysicalHost.  # noqa: E501


        :return: The physical_machine_uuid of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._physical_machine_uuid

    @physical_machine_uuid.setter
    def physical_machine_uuid(self, physical_machine_uuid):
        """Sets the physical_machine_uuid of this PhysicalHost.


        :param physical_machine_uuid: The physical_machine_uuid of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._physical_machine_uuid = physical_machine_uuid

    @property
    def template_profile(self):
        """Gets the template_profile of this PhysicalHost.  # noqa: E501


        :return: The template_profile of this PhysicalHost.  # noqa: E501
        :rtype: TemplateProfile
        """
        return self._template_profile

    @template_profile.setter
    def template_profile(self, template_profile):
        """Sets the template_profile of this PhysicalHost.


        :param template_profile: The template_profile of this PhysicalHost.  # noqa: E501
        :type: TemplateProfile
        """

        self._template_profile = template_profile

    @property
    def subtype(self):
        """Gets the subtype of this PhysicalHost.  # noqa: E501


        :return: The subtype of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this PhysicalHost.


        :param subtype: The subtype of this PhysicalHost.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def physical_machine(self):
        """Gets the physical_machine of this PhysicalHost.  # noqa: E501


        :return: The physical_machine of this PhysicalHost.  # noqa: E501
        :rtype: PhysicalMachine
        """
        return self._physical_machine

    @physical_machine.setter
    def physical_machine(self, physical_machine):
        """Sets the physical_machine of this PhysicalHost.


        :param physical_machine: The physical_machine of this PhysicalHost.  # noqa: E501
        :type: PhysicalMachine
        """

        self._physical_machine = physical_machine

    @property
    def mac_address(self):
        """Gets the mac_address of this PhysicalHost.  # noqa: E501


        :return: The mac_address of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this PhysicalHost.


        :param mac_address: The mac_address of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def ip_address(self):
        """Gets the ip_address of this PhysicalHost.  # noqa: E501


        :return: The ip_address of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PhysicalHost.


        :param ip_address: The ip_address of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def hostname(self):
        """Gets the hostname of this PhysicalHost.  # noqa: E501


        :return: The hostname of this PhysicalHost.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this PhysicalHost.


        :param hostname: The hostname of this PhysicalHost.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

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
        if not isinstance(other, PhysicalHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhysicalHost):
            return True

        return self.to_dict() != other.to_dict()
