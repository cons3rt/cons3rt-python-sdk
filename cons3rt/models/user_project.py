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


class UserProject(object):
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
        'id': 'int',
        'username': 'str',
        'email': 'str',
        'membership_state': 'str',
        'roles': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'email': 'email',
        'membership_state': 'membershipState',
        'roles': 'roles'
    }

    def __init__(self, id=None, username=None, email=None, membership_state=None, roles=None, local_vars_configuration=None):  # noqa: E501
        """UserProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._email = None
        self._membership_state = None
        self._roles = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if membership_state is not None:
            self.membership_state = membership_state
        if roles is not None:
            self.roles = roles

    @property
    def id(self):
        """Gets the id of this UserProject.  # noqa: E501


        :return: The id of this UserProject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserProject.


        :param id: The id of this UserProject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this UserProject.  # noqa: E501


        :return: The username of this UserProject.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserProject.


        :param username: The username of this UserProject.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this UserProject.  # noqa: E501


        :return: The email of this UserProject.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserProject.


        :param email: The email of this UserProject.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def membership_state(self):
        """Gets the membership_state of this UserProject.  # noqa: E501


        :return: The membership_state of this UserProject.  # noqa: E501
        :rtype: str
        """
        return self._membership_state

    @membership_state.setter
    def membership_state(self, membership_state):
        """Sets the membership_state of this UserProject.


        :param membership_state: The membership_state of this UserProject.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUESTED", "ACTIVE", "BLOCKED", "DELETED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and membership_state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `membership_state` ({0}), must be one of {1}"  # noqa: E501
                .format(membership_state, allowed_values)
            )

        self._membership_state = membership_state

    @property
    def roles(self):
        """Gets the roles of this UserProject.  # noqa: E501


        :return: The roles of this UserProject.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserProject.


        :param roles: The roles of this UserProject.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ADMINISTRATOR", "ASSET_RESTORER", "STATUS_READER", "UI_MACHINE", "TEST_TOOL", "MEMBER", "CONSUMER", "STANDARD", "SOFTWARE_DEVELOPER", "TEST_DEVELOPER", "ASSET_SHARER", "ASSET_PROMOTER", "POWER_SCHEDULE_UPDATER", "PROJECT_OWNER", "PROJECT_MANAGER", "PROJECT_MODERATOR", "REMOTE_ACCESS", "MAESTRO_MACHINE", "FAP_MACHINE", "SCHEDULER_MACHINE", "CONS3RT_MACHINE", "SOURCEBUILDER_MACHINE", "SYSTEM_ASSET_IMPORTER", "ASSET_CERTIFIER", "ASSET_UPLOADER"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(roles).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `roles` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(roles) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._roles = roles

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
        if not isinstance(other, UserProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserProject):
            return True

        return self.to_dict() != other.to_dict()
