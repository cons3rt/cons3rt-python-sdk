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


class FullVCloudCloud(object):
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
        'hostname': 'str',
        'port': 'int',
        'protocol': 'str',
        'remote_access_internal_ip': 'str',
        'remote_access_port': 'int',
        'username': 'str'
    }

    attribute_map = {
        'hostname': 'hostname',
        'port': 'port',
        'protocol': 'protocol',
        'remote_access_internal_ip': 'remoteAccessInternalIp',
        'remote_access_port': 'remoteAccessPort',
        'username': 'username'
    }

    def __init__(self, hostname=None, port=None, protocol=None, remote_access_internal_ip=None, remote_access_port=None, username=None, local_vars_configuration=None):  # noqa: E501
        """FullVCloudCloud - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hostname = None
        self._port = None
        self._protocol = None
        self._remote_access_internal_ip = None
        self._remote_access_port = None
        self._username = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if remote_access_internal_ip is not None:
            self.remote_access_internal_ip = remote_access_internal_ip
        if remote_access_port is not None:
            self.remote_access_port = remote_access_port
        if username is not None:
            self.username = username

    @property
    def hostname(self):
        """Gets the hostname of this FullVCloudCloud.  # noqa: E501


        :return: The hostname of this FullVCloudCloud.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this FullVCloudCloud.


        :param hostname: The hostname of this FullVCloudCloud.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this FullVCloudCloud.  # noqa: E501


        :return: The port of this FullVCloudCloud.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this FullVCloudCloud.


        :param port: The port of this FullVCloudCloud.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this FullVCloudCloud.  # noqa: E501


        :return: The protocol of this FullVCloudCloud.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FullVCloudCloud.


        :param protocol: The protocol of this FullVCloudCloud.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def remote_access_internal_ip(self):
        """Gets the remote_access_internal_ip of this FullVCloudCloud.  # noqa: E501


        :return: The remote_access_internal_ip of this FullVCloudCloud.  # noqa: E501
        :rtype: str
        """
        return self._remote_access_internal_ip

    @remote_access_internal_ip.setter
    def remote_access_internal_ip(self, remote_access_internal_ip):
        """Sets the remote_access_internal_ip of this FullVCloudCloud.


        :param remote_access_internal_ip: The remote_access_internal_ip of this FullVCloudCloud.  # noqa: E501
        :type: str
        """

        self._remote_access_internal_ip = remote_access_internal_ip

    @property
    def remote_access_port(self):
        """Gets the remote_access_port of this FullVCloudCloud.  # noqa: E501


        :return: The remote_access_port of this FullVCloudCloud.  # noqa: E501
        :rtype: int
        """
        return self._remote_access_port

    @remote_access_port.setter
    def remote_access_port(self, remote_access_port):
        """Sets the remote_access_port of this FullVCloudCloud.


        :param remote_access_port: The remote_access_port of this FullVCloudCloud.  # noqa: E501
        :type: int
        """

        self._remote_access_port = remote_access_port

    @property
    def username(self):
        """Gets the username of this FullVCloudCloud.  # noqa: E501


        :return: The username of this FullVCloudCloud.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this FullVCloudCloud.


        :param username: The username of this FullVCloudCloud.  # noqa: E501
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
        if not isinstance(other, FullVCloudCloud):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullVCloudCloud):
            return True

        return self.to_dict() != other.to_dict()
