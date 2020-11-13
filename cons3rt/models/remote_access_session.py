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


class RemoteAccessSession(object):
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
        'end_date': 'datetime',
        'id': 'int',
        'low_bandwidth': 'bool',
        'start_date': 'datetime',
        'username': 'str',
        'type': 'str'
    }

    attribute_map = {
        'end_date': 'endDate',
        'id': 'id',
        'low_bandwidth': 'lowBandwidth',
        'start_date': 'startDate',
        'username': 'username',
        'type': 'type'
    }

    def __init__(self, end_date=None, id=None, low_bandwidth=None, start_date=None, username=None, type=None, local_vars_configuration=None):  # noqa: E501
        """RemoteAccessSession - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_date = None
        self._id = None
        self._low_bandwidth = None
        self._start_date = None
        self._username = None
        self._type = None
        self.discriminator = None

        if end_date is not None:
            self.end_date = end_date
        if id is not None:
            self.id = id
        if low_bandwidth is not None:
            self.low_bandwidth = low_bandwidth
        if start_date is not None:
            self.start_date = start_date
        if username is not None:
            self.username = username
        if type is not None:
            self.type = type

    @property
    def end_date(self):
        """Gets the end_date of this RemoteAccessSession.  # noqa: E501


        :return: The end_date of this RemoteAccessSession.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this RemoteAccessSession.


        :param end_date: The end_date of this RemoteAccessSession.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def id(self):
        """Gets the id of this RemoteAccessSession.  # noqa: E501


        :return: The id of this RemoteAccessSession.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RemoteAccessSession.


        :param id: The id of this RemoteAccessSession.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def low_bandwidth(self):
        """Gets the low_bandwidth of this RemoteAccessSession.  # noqa: E501


        :return: The low_bandwidth of this RemoteAccessSession.  # noqa: E501
        :rtype: bool
        """
        return self._low_bandwidth

    @low_bandwidth.setter
    def low_bandwidth(self, low_bandwidth):
        """Sets the low_bandwidth of this RemoteAccessSession.


        :param low_bandwidth: The low_bandwidth of this RemoteAccessSession.  # noqa: E501
        :type: bool
        """

        self._low_bandwidth = low_bandwidth

    @property
    def start_date(self):
        """Gets the start_date of this RemoteAccessSession.  # noqa: E501


        :return: The start_date of this RemoteAccessSession.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this RemoteAccessSession.


        :param start_date: The start_date of this RemoteAccessSession.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def username(self):
        """Gets the username of this RemoteAccessSession.  # noqa: E501


        :return: The username of this RemoteAccessSession.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this RemoteAccessSession.


        :param username: The username of this RemoteAccessSession.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def type(self):
        """Gets the type of this RemoteAccessSession.  # noqa: E501


        :return: The type of this RemoteAccessSession.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RemoteAccessSession.


        :param type: The type of this RemoteAccessSession.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "SSH", "VNC", "RDP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, RemoteAccessSession):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteAccessSession):
            return True

        return self.to_dict() != other.to_dict()
