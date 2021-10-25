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


class Project(object):
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
        'active_member_count': 'int',
        'created_at': 'int',
        'default_power_schedule': 'PowerSchedule',
        'default_role': 'str',
        'default_virtualization_realm': 'VirtualizationRealm',
        'description': 'str',
        'features': 'ProjectFeatures',
        'id': 'int',
        'itar_comment': 'str',
        'itar_restricted': 'bool',
        'limits': 'ProjectLimits',
        'total_member_count': 'int',
        'name': 'str',
        'owning_team': 'Team',
        'is_private': 'bool',
        'trusted_projects': 'list[Project]',
        'resource_usage': 'ResourceUsage',
        'submission_services': 'list[SubmissionService]',
        'updated_at': 'int',
        'members': 'list[User]',
        'virtualization_realms': 'list[VirtualizationRealm]'
    }

    attribute_map = {
        'active_member_count': 'activeMemberCount',
        'created_at': 'createdAt',
        'default_power_schedule': 'defaultPowerSchedule',
        'default_role': 'defaultRole',
        'default_virtualization_realm': 'defaultVirtualizationRealm',
        'description': 'description',
        'features': 'features',
        'id': 'id',
        'itar_comment': 'itarComment',
        'itar_restricted': 'itarRestricted',
        'limits': 'limits',
        'total_member_count': 'totalMemberCount',
        'name': 'name',
        'owning_team': 'owningTeam',
        'is_private': 'isPrivate',
        'trusted_projects': 'trustedProjects',
        'resource_usage': 'resourceUsage',
        'submission_services': 'submissionServices',
        'updated_at': 'updatedAt',
        'members': 'members',
        'virtualization_realms': 'virtualizationRealms'
    }

    def __init__(self, active_member_count=None, created_at=None, default_power_schedule=None, default_role=None, default_virtualization_realm=None, description=None, features=None, id=None, itar_comment=None, itar_restricted=None, limits=None, total_member_count=None, name=None, owning_team=None, is_private=None, trusted_projects=None, resource_usage=None, submission_services=None, updated_at=None, members=None, virtualization_realms=None, local_vars_configuration=None):  # noqa: E501
        """Project - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._active_member_count = None
        self._created_at = None
        self._default_power_schedule = None
        self._default_role = None
        self._default_virtualization_realm = None
        self._description = None
        self._features = None
        self._id = None
        self._itar_comment = None
        self._itar_restricted = None
        self._limits = None
        self._total_member_count = None
        self._name = None
        self._owning_team = None
        self._is_private = None
        self._trusted_projects = None
        self._resource_usage = None
        self._submission_services = None
        self._updated_at = None
        self._members = None
        self._virtualization_realms = None
        self.discriminator = None

        if active_member_count is not None:
            self.active_member_count = active_member_count
        if created_at is not None:
            self.created_at = created_at
        if default_power_schedule is not None:
            self.default_power_schedule = default_power_schedule
        if default_role is not None:
            self.default_role = default_role
        if default_virtualization_realm is not None:
            self.default_virtualization_realm = default_virtualization_realm
        if description is not None:
            self.description = description
        if features is not None:
            self.features = features
        self.id = id
        if itar_comment is not None:
            self.itar_comment = itar_comment
        if itar_restricted is not None:
            self.itar_restricted = itar_restricted
        self.limits = limits
        if total_member_count is not None:
            self.total_member_count = total_member_count
        if name is not None:
            self.name = name
        if owning_team is not None:
            self.owning_team = owning_team
        if is_private is not None:
            self.is_private = is_private
        if trusted_projects is not None:
            self.trusted_projects = trusted_projects
        if resource_usage is not None:
            self.resource_usage = resource_usage
        if submission_services is not None:
            self.submission_services = submission_services
        if updated_at is not None:
            self.updated_at = updated_at
        if members is not None:
            self.members = members
        if virtualization_realms is not None:
            self.virtualization_realms = virtualization_realms

    @property
    def active_member_count(self):
        """Gets the active_member_count of this Project.  # noqa: E501


        :return: The active_member_count of this Project.  # noqa: E501
        :rtype: int
        """
        return self._active_member_count

    @active_member_count.setter
    def active_member_count(self, active_member_count):
        """Sets the active_member_count of this Project.


        :param active_member_count: The active_member_count of this Project.  # noqa: E501
        :type: int
        """

        self._active_member_count = active_member_count

    @property
    def created_at(self):
        """Gets the created_at of this Project.  # noqa: E501


        :return: The created_at of this Project.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Project.


        :param created_at: The created_at of this Project.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def default_power_schedule(self):
        """Gets the default_power_schedule of this Project.  # noqa: E501


        :return: The default_power_schedule of this Project.  # noqa: E501
        :rtype: PowerSchedule
        """
        return self._default_power_schedule

    @default_power_schedule.setter
    def default_power_schedule(self, default_power_schedule):
        """Sets the default_power_schedule of this Project.


        :param default_power_schedule: The default_power_schedule of this Project.  # noqa: E501
        :type: PowerSchedule
        """

        self._default_power_schedule = default_power_schedule

    @property
    def default_role(self):
        """Gets the default_role of this Project.  # noqa: E501


        :return: The default_role of this Project.  # noqa: E501
        :rtype: str
        """
        return self._default_role

    @default_role.setter
    def default_role(self, default_role):
        """Sets the default_role of this Project.


        :param default_role: The default_role of this Project.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADMINISTRATOR", "ASSET_RESTORER", "STATUS_READER", "UI_MACHINE", "TEST_TOOL", "MEMBER", "CONSUMER", "STANDARD", "SOFTWARE_DEVELOPER", "TEST_DEVELOPER", "ASSET_SHARER", "ASSET_PROMOTER", "POWER_SCHEDULE_UPDATER", "PROJECT_OWNER", "PROJECT_MANAGER", "PROJECT_MODERATOR", "REMOTE_ACCESS", "MAESTRO_MACHINE", "FAP_MACHINE", "SCHEDULER_MACHINE", "CONS3RT_MACHINE", "SOURCEBUILDER_MACHINE", "SYSTEM_ASSET_IMPORTER", "ASSET_CERTIFIER", "ASSET_UPLOADER"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and default_role not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `default_role` ({0}), must be one of {1}"  # noqa: E501
                .format(default_role, allowed_values)
            )

        self._default_role = default_role

    @property
    def default_virtualization_realm(self):
        """Gets the default_virtualization_realm of this Project.  # noqa: E501


        :return: The default_virtualization_realm of this Project.  # noqa: E501
        :rtype: VirtualizationRealm
        """
        return self._default_virtualization_realm

    @default_virtualization_realm.setter
    def default_virtualization_realm(self, default_virtualization_realm):
        """Sets the default_virtualization_realm of this Project.


        :param default_virtualization_realm: The default_virtualization_realm of this Project.  # noqa: E501
        :type: VirtualizationRealm
        """

        self._default_virtualization_realm = default_virtualization_realm

    @property
    def description(self):
        """Gets the description of this Project.  # noqa: E501


        :return: The description of this Project.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Project.


        :param description: The description of this Project.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def features(self):
        """Gets the features of this Project.  # noqa: E501


        :return: The features of this Project.  # noqa: E501
        :rtype: ProjectFeatures
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this Project.


        :param features: The features of this Project.  # noqa: E501
        :type: ProjectFeatures
        """

        self._features = features

    @property
    def id(self):
        """Gets the id of this Project.  # noqa: E501


        :return: The id of this Project.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Project.


        :param id: The id of this Project.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def itar_comment(self):
        """Gets the itar_comment of this Project.  # noqa: E501


        :return: The itar_comment of this Project.  # noqa: E501
        :rtype: str
        """
        return self._itar_comment

    @itar_comment.setter
    def itar_comment(self, itar_comment):
        """Sets the itar_comment of this Project.


        :param itar_comment: The itar_comment of this Project.  # noqa: E501
        :type: str
        """

        self._itar_comment = itar_comment

    @property
    def itar_restricted(self):
        """Gets the itar_restricted of this Project.  # noqa: E501


        :return: The itar_restricted of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._itar_restricted

    @itar_restricted.setter
    def itar_restricted(self, itar_restricted):
        """Sets the itar_restricted of this Project.


        :param itar_restricted: The itar_restricted of this Project.  # noqa: E501
        :type: bool
        """

        self._itar_restricted = itar_restricted

    @property
    def limits(self):
        """Gets the limits of this Project.  # noqa: E501


        :return: The limits of this Project.  # noqa: E501
        :rtype: ProjectLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this Project.


        :param limits: The limits of this Project.  # noqa: E501
        :type: ProjectLimits
        """
        if self.local_vars_configuration.client_side_validation and limits is None:  # noqa: E501
            raise ValueError("Invalid value for `limits`, must not be `None`")  # noqa: E501

        self._limits = limits

    @property
    def total_member_count(self):
        """Gets the total_member_count of this Project.  # noqa: E501


        :return: The total_member_count of this Project.  # noqa: E501
        :rtype: int
        """
        return self._total_member_count

    @total_member_count.setter
    def total_member_count(self, total_member_count):
        """Sets the total_member_count of this Project.


        :param total_member_count: The total_member_count of this Project.  # noqa: E501
        :type: int
        """

        self._total_member_count = total_member_count

    @property
    def name(self):
        """Gets the name of this Project.  # noqa: E501


        :return: The name of this Project.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Project.


        :param name: The name of this Project.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owning_team(self):
        """Gets the owning_team of this Project.  # noqa: E501


        :return: The owning_team of this Project.  # noqa: E501
        :rtype: Team
        """
        return self._owning_team

    @owning_team.setter
    def owning_team(self, owning_team):
        """Sets the owning_team of this Project.


        :param owning_team: The owning_team of this Project.  # noqa: E501
        :type: Team
        """

        self._owning_team = owning_team

    @property
    def is_private(self):
        """Gets the is_private of this Project.  # noqa: E501


        :return: The is_private of this Project.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this Project.


        :param is_private: The is_private of this Project.  # noqa: E501
        :type: bool
        """

        self._is_private = is_private

    @property
    def trusted_projects(self):
        """Gets the trusted_projects of this Project.  # noqa: E501


        :return: The trusted_projects of this Project.  # noqa: E501
        :rtype: list[Project]
        """
        return self._trusted_projects

    @trusted_projects.setter
    def trusted_projects(self, trusted_projects):
        """Sets the trusted_projects of this Project.


        :param trusted_projects: The trusted_projects of this Project.  # noqa: E501
        :type: list[Project]
        """

        self._trusted_projects = trusted_projects

    @property
    def resource_usage(self):
        """Gets the resource_usage of this Project.  # noqa: E501


        :return: The resource_usage of this Project.  # noqa: E501
        :rtype: ResourceUsage
        """
        return self._resource_usage

    @resource_usage.setter
    def resource_usage(self, resource_usage):
        """Sets the resource_usage of this Project.


        :param resource_usage: The resource_usage of this Project.  # noqa: E501
        :type: ResourceUsage
        """

        self._resource_usage = resource_usage

    @property
    def submission_services(self):
        """Gets the submission_services of this Project.  # noqa: E501


        :return: The submission_services of this Project.  # noqa: E501
        :rtype: list[SubmissionService]
        """
        return self._submission_services

    @submission_services.setter
    def submission_services(self, submission_services):
        """Sets the submission_services of this Project.


        :param submission_services: The submission_services of this Project.  # noqa: E501
        :type: list[SubmissionService]
        """

        self._submission_services = submission_services

    @property
    def updated_at(self):
        """Gets the updated_at of this Project.  # noqa: E501


        :return: The updated_at of this Project.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Project.


        :param updated_at: The updated_at of this Project.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def members(self):
        """Gets the members of this Project.  # noqa: E501


        :return: The members of this Project.  # noqa: E501
        :rtype: list[User]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this Project.


        :param members: The members of this Project.  # noqa: E501
        :type: list[User]
        """

        self._members = members

    @property
    def virtualization_realms(self):
        """Gets the virtualization_realms of this Project.  # noqa: E501


        :return: The virtualization_realms of this Project.  # noqa: E501
        :rtype: list[VirtualizationRealm]
        """
        return self._virtualization_realms

    @virtualization_realms.setter
    def virtualization_realms(self, virtualization_realms):
        """Sets the virtualization_realms of this Project.


        :param virtualization_realms: The virtualization_realms of this Project.  # noqa: E501
        :type: list[VirtualizationRealm]
        """

        self._virtualization_realms = virtualization_realms

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
        if not isinstance(other, Project):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Project):
            return True

        return self.to_dict() != other.to_dict()
