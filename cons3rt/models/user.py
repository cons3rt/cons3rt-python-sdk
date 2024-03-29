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


class User(object):
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
        'created_at': 'int',
        'updated_at': 'int',
        'administered_clouds': 'list[Cloud]',
        'administered_virt_realms': 'list[VirtualizationRealm]',
        'certificates': 'list[Certificate]',
        'comment': 'str',
        'default_project': 'Project',
        'email': 'str',
        'firstname': 'str',
        'id': 'int',
        'lastname': 'str',
        'log_entries': 'list[LogEntry]',
        'organization': 'str',
        'project_count': 'int',
        'state': 'str',
        'terms_of_service_accepted': 'bool',
        'username': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'administered_clouds': 'administeredClouds',
        'administered_virt_realms': 'administeredVirtRealms',
        'certificates': 'certificates',
        'comment': 'comment',
        'default_project': 'defaultProject',
        'email': 'email',
        'firstname': 'firstname',
        'id': 'id',
        'lastname': 'lastname',
        'log_entries': 'logEntries',
        'organization': 'organization',
        'project_count': 'projectCount',
        'state': 'state',
        'terms_of_service_accepted': 'termsOfServiceAccepted',
        'username': 'username'
    }

    def __init__(self, created_at=None, updated_at=None, administered_clouds=None, administered_virt_realms=None, certificates=None, comment=None, default_project=None, email=None, firstname=None, id=None, lastname=None, log_entries=None, organization=None, project_count=None, state=None, terms_of_service_accepted=None, username=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_at = None
        self._updated_at = None
        self._administered_clouds = None
        self._administered_virt_realms = None
        self._certificates = None
        self._comment = None
        self._default_project = None
        self._email = None
        self._firstname = None
        self._id = None
        self._lastname = None
        self._log_entries = None
        self._organization = None
        self._project_count = None
        self._state = None
        self._terms_of_service_accepted = None
        self._username = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if administered_clouds is not None:
            self.administered_clouds = administered_clouds
        if administered_virt_realms is not None:
            self.administered_virt_realms = administered_virt_realms
        if certificates is not None:
            self.certificates = certificates
        if comment is not None:
            self.comment = comment
        if default_project is not None:
            self.default_project = default_project
        if email is not None:
            self.email = email
        if firstname is not None:
            self.firstname = firstname
        if id is not None:
            self.id = id
        if lastname is not None:
            self.lastname = lastname
        if log_entries is not None:
            self.log_entries = log_entries
        if organization is not None:
            self.organization = organization
        if project_count is not None:
            self.project_count = project_count
        if state is not None:
            self.state = state
        if terms_of_service_accepted is not None:
            self.terms_of_service_accepted = terms_of_service_accepted
        if username is not None:
            self.username = username

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501


        :return: The created_at of this User.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.


        :param created_at: The created_at of this User.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this User.  # noqa: E501


        :return: The updated_at of this User.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this User.


        :param updated_at: The updated_at of this User.  # noqa: E501
        :type: int
        """

        self._updated_at = updated_at

    @property
    def administered_clouds(self):
        """Gets the administered_clouds of this User.  # noqa: E501


        :return: The administered_clouds of this User.  # noqa: E501
        :rtype: list[Cloud]
        """
        return self._administered_clouds

    @administered_clouds.setter
    def administered_clouds(self, administered_clouds):
        """Sets the administered_clouds of this User.


        :param administered_clouds: The administered_clouds of this User.  # noqa: E501
        :type: list[Cloud]
        """

        self._administered_clouds = administered_clouds

    @property
    def administered_virt_realms(self):
        """Gets the administered_virt_realms of this User.  # noqa: E501


        :return: The administered_virt_realms of this User.  # noqa: E501
        :rtype: list[VirtualizationRealm]
        """
        return self._administered_virt_realms

    @administered_virt_realms.setter
    def administered_virt_realms(self, administered_virt_realms):
        """Sets the administered_virt_realms of this User.


        :param administered_virt_realms: The administered_virt_realms of this User.  # noqa: E501
        :type: list[VirtualizationRealm]
        """

        self._administered_virt_realms = administered_virt_realms

    @property
    def certificates(self):
        """Gets the certificates of this User.  # noqa: E501


        :return: The certificates of this User.  # noqa: E501
        :rtype: list[Certificate]
        """
        return self._certificates

    @certificates.setter
    def certificates(self, certificates):
        """Sets the certificates of this User.


        :param certificates: The certificates of this User.  # noqa: E501
        :type: list[Certificate]
        """

        self._certificates = certificates

    @property
    def comment(self):
        """Gets the comment of this User.  # noqa: E501


        :return: The comment of this User.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this User.


        :param comment: The comment of this User.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def default_project(self):
        """Gets the default_project of this User.  # noqa: E501


        :return: The default_project of this User.  # noqa: E501
        :rtype: Project
        """
        return self._default_project

    @default_project.setter
    def default_project(self, default_project):
        """Sets the default_project of this User.


        :param default_project: The default_project of this User.  # noqa: E501
        :type: Project
        """

        self._default_project = default_project

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this User.  # noqa: E501


        :return: The firstname of this User.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this User.


        :param firstname: The firstname of this User.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def lastname(self):
        """Gets the lastname of this User.  # noqa: E501


        :return: The lastname of this User.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this User.


        :param lastname: The lastname of this User.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def log_entries(self):
        """Gets the log_entries of this User.  # noqa: E501


        :return: The log_entries of this User.  # noqa: E501
        :rtype: list[LogEntry]
        """
        return self._log_entries

    @log_entries.setter
    def log_entries(self, log_entries):
        """Sets the log_entries of this User.


        :param log_entries: The log_entries of this User.  # noqa: E501
        :type: list[LogEntry]
        """

        self._log_entries = log_entries

    @property
    def organization(self):
        """Gets the organization of this User.  # noqa: E501


        :return: The organization of this User.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this User.


        :param organization: The organization of this User.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def project_count(self):
        """Gets the project_count of this User.  # noqa: E501


        :return: The project_count of this User.  # noqa: E501
        :rtype: int
        """
        return self._project_count

    @project_count.setter
    def project_count(self, project_count):
        """Sets the project_count of this User.


        :param project_count: The project_count of this User.  # noqa: E501
        :type: int
        """

        self._project_count = project_count

    @property
    def state(self):
        """Gets the state of this User.  # noqa: E501


        :return: The state of this User.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this User.


        :param state: The state of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUESTED", "ACTIVE", "INACTIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def terms_of_service_accepted(self):
        """Gets the terms_of_service_accepted of this User.  # noqa: E501


        :return: The terms_of_service_accepted of this User.  # noqa: E501
        :rtype: bool
        """
        return self._terms_of_service_accepted

    @terms_of_service_accepted.setter
    def terms_of_service_accepted(self, terms_of_service_accepted):
        """Sets the terms_of_service_accepted of this User.


        :param terms_of_service_accepted: The terms_of_service_accepted of this User.  # noqa: E501
        :type: bool
        """

        self._terms_of_service_accepted = terms_of_service_accepted

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501


        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.


        :param username: The username of this User.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
