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


class SubmissionEndpoint(object):
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
        'host': 'str',
        'id': 'int',
        'port': 'int',
        'type': 'str',
        'subtype': 'str'
    }

    attribute_map = {
        'host': 'host',
        'id': 'id',
        'port': 'port',
        'type': 'type',
        'subtype': 'subtype'
    }

    discriminator_value_class_map = {
        'PathBasedSubmissionEndpoint': 'PathBasedSubmissionEndpoint',
        'DockerRegistrySubmissionEndpoint': 'DockerRegistrySubmissionEndpoint'
    }

    def __init__(self, host=None, id=None, port=None, type=None, subtype=None, local_vars_configuration=None):  # noqa: E501
        """SubmissionEndpoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._id = None
        self._port = None
        self._type = None
        self._subtype = None
        self.discriminator = 'subtype'

        self.host = host
        if id is not None:
            self.id = id
        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        self.subtype = subtype

    @property
    def host(self):
        """Gets the host of this SubmissionEndpoint.  # noqa: E501


        :return: The host of this SubmissionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SubmissionEndpoint.


        :param host: The host of this SubmissionEndpoint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def id(self):
        """Gets the id of this SubmissionEndpoint.  # noqa: E501


        :return: The id of this SubmissionEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubmissionEndpoint.


        :param id: The id of this SubmissionEndpoint.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def port(self):
        """Gets the port of this SubmissionEndpoint.  # noqa: E501


        :return: The port of this SubmissionEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SubmissionEndpoint.


        :param port: The port of this SubmissionEndpoint.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def type(self):
        """Gets the type of this SubmissionEndpoint.  # noqa: E501


        :return: The type of this SubmissionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubmissionEndpoint.


        :param type: The type of this SubmissionEndpoint.  # noqa: E501
        :type: str
        """
        allowed_values = ["DockerRegistryEndpoint", "HttpPostEndpoint", "S3Endpoint", "SFTPEndpoint"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def subtype(self):
        """Gets the subtype of this SubmissionEndpoint.  # noqa: E501


        :return: The subtype of this SubmissionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this SubmissionEndpoint.


        :param subtype: The subtype of this SubmissionEndpoint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, SubmissionEndpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubmissionEndpoint):
            return True

        return self.to_dict() != other.to_dict()
