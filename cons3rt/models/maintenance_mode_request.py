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


class MaintenanceModeRequest(object):
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
        'end_date': 'int',
        'message': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'end_date': 'endDate',
        'message': 'message',
        'timeout': 'timeout'
    }

    def __init__(self, end_date=None, message=None, timeout=None, local_vars_configuration=None):  # noqa: E501
        """MaintenanceModeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._end_date = None
        self._message = None
        self._timeout = None
        self.discriminator = None

        if end_date is not None:
            self.end_date = end_date
        if message is not None:
            self.message = message
        if timeout is not None:
            self.timeout = timeout

    @property
    def end_date(self):
        """Gets the end_date of this MaintenanceModeRequest.  # noqa: E501


        :return: The end_date of this MaintenanceModeRequest.  # noqa: E501
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this MaintenanceModeRequest.


        :param end_date: The end_date of this MaintenanceModeRequest.  # noqa: E501
        :type: int
        """

        self._end_date = end_date

    @property
    def message(self):
        """Gets the message of this MaintenanceModeRequest.  # noqa: E501


        :return: The message of this MaintenanceModeRequest.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this MaintenanceModeRequest.


        :param message: The message of this MaintenanceModeRequest.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def timeout(self):
        """Gets the timeout of this MaintenanceModeRequest.  # noqa: E501


        :return: The timeout of this MaintenanceModeRequest.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this MaintenanceModeRequest.


        :param timeout: The timeout of this MaintenanceModeRequest.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

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
        if not isinstance(other, MaintenanceModeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MaintenanceModeRequest):
            return True

        return self.to_dict() != other.to_dict()
