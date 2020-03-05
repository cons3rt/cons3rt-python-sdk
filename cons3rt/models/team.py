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


class Team(object):
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
        'asset_bundle_installer_enabled': 'bool',
        'availability_zone_enabled': 'bool',
        'lead_user': 'User',
        'icon': 'str',
        'id': 'int',
        'managed_virtualization_realms': 'list[VirtualizationRealm]',
        'team_managers': 'list[User]',
        'max_assets': 'int',
        'max_managed_virtualization_realms': 'int',
        'max_num_cpus': 'int',
        'max_num_gpus': 'int',
        'max_projects': 'int',
        'max_ram_in_megabytes': 'int',
        'max_shared_remote_access_sessions': 'int',
        'max_storage_in_megabytes': 'int',
        'max_users': 'int',
        'max_virtual_machines': 'int',
        'name': 'str',
        'order_number': 'str',
        'owned_clouds': 'list[Cloud]',
        'power_schedule_enabled': 'bool',
        'owned_projects': 'list[Project]',
        'contact_info': 'PocInfo',
        'private': 'bool',
        'rdp_client_proxy_enabled': 'bool',
        'rdp_client_session_duration': 'int',
        'state': 'str',
        'snapshot_enabled': 'bool',
        'valid_until': 'int'
    }

    attribute_map = {
        'asset_bundle_installer_enabled': 'assetBundleInstallerEnabled',
        'availability_zone_enabled': 'availabilityZoneEnabled',
        'lead_user': 'leadUser',
        'icon': 'icon',
        'id': 'id',
        'managed_virtualization_realms': 'managedVirtualizationRealms',
        'team_managers': 'teamManagers',
        'max_assets': 'maxAssets',
        'max_managed_virtualization_realms': 'maxManagedVirtualizationRealms',
        'max_num_cpus': 'maxNumCpus',
        'max_num_gpus': 'maxNumGpus',
        'max_projects': 'maxProjects',
        'max_ram_in_megabytes': 'maxRamInMegabytes',
        'max_shared_remote_access_sessions': 'maxSharedRemoteAccessSessions',
        'max_storage_in_megabytes': 'maxStorageInMegabytes',
        'max_users': 'maxUsers',
        'max_virtual_machines': 'maxVirtualMachines',
        'name': 'name',
        'order_number': 'orderNumber',
        'owned_clouds': 'ownedClouds',
        'power_schedule_enabled': 'powerScheduleEnabled',
        'owned_projects': 'ownedProjects',
        'contact_info': 'contactInfo',
        'private': 'private',
        'rdp_client_proxy_enabled': 'rdpClientProxyEnabled',
        'rdp_client_session_duration': 'rdpClientSessionDuration',
        'state': 'state',
        'snapshot_enabled': 'snapshotEnabled',
        'valid_until': 'validUntil'
    }

    def __init__(self, asset_bundle_installer_enabled=None, availability_zone_enabled=None, lead_user=None, icon=None, id=None, managed_virtualization_realms=None, team_managers=None, max_assets=None, max_managed_virtualization_realms=None, max_num_cpus=None, max_num_gpus=None, max_projects=None, max_ram_in_megabytes=None, max_shared_remote_access_sessions=None, max_storage_in_megabytes=None, max_users=None, max_virtual_machines=None, name=None, order_number=None, owned_clouds=None, power_schedule_enabled=None, owned_projects=None, contact_info=None, private=None, rdp_client_proxy_enabled=None, rdp_client_session_duration=None, state=None, snapshot_enabled=None, valid_until=None, local_vars_configuration=None):  # noqa: E501
        """Team - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_bundle_installer_enabled = None
        self._availability_zone_enabled = None
        self._lead_user = None
        self._icon = None
        self._id = None
        self._managed_virtualization_realms = None
        self._team_managers = None
        self._max_assets = None
        self._max_managed_virtualization_realms = None
        self._max_num_cpus = None
        self._max_num_gpus = None
        self._max_projects = None
        self._max_ram_in_megabytes = None
        self._max_shared_remote_access_sessions = None
        self._max_storage_in_megabytes = None
        self._max_users = None
        self._max_virtual_machines = None
        self._name = None
        self._order_number = None
        self._owned_clouds = None
        self._power_schedule_enabled = None
        self._owned_projects = None
        self._contact_info = None
        self._private = None
        self._rdp_client_proxy_enabled = None
        self._rdp_client_session_duration = None
        self._state = None
        self._snapshot_enabled = None
        self._valid_until = None
        self.discriminator = None

        if asset_bundle_installer_enabled is not None:
            self.asset_bundle_installer_enabled = asset_bundle_installer_enabled
        if availability_zone_enabled is not None:
            self.availability_zone_enabled = availability_zone_enabled
        self.lead_user = lead_user
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if managed_virtualization_realms is not None:
            self.managed_virtualization_realms = managed_virtualization_realms
        if team_managers is not None:
            self.team_managers = team_managers
        if max_assets is not None:
            self.max_assets = max_assets
        if max_managed_virtualization_realms is not None:
            self.max_managed_virtualization_realms = max_managed_virtualization_realms
        if max_num_cpus is not None:
            self.max_num_cpus = max_num_cpus
        if max_num_gpus is not None:
            self.max_num_gpus = max_num_gpus
        if max_projects is not None:
            self.max_projects = max_projects
        if max_ram_in_megabytes is not None:
            self.max_ram_in_megabytes = max_ram_in_megabytes
        if max_shared_remote_access_sessions is not None:
            self.max_shared_remote_access_sessions = max_shared_remote_access_sessions
        if max_storage_in_megabytes is not None:
            self.max_storage_in_megabytes = max_storage_in_megabytes
        if max_users is not None:
            self.max_users = max_users
        if max_virtual_machines is not None:
            self.max_virtual_machines = max_virtual_machines
        self.name = name
        if order_number is not None:
            self.order_number = order_number
        if owned_clouds is not None:
            self.owned_clouds = owned_clouds
        if power_schedule_enabled is not None:
            self.power_schedule_enabled = power_schedule_enabled
        if owned_projects is not None:
            self.owned_projects = owned_projects
        self.contact_info = contact_info
        if private is not None:
            self.private = private
        if rdp_client_proxy_enabled is not None:
            self.rdp_client_proxy_enabled = rdp_client_proxy_enabled
        if rdp_client_session_duration is not None:
            self.rdp_client_session_duration = rdp_client_session_duration
        self.state = state
        if snapshot_enabled is not None:
            self.snapshot_enabled = snapshot_enabled
        self.valid_until = valid_until

    @property
    def asset_bundle_installer_enabled(self):
        """Gets the asset_bundle_installer_enabled of this Team.  # noqa: E501


        :return: The asset_bundle_installer_enabled of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._asset_bundle_installer_enabled

    @asset_bundle_installer_enabled.setter
    def asset_bundle_installer_enabled(self, asset_bundle_installer_enabled):
        """Sets the asset_bundle_installer_enabled of this Team.


        :param asset_bundle_installer_enabled: The asset_bundle_installer_enabled of this Team.  # noqa: E501
        :type: bool
        """

        self._asset_bundle_installer_enabled = asset_bundle_installer_enabled

    @property
    def availability_zone_enabled(self):
        """Gets the availability_zone_enabled of this Team.  # noqa: E501


        :return: The availability_zone_enabled of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._availability_zone_enabled

    @availability_zone_enabled.setter
    def availability_zone_enabled(self, availability_zone_enabled):
        """Sets the availability_zone_enabled of this Team.


        :param availability_zone_enabled: The availability_zone_enabled of this Team.  # noqa: E501
        :type: bool
        """

        self._availability_zone_enabled = availability_zone_enabled

    @property
    def lead_user(self):
        """Gets the lead_user of this Team.  # noqa: E501


        :return: The lead_user of this Team.  # noqa: E501
        :rtype: User
        """
        return self._lead_user

    @lead_user.setter
    def lead_user(self, lead_user):
        """Sets the lead_user of this Team.


        :param lead_user: The lead_user of this Team.  # noqa: E501
        :type: User
        """
        if self.local_vars_configuration.client_side_validation and lead_user is None:  # noqa: E501
            raise ValueError("Invalid value for `lead_user`, must not be `None`")  # noqa: E501

        self._lead_user = lead_user

    @property
    def icon(self):
        """Gets the icon of this Team.  # noqa: E501


        :return: The icon of this Team.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Team.


        :param icon: The icon of this Team.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this Team.  # noqa: E501


        :return: The id of this Team.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Team.


        :param id: The id of this Team.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def managed_virtualization_realms(self):
        """Gets the managed_virtualization_realms of this Team.  # noqa: E501


        :return: The managed_virtualization_realms of this Team.  # noqa: E501
        :rtype: list[VirtualizationRealm]
        """
        return self._managed_virtualization_realms

    @managed_virtualization_realms.setter
    def managed_virtualization_realms(self, managed_virtualization_realms):
        """Sets the managed_virtualization_realms of this Team.


        :param managed_virtualization_realms: The managed_virtualization_realms of this Team.  # noqa: E501
        :type: list[VirtualizationRealm]
        """

        self._managed_virtualization_realms = managed_virtualization_realms

    @property
    def team_managers(self):
        """Gets the team_managers of this Team.  # noqa: E501


        :return: The team_managers of this Team.  # noqa: E501
        :rtype: list[User]
        """
        return self._team_managers

    @team_managers.setter
    def team_managers(self, team_managers):
        """Sets the team_managers of this Team.


        :param team_managers: The team_managers of this Team.  # noqa: E501
        :type: list[User]
        """

        self._team_managers = team_managers

    @property
    def max_assets(self):
        """Gets the max_assets of this Team.  # noqa: E501


        :return: The max_assets of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_assets

    @max_assets.setter
    def max_assets(self, max_assets):
        """Sets the max_assets of this Team.


        :param max_assets: The max_assets of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_assets is not None and max_assets < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_assets`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_assets = max_assets

    @property
    def max_managed_virtualization_realms(self):
        """Gets the max_managed_virtualization_realms of this Team.  # noqa: E501


        :return: The max_managed_virtualization_realms of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_managed_virtualization_realms

    @max_managed_virtualization_realms.setter
    def max_managed_virtualization_realms(self, max_managed_virtualization_realms):
        """Sets the max_managed_virtualization_realms of this Team.


        :param max_managed_virtualization_realms: The max_managed_virtualization_realms of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_managed_virtualization_realms is not None and max_managed_virtualization_realms < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_managed_virtualization_realms`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_managed_virtualization_realms = max_managed_virtualization_realms

    @property
    def max_num_cpus(self):
        """Gets the max_num_cpus of this Team.  # noqa: E501


        :return: The max_num_cpus of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_num_cpus

    @max_num_cpus.setter
    def max_num_cpus(self, max_num_cpus):
        """Sets the max_num_cpus of this Team.


        :param max_num_cpus: The max_num_cpus of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_num_cpus is not None and max_num_cpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_num_cpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_num_cpus = max_num_cpus

    @property
    def max_num_gpus(self):
        """Gets the max_num_gpus of this Team.  # noqa: E501


        :return: The max_num_gpus of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_num_gpus

    @max_num_gpus.setter
    def max_num_gpus(self, max_num_gpus):
        """Sets the max_num_gpus of this Team.


        :param max_num_gpus: The max_num_gpus of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_num_gpus is not None and max_num_gpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_num_gpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_num_gpus = max_num_gpus

    @property
    def max_projects(self):
        """Gets the max_projects of this Team.  # noqa: E501


        :return: The max_projects of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_projects

    @max_projects.setter
    def max_projects(self, max_projects):
        """Sets the max_projects of this Team.


        :param max_projects: The max_projects of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_projects is not None and max_projects < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_projects`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_projects = max_projects

    @property
    def max_ram_in_megabytes(self):
        """Gets the max_ram_in_megabytes of this Team.  # noqa: E501


        :return: The max_ram_in_megabytes of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_ram_in_megabytes

    @max_ram_in_megabytes.setter
    def max_ram_in_megabytes(self, max_ram_in_megabytes):
        """Sets the max_ram_in_megabytes of this Team.


        :param max_ram_in_megabytes: The max_ram_in_megabytes of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_ram_in_megabytes is not None and max_ram_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_ram_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_ram_in_megabytes = max_ram_in_megabytes

    @property
    def max_shared_remote_access_sessions(self):
        """Gets the max_shared_remote_access_sessions of this Team.  # noqa: E501


        :return: The max_shared_remote_access_sessions of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_shared_remote_access_sessions

    @max_shared_remote_access_sessions.setter
    def max_shared_remote_access_sessions(self, max_shared_remote_access_sessions):
        """Sets the max_shared_remote_access_sessions of this Team.


        :param max_shared_remote_access_sessions: The max_shared_remote_access_sessions of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_shared_remote_access_sessions is not None and max_shared_remote_access_sessions < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_shared_remote_access_sessions`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_shared_remote_access_sessions = max_shared_remote_access_sessions

    @property
    def max_storage_in_megabytes(self):
        """Gets the max_storage_in_megabytes of this Team.  # noqa: E501


        :return: The max_storage_in_megabytes of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_storage_in_megabytes

    @max_storage_in_megabytes.setter
    def max_storage_in_megabytes(self, max_storage_in_megabytes):
        """Sets the max_storage_in_megabytes of this Team.


        :param max_storage_in_megabytes: The max_storage_in_megabytes of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_storage_in_megabytes is not None and max_storage_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_storage_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_storage_in_megabytes = max_storage_in_megabytes

    @property
    def max_users(self):
        """Gets the max_users of this Team.  # noqa: E501


        :return: The max_users of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """Sets the max_users of this Team.


        :param max_users: The max_users of this Team.  # noqa: E501
        :type: int
        """

        self._max_users = max_users

    @property
    def max_virtual_machines(self):
        """Gets the max_virtual_machines of this Team.  # noqa: E501


        :return: The max_virtual_machines of this Team.  # noqa: E501
        :rtype: int
        """
        return self._max_virtual_machines

    @max_virtual_machines.setter
    def max_virtual_machines(self, max_virtual_machines):
        """Sets the max_virtual_machines of this Team.


        :param max_virtual_machines: The max_virtual_machines of this Team.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_virtual_machines is not None and max_virtual_machines < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_virtual_machines`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_virtual_machines = max_virtual_machines

    @property
    def name(self):
        """Gets the name of this Team.  # noqa: E501


        :return: The name of this Team.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Team.


        :param name: The name of this Team.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def order_number(self):
        """Gets the order_number of this Team.  # noqa: E501


        :return: The order_number of this Team.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this Team.


        :param order_number: The order_number of this Team.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def owned_clouds(self):
        """Gets the owned_clouds of this Team.  # noqa: E501


        :return: The owned_clouds of this Team.  # noqa: E501
        :rtype: list[Cloud]
        """
        return self._owned_clouds

    @owned_clouds.setter
    def owned_clouds(self, owned_clouds):
        """Sets the owned_clouds of this Team.


        :param owned_clouds: The owned_clouds of this Team.  # noqa: E501
        :type: list[Cloud]
        """

        self._owned_clouds = owned_clouds

    @property
    def power_schedule_enabled(self):
        """Gets the power_schedule_enabled of this Team.  # noqa: E501


        :return: The power_schedule_enabled of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._power_schedule_enabled

    @power_schedule_enabled.setter
    def power_schedule_enabled(self, power_schedule_enabled):
        """Sets the power_schedule_enabled of this Team.


        :param power_schedule_enabled: The power_schedule_enabled of this Team.  # noqa: E501
        :type: bool
        """

        self._power_schedule_enabled = power_schedule_enabled

    @property
    def owned_projects(self):
        """Gets the owned_projects of this Team.  # noqa: E501


        :return: The owned_projects of this Team.  # noqa: E501
        :rtype: list[Project]
        """
        return self._owned_projects

    @owned_projects.setter
    def owned_projects(self, owned_projects):
        """Sets the owned_projects of this Team.


        :param owned_projects: The owned_projects of this Team.  # noqa: E501
        :type: list[Project]
        """

        self._owned_projects = owned_projects

    @property
    def contact_info(self):
        """Gets the contact_info of this Team.  # noqa: E501


        :return: The contact_info of this Team.  # noqa: E501
        :rtype: PocInfo
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Sets the contact_info of this Team.


        :param contact_info: The contact_info of this Team.  # noqa: E501
        :type: PocInfo
        """
        if self.local_vars_configuration.client_side_validation and contact_info is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_info`, must not be `None`")  # noqa: E501

        self._contact_info = contact_info

    @property
    def private(self):
        """Gets the private of this Team.  # noqa: E501


        :return: The private of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this Team.


        :param private: The private of this Team.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def rdp_client_proxy_enabled(self):
        """Gets the rdp_client_proxy_enabled of this Team.  # noqa: E501


        :return: The rdp_client_proxy_enabled of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._rdp_client_proxy_enabled

    @rdp_client_proxy_enabled.setter
    def rdp_client_proxy_enabled(self, rdp_client_proxy_enabled):
        """Sets the rdp_client_proxy_enabled of this Team.


        :param rdp_client_proxy_enabled: The rdp_client_proxy_enabled of this Team.  # noqa: E501
        :type: bool
        """

        self._rdp_client_proxy_enabled = rdp_client_proxy_enabled

    @property
    def rdp_client_session_duration(self):
        """Gets the rdp_client_session_duration of this Team.  # noqa: E501


        :return: The rdp_client_session_duration of this Team.  # noqa: E501
        :rtype: int
        """
        return self._rdp_client_session_duration

    @rdp_client_session_duration.setter
    def rdp_client_session_duration(self, rdp_client_session_duration):
        """Sets the rdp_client_session_duration of this Team.


        :param rdp_client_session_duration: The rdp_client_session_duration of this Team.  # noqa: E501
        :type: int
        """

        self._rdp_client_session_duration = rdp_client_session_duration

    @property
    def state(self):
        """Gets the state of this Team.  # noqa: E501


        :return: The state of this Team.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Team.


        :param state: The state of this Team.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and state is None:  # noqa: E501
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["ACTIVE", "INACTIVE", "REQUESTED", "RETIRED", "UNFUNDED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def snapshot_enabled(self):
        """Gets the snapshot_enabled of this Team.  # noqa: E501


        :return: The snapshot_enabled of this Team.  # noqa: E501
        :rtype: bool
        """
        return self._snapshot_enabled

    @snapshot_enabled.setter
    def snapshot_enabled(self, snapshot_enabled):
        """Sets the snapshot_enabled of this Team.


        :param snapshot_enabled: The snapshot_enabled of this Team.  # noqa: E501
        :type: bool
        """

        self._snapshot_enabled = snapshot_enabled

    @property
    def valid_until(self):
        """Gets the valid_until of this Team.  # noqa: E501


        :return: The valid_until of this Team.  # noqa: E501
        :rtype: int
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this Team.


        :param valid_until: The valid_until of this Team.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and valid_until is None:  # noqa: E501
            raise ValueError("Invalid value for `valid_until`, must not be `None`")  # noqa: E501

        self._valid_until = valid_until

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
        if not isinstance(other, Team):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Team):
            return True

        return self.to_dict() != other.to_dict()
