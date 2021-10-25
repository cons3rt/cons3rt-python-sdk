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


class RemoteAccessConfig(object):
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
        'remote_access_ip_address': 'str',
        'remote_access_port': 'int',
        'instance_type': 'str',
        'template_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'remote_access_ip_address': 'remoteAccessIpAddress',
        'remote_access_port': 'remoteAccessPort',
        'instance_type': 'instanceType',
        'template_name': 'templateName'
    }

    def __init__(self, id=None, remote_access_ip_address=None, remote_access_port=None, instance_type=None, template_name=None, local_vars_configuration=None):  # noqa: E501
        """RemoteAccessConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._remote_access_ip_address = None
        self._remote_access_port = None
        self._instance_type = None
        self._template_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.remote_access_ip_address = remote_access_ip_address
        self.remote_access_port = remote_access_port
        self.instance_type = instance_type
        if template_name is not None:
            self.template_name = template_name

    @property
    def id(self):
        """Gets the id of this RemoteAccessConfig.  # noqa: E501


        :return: The id of this RemoteAccessConfig.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RemoteAccessConfig.


        :param id: The id of this RemoteAccessConfig.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def remote_access_ip_address(self):
        """Gets the remote_access_ip_address of this RemoteAccessConfig.  # noqa: E501


        :return: The remote_access_ip_address of this RemoteAccessConfig.  # noqa: E501
        :rtype: str
        """
        return self._remote_access_ip_address

    @remote_access_ip_address.setter
    def remote_access_ip_address(self, remote_access_ip_address):
        """Sets the remote_access_ip_address of this RemoteAccessConfig.


        :param remote_access_ip_address: The remote_access_ip_address of this RemoteAccessConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and remote_access_ip_address is None:  # noqa: E501
            raise ValueError("Invalid value for `remote_access_ip_address`, must not be `None`")  # noqa: E501

        self._remote_access_ip_address = remote_access_ip_address

    @property
    def remote_access_port(self):
        """Gets the remote_access_port of this RemoteAccessConfig.  # noqa: E501


        :return: The remote_access_port of this RemoteAccessConfig.  # noqa: E501
        :rtype: int
        """
        return self._remote_access_port

    @remote_access_port.setter
    def remote_access_port(self, remote_access_port):
        """Sets the remote_access_port of this RemoteAccessConfig.


        :param remote_access_port: The remote_access_port of this RemoteAccessConfig.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and remote_access_port is None:  # noqa: E501
            raise ValueError("Invalid value for `remote_access_port`, must not be `None`")  # noqa: E501

        self._remote_access_port = remote_access_port

    @property
    def instance_type(self):
        """Gets the instance_type of this RemoteAccessConfig.  # noqa: E501


        :return: The instance_type of this RemoteAccessConfig.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this RemoteAccessConfig.


        :param instance_type: The instance_type of this RemoteAccessConfig.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instance_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_type`, must not be `None`")  # noqa: E501
        allowed_values = ["LARGE", "MEDIUM", "SMALL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instance_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instance_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instance_type, allowed_values)
            )

        self._instance_type = instance_type

    @property
    def template_name(self):
        """Gets the template_name of this RemoteAccessConfig.  # noqa: E501


        :return: The template_name of this RemoteAccessConfig.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this RemoteAccessConfig.


        :param template_name: The template_name of this RemoteAccessConfig.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

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
        if not isinstance(other, RemoteAccessConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteAccessConfig):
            return True

        return self.to_dict() != other.to_dict()
