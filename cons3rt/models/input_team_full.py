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


class InputTeamFull(object):
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
        'lead_user': 'InputUser',
        'icon': 'str',
        'id': 'int',
        'team_managers': 'list[InputUser]',
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
        'contact_info': 'PocInfo',
        'power_schedule_enabled': 'bool',
        'private': 'bool',
        'rdp_client_proxy_enabled': 'bool',
        'rdp_client_session_duration': 'int',
        'snapshot_enabled': 'bool',
        'state': 'str',
        'valid_until': 'int'
    }

    attribute_map = {
        'asset_bundle_installer_enabled': 'assetBundleInstallerEnabled',
        'availability_zone_enabled': 'availabilityZoneEnabled',
        'lead_user': 'leadUser',
        'icon': 'icon',
        'id': 'id',
        'team_managers': 'teamManagers',
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
        'contact_info': 'contactInfo',
        'power_schedule_enabled': 'powerScheduleEnabled',
        'private': 'private',
        'rdp_client_proxy_enabled': 'rdpClientProxyEnabled',
        'rdp_client_session_duration': 'rdpClientSessionDuration',
        'snapshot_enabled': 'snapshotEnabled',
        'state': 'state',
        'valid_until': 'validUntil'
    }

    def __init__(self, asset_bundle_installer_enabled=None, availability_zone_enabled=None, lead_user=None, icon=None, id=None, team_managers=None, max_managed_virtualization_realms=None, max_num_cpus=None, max_num_gpus=None, max_projects=None, max_ram_in_megabytes=None, max_shared_remote_access_sessions=None, max_storage_in_megabytes=None, max_users=None, max_virtual_machines=None, name=None, order_number=None, contact_info=None, power_schedule_enabled=None, private=None, rdp_client_proxy_enabled=None, rdp_client_session_duration=None, snapshot_enabled=None, state=None, valid_until=None, local_vars_configuration=None):  # noqa: E501
        """InputTeamFull - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_bundle_installer_enabled = None
        self._availability_zone_enabled = None
        self._lead_user = None
        self._icon = None
        self._id = None
        self._team_managers = None
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
        self._contact_info = None
        self._power_schedule_enabled = None
        self._private = None
        self._rdp_client_proxy_enabled = None
        self._rdp_client_session_duration = None
        self._snapshot_enabled = None
        self._state = None
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
        self.team_managers = team_managers
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
        self.contact_info = contact_info
        if power_schedule_enabled is not None:
            self.power_schedule_enabled = power_schedule_enabled
        if private is not None:
            self.private = private
        if rdp_client_proxy_enabled is not None:
            self.rdp_client_proxy_enabled = rdp_client_proxy_enabled
        if rdp_client_session_duration is not None:
            self.rdp_client_session_duration = rdp_client_session_duration
        if snapshot_enabled is not None:
            self.snapshot_enabled = snapshot_enabled
        self.state = state
        self.valid_until = valid_until

    @property
    def asset_bundle_installer_enabled(self):
        """Gets the asset_bundle_installer_enabled of this InputTeamFull.  # noqa: E501


        :return: The asset_bundle_installer_enabled of this InputTeamFull.  # noqa: E501
        :rtype: bool
        """
        return self._asset_bundle_installer_enabled

    @asset_bundle_installer_enabled.setter
    def asset_bundle_installer_enabled(self, asset_bundle_installer_enabled):
        """Sets the asset_bundle_installer_enabled of this InputTeamFull.


        :param asset_bundle_installer_enabled: The asset_bundle_installer_enabled of this InputTeamFull.  # noqa: E501
        :type: bool
        """

        self._asset_bundle_installer_enabled = asset_bundle_installer_enabled

    @property
    def availability_zone_enabled(self):
        """Gets the availability_zone_enabled of this InputTeamFull.  # noqa: E501


        :return: The availability_zone_enabled of this InputTeamFull.  # noqa: E501
        :rtype: bool
        """
        return self._availability_zone_enabled

    @availability_zone_enabled.setter
    def availability_zone_enabled(self, availability_zone_enabled):
        """Sets the availability_zone_enabled of this InputTeamFull.


        :param availability_zone_enabled: The availability_zone_enabled of this InputTeamFull.  # noqa: E501
        :type: bool
        """

        self._availability_zone_enabled = availability_zone_enabled

    @property
    def lead_user(self):
        """Gets the lead_user of this InputTeamFull.  # noqa: E501


        :return: The lead_user of this InputTeamFull.  # noqa: E501
        :rtype: InputUser
        """
        return self._lead_user

    @lead_user.setter
    def lead_user(self, lead_user):
        """Sets the lead_user of this InputTeamFull.


        :param lead_user: The lead_user of this InputTeamFull.  # noqa: E501
        :type: InputUser
        """
        if self.local_vars_configuration.client_side_validation and lead_user is None:  # noqa: E501
            raise ValueError("Invalid value for `lead_user`, must not be `None`")  # noqa: E501

        self._lead_user = lead_user

    @property
    def icon(self):
        """Gets the icon of this InputTeamFull.  # noqa: E501


        :return: The icon of this InputTeamFull.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this InputTeamFull.


        :param icon: The icon of this InputTeamFull.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this InputTeamFull.  # noqa: E501


        :return: The id of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InputTeamFull.


        :param id: The id of this InputTeamFull.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def team_managers(self):
        """Gets the team_managers of this InputTeamFull.  # noqa: E501


        :return: The team_managers of this InputTeamFull.  # noqa: E501
        :rtype: list[InputUser]
        """
        return self._team_managers

    @team_managers.setter
    def team_managers(self, team_managers):
        """Sets the team_managers of this InputTeamFull.


        :param team_managers: The team_managers of this InputTeamFull.  # noqa: E501
        :type: list[InputUser]
        """
        if self.local_vars_configuration.client_side_validation and team_managers is None:  # noqa: E501
            raise ValueError("Invalid value for `team_managers`, must not be `None`")  # noqa: E501

        self._team_managers = team_managers

    @property
    def max_managed_virtualization_realms(self):
        """Gets the max_managed_virtualization_realms of this InputTeamFull.  # noqa: E501


        :return: The max_managed_virtualization_realms of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_managed_virtualization_realms

    @max_managed_virtualization_realms.setter
    def max_managed_virtualization_realms(self, max_managed_virtualization_realms):
        """Sets the max_managed_virtualization_realms of this InputTeamFull.


        :param max_managed_virtualization_realms: The max_managed_virtualization_realms of this InputTeamFull.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_managed_virtualization_realms is not None and max_managed_virtualization_realms < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_managed_virtualization_realms`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_managed_virtualization_realms = max_managed_virtualization_realms

    @property
    def max_num_cpus(self):
        """Gets the max_num_cpus of this InputTeamFull.  # noqa: E501


        :return: The max_num_cpus of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_num_cpus

    @max_num_cpus.setter
    def max_num_cpus(self, max_num_cpus):
        """Sets the max_num_cpus of this InputTeamFull.


        :param max_num_cpus: The max_num_cpus of this InputTeamFull.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_num_cpus is not None and max_num_cpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_num_cpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_num_cpus = max_num_cpus

    @property
    def max_num_gpus(self):
        """Gets the max_num_gpus of this InputTeamFull.  # noqa: E501


        :return: The max_num_gpus of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_num_gpus

    @max_num_gpus.setter
    def max_num_gpus(self, max_num_gpus):
        """Sets the max_num_gpus of this InputTeamFull.


        :param max_num_gpus: The max_num_gpus of this InputTeamFull.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_num_gpus is not None and max_num_gpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_num_gpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_num_gpus = max_num_gpus

    @property
    def max_projects(self):
        """Gets the max_projects of this InputTeamFull.  # noqa: E501


        :return: The max_projects of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_projects

    @max_projects.setter
    def max_projects(self, max_projects):
        """Sets the max_projects of this InputTeamFull.


        :param max_projects: The max_projects of this InputTeamFull.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_projects is not None and max_projects < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_projects`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_projects = max_projects

    @property
    def max_ram_in_megabytes(self):
        """Gets the max_ram_in_megabytes of this InputTeamFull.  # noqa: E501


        :return: The max_ram_in_megabytes of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_ram_in_megabytes

    @max_ram_in_megabytes.setter
    def max_ram_in_megabytes(self, max_ram_in_megabytes):
        """Sets the max_ram_in_megabytes of this InputTeamFull.


        :param max_ram_in_megabytes: The max_ram_in_megabytes of this InputTeamFull.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_ram_in_megabytes is not None and max_ram_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_ram_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_ram_in_megabytes = max_ram_in_megabytes

    @property
    def max_shared_remote_access_sessions(self):
        """Gets the max_shared_remote_access_sessions of this InputTeamFull.  # noqa: E501


        :return: The max_shared_remote_access_sessions of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_shared_remote_access_sessions

    @max_shared_remote_access_sessions.setter
    def max_shared_remote_access_sessions(self, max_shared_remote_access_sessions):
        """Sets the max_shared_remote_access_sessions of this InputTeamFull.


        :param max_shared_remote_access_sessions: The max_shared_remote_access_sessions of this InputTeamFull.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_shared_remote_access_sessions is not None and max_shared_remote_access_sessions < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_shared_remote_access_sessions`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_shared_remote_access_sessions = max_shared_remote_access_sessions

    @property
    def max_storage_in_megabytes(self):
        """Gets the max_storage_in_megabytes of this InputTeamFull.  # noqa: E501


        :return: The max_storage_in_megabytes of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_storage_in_megabytes

    @max_storage_in_megabytes.setter
    def max_storage_in_megabytes(self, max_storage_in_megabytes):
        """Sets the max_storage_in_megabytes of this InputTeamFull.


        :param max_storage_in_megabytes: The max_storage_in_megabytes of this InputTeamFull.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_storage_in_megabytes is not None and max_storage_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_storage_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_storage_in_megabytes = max_storage_in_megabytes

    @property
    def max_users(self):
        """Gets the max_users of this InputTeamFull.  # noqa: E501


        :return: The max_users of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_users

    @max_users.setter
    def max_users(self, max_users):
        """Sets the max_users of this InputTeamFull.


        :param max_users: The max_users of this InputTeamFull.  # noqa: E501
        :type: int
        """

        self._max_users = max_users

    @property
    def max_virtual_machines(self):
        """Gets the max_virtual_machines of this InputTeamFull.  # noqa: E501


        :return: The max_virtual_machines of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._max_virtual_machines

    @max_virtual_machines.setter
    def max_virtual_machines(self, max_virtual_machines):
        """Sets the max_virtual_machines of this InputTeamFull.


        :param max_virtual_machines: The max_virtual_machines of this InputTeamFull.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_virtual_machines is not None and max_virtual_machines < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_virtual_machines`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_virtual_machines = max_virtual_machines

    @property
    def name(self):
        """Gets the name of this InputTeamFull.  # noqa: E501


        :return: The name of this InputTeamFull.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputTeamFull.


        :param name: The name of this InputTeamFull.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def order_number(self):
        """Gets the order_number of this InputTeamFull.  # noqa: E501


        :return: The order_number of this InputTeamFull.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this InputTeamFull.


        :param order_number: The order_number of this InputTeamFull.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def contact_info(self):
        """Gets the contact_info of this InputTeamFull.  # noqa: E501


        :return: The contact_info of this InputTeamFull.  # noqa: E501
        :rtype: PocInfo
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Sets the contact_info of this InputTeamFull.


        :param contact_info: The contact_info of this InputTeamFull.  # noqa: E501
        :type: PocInfo
        """
        if self.local_vars_configuration.client_side_validation and contact_info is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_info`, must not be `None`")  # noqa: E501

        self._contact_info = contact_info

    @property
    def power_schedule_enabled(self):
        """Gets the power_schedule_enabled of this InputTeamFull.  # noqa: E501


        :return: The power_schedule_enabled of this InputTeamFull.  # noqa: E501
        :rtype: bool
        """
        return self._power_schedule_enabled

    @power_schedule_enabled.setter
    def power_schedule_enabled(self, power_schedule_enabled):
        """Sets the power_schedule_enabled of this InputTeamFull.


        :param power_schedule_enabled: The power_schedule_enabled of this InputTeamFull.  # noqa: E501
        :type: bool
        """

        self._power_schedule_enabled = power_schedule_enabled

    @property
    def private(self):
        """Gets the private of this InputTeamFull.  # noqa: E501


        :return: The private of this InputTeamFull.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this InputTeamFull.


        :param private: The private of this InputTeamFull.  # noqa: E501
        :type: bool
        """

        self._private = private

    @property
    def rdp_client_proxy_enabled(self):
        """Gets the rdp_client_proxy_enabled of this InputTeamFull.  # noqa: E501


        :return: The rdp_client_proxy_enabled of this InputTeamFull.  # noqa: E501
        :rtype: bool
        """
        return self._rdp_client_proxy_enabled

    @rdp_client_proxy_enabled.setter
    def rdp_client_proxy_enabled(self, rdp_client_proxy_enabled):
        """Sets the rdp_client_proxy_enabled of this InputTeamFull.


        :param rdp_client_proxy_enabled: The rdp_client_proxy_enabled of this InputTeamFull.  # noqa: E501
        :type: bool
        """

        self._rdp_client_proxy_enabled = rdp_client_proxy_enabled

    @property
    def rdp_client_session_duration(self):
        """Gets the rdp_client_session_duration of this InputTeamFull.  # noqa: E501


        :return: The rdp_client_session_duration of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._rdp_client_session_duration

    @rdp_client_session_duration.setter
    def rdp_client_session_duration(self, rdp_client_session_duration):
        """Sets the rdp_client_session_duration of this InputTeamFull.


        :param rdp_client_session_duration: The rdp_client_session_duration of this InputTeamFull.  # noqa: E501
        :type: int
        """

        self._rdp_client_session_duration = rdp_client_session_duration

    @property
    def snapshot_enabled(self):
        """Gets the snapshot_enabled of this InputTeamFull.  # noqa: E501


        :return: The snapshot_enabled of this InputTeamFull.  # noqa: E501
        :rtype: bool
        """
        return self._snapshot_enabled

    @snapshot_enabled.setter
    def snapshot_enabled(self, snapshot_enabled):
        """Sets the snapshot_enabled of this InputTeamFull.


        :param snapshot_enabled: The snapshot_enabled of this InputTeamFull.  # noqa: E501
        :type: bool
        """

        self._snapshot_enabled = snapshot_enabled

    @property
    def state(self):
        """Gets the state of this InputTeamFull.  # noqa: E501


        :return: The state of this InputTeamFull.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InputTeamFull.


        :param state: The state of this InputTeamFull.  # noqa: E501
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
    def valid_until(self):
        """Gets the valid_until of this InputTeamFull.  # noqa: E501


        :return: The valid_until of this InputTeamFull.  # noqa: E501
        :rtype: int
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this InputTeamFull.


        :param valid_until: The valid_until of this InputTeamFull.  # noqa: E501
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
        if not isinstance(other, InputTeamFull):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputTeamFull):
            return True

        return self.to_dict() != other.to_dict()
