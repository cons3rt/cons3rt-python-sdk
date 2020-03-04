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


class LogEntry(object):
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
        'message': 'str',
        'project_name': 'str',
        'severity': 'str',
        'source': 'str',
        'time': 'datetime',
        'username': 'str'
    }

    attribute_map = {
        'id': 'id',
        'message': 'message',
        'project_name': 'projectName',
        'severity': 'severity',
        'source': 'source',
        'time': 'time',
        'username': 'username'
    }

    def __init__(self, id=None, message=None, project_name=None, severity=None, source=None, time=None, username=None, local_vars_configuration=None):  # noqa: E501
        """LogEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._message = None
        self._project_name = None
        self._severity = None
        self._source = None
        self._time = None
        self._username = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if message is not None:
            self.message = message
        if project_name is not None:
            self.project_name = project_name
        if severity is not None:
            self.severity = severity
        if source is not None:
            self.source = source
        if time is not None:
            self.time = time
        if username is not None:
            self.username = username

    @property
    def id(self):
        """Gets the id of this LogEntry.  # noqa: E501


        :return: The id of this LogEntry.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LogEntry.


        :param id: The id of this LogEntry.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def message(self):
        """Gets the message of this LogEntry.  # noqa: E501


        :return: The message of this LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LogEntry.


        :param message: The message of this LogEntry.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def project_name(self):
        """Gets the project_name of this LogEntry.  # noqa: E501


        :return: The project_name of this LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this LogEntry.


        :param project_name: The project_name of this LogEntry.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def severity(self):
        """Gets the severity of this LogEntry.  # noqa: E501


        :return: The severity of this LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this LogEntry.


        :param severity: The severity of this LogEntry.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEBUG", "INFO", "WARNING", "ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and severity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def source(self):
        """Gets the source of this LogEntry.  # noqa: E501


        :return: The source of this LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this LogEntry.


        :param source: The source of this LogEntry.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def time(self):
        """Gets the time of this LogEntry.  # noqa: E501


        :return: The time of this LogEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this LogEntry.


        :param time: The time of this LogEntry.  # noqa: E501
        :type: datetime
        """

        self._time = time

    @property
    def username(self):
        """Gets the username of this LogEntry.  # noqa: E501


        :return: The username of this LogEntry.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this LogEntry.


        :param username: The username of this LogEntry.  # noqa: E501
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
        if not isinstance(other, LogEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LogEntry):
            return True

        return self.to_dict() != other.to_dict()
