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


class InputVCloudRestCloudAllOf(object):
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
        'password': 'str',
        'port': 'int',
        'protocol': 'str',
        'remote_access_internal_ip': 'str',
        'remote_access_port': 'int',
        'username': 'str',
        'gpu_profile_types': 'list[str]',
        'vsphere_api_version': 'str',
        'vsphere_host': 'str',
        'vsphere_port': 'int'
    }

    attribute_map = {
        'hostname': 'hostname',
        'password': 'password',
        'port': 'port',
        'protocol': 'protocol',
        'remote_access_internal_ip': 'remoteAccessInternalIp',
        'remote_access_port': 'remoteAccessPort',
        'username': 'username',
        'gpu_profile_types': 'gpuProfileTypes',
        'vsphere_api_version': 'vsphereApiVersion',
        'vsphere_host': 'vsphereHost',
        'vsphere_port': 'vspherePort'
    }

    def __init__(self, hostname=None, password=None, port=None, protocol=None, remote_access_internal_ip=None, remote_access_port=None, username=None, gpu_profile_types=None, vsphere_api_version=None, vsphere_host=None, vsphere_port=None, local_vars_configuration=None):  # noqa: E501
        """InputVCloudRestCloudAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hostname = None
        self._password = None
        self._port = None
        self._protocol = None
        self._remote_access_internal_ip = None
        self._remote_access_port = None
        self._username = None
        self._gpu_profile_types = None
        self._vsphere_api_version = None
        self._vsphere_host = None
        self._vsphere_port = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if password is not None:
            self.password = password
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
        if gpu_profile_types is not None:
            self.gpu_profile_types = gpu_profile_types
        if vsphere_api_version is not None:
            self.vsphere_api_version = vsphere_api_version
        if vsphere_host is not None:
            self.vsphere_host = vsphere_host
        if vsphere_port is not None:
            self.vsphere_port = vsphere_port

    @property
    def hostname(self):
        """Gets the hostname of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The hostname of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this InputVCloudRestCloudAllOf.


        :param hostname: The hostname of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def password(self):
        """Gets the password of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The password of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InputVCloudRestCloudAllOf.


        :param password: The password of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """Gets the port of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The port of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InputVCloudRestCloudAllOf.


        :param port: The port of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The protocol of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this InputVCloudRestCloudAllOf.


        :param protocol: The protocol of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def remote_access_internal_ip(self):
        """Gets the remote_access_internal_ip of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The remote_access_internal_ip of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._remote_access_internal_ip

    @remote_access_internal_ip.setter
    def remote_access_internal_ip(self, remote_access_internal_ip):
        """Sets the remote_access_internal_ip of this InputVCloudRestCloudAllOf.


        :param remote_access_internal_ip: The remote_access_internal_ip of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: str
        """

        self._remote_access_internal_ip = remote_access_internal_ip

    @property
    def remote_access_port(self):
        """Gets the remote_access_port of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The remote_access_port of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: int
        """
        return self._remote_access_port

    @remote_access_port.setter
    def remote_access_port(self, remote_access_port):
        """Sets the remote_access_port of this InputVCloudRestCloudAllOf.


        :param remote_access_port: The remote_access_port of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: int
        """

        self._remote_access_port = remote_access_port

    @property
    def username(self):
        """Gets the username of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The username of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InputVCloudRestCloudAllOf.


        :param username: The username of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def gpu_profile_types(self):
        """Gets the gpu_profile_types of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The gpu_profile_types of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._gpu_profile_types

    @gpu_profile_types.setter
    def gpu_profile_types(self, gpu_profile_types):
        """Sets the gpu_profile_types of this InputVCloudRestCloudAllOf.


        :param gpu_profile_types: The gpu_profile_types of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["M10_0Q", "M10_1Q", "M10_2Q", "M10_4Q", "V100D_2Q", "V100D_4Q"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(gpu_profile_types).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `gpu_profile_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(gpu_profile_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._gpu_profile_types = gpu_profile_types

    @property
    def vsphere_api_version(self):
        """Gets the vsphere_api_version of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The vsphere_api_version of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._vsphere_api_version

    @vsphere_api_version.setter
    def vsphere_api_version(self, vsphere_api_version):
        """Sets the vsphere_api_version of this InputVCloudRestCloudAllOf.


        :param vsphere_api_version: The vsphere_api_version of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                vsphere_api_version is not None and len(vsphere_api_version) > 6):
            raise ValueError("Invalid value for `vsphere_api_version`, length must be less than or equal to `6`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                vsphere_api_version is not None and len(vsphere_api_version) < 1):
            raise ValueError("Invalid value for `vsphere_api_version`, length must be greater than or equal to `1`")  # noqa: E501

        self._vsphere_api_version = vsphere_api_version

    @property
    def vsphere_host(self):
        """Gets the vsphere_host of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The vsphere_host of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._vsphere_host

    @vsphere_host.setter
    def vsphere_host(self, vsphere_host):
        """Sets the vsphere_host of this InputVCloudRestCloudAllOf.


        :param vsphere_host: The vsphere_host of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: str
        """

        self._vsphere_host = vsphere_host

    @property
    def vsphere_port(self):
        """Gets the vsphere_port of this InputVCloudRestCloudAllOf.  # noqa: E501


        :return: The vsphere_port of this InputVCloudRestCloudAllOf.  # noqa: E501
        :rtype: int
        """
        return self._vsphere_port

    @vsphere_port.setter
    def vsphere_port(self, vsphere_port):
        """Sets the vsphere_port of this InputVCloudRestCloudAllOf.


        :param vsphere_port: The vsphere_port of this InputVCloudRestCloudAllOf.  # noqa: E501
        :type: int
        """

        self._vsphere_port = vsphere_port

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
        if not isinstance(other, InputVCloudRestCloudAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputVCloudRestCloudAllOf):
            return True

        return self.to_dict() != other.to_dict()
