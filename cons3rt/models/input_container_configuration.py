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


class InputContainerConfiguration(object):
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
        'port_mapping': 'ContainerPortMapping',
        'container_name': 'str',
        'run_arguments': 'str',
        'environment_map': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'port_mapping': 'portMapping',
        'container_name': 'containerName',
        'run_arguments': 'runArguments',
        'environment_map': 'environmentMap'
    }

    def __init__(self, id=None, port_mapping=None, container_name=None, run_arguments=None, environment_map=None, local_vars_configuration=None):  # noqa: E501
        """InputContainerConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._port_mapping = None
        self._container_name = None
        self._run_arguments = None
        self._environment_map = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if port_mapping is not None:
            self.port_mapping = port_mapping
        self.container_name = container_name
        if run_arguments is not None:
            self.run_arguments = run_arguments
        if environment_map is not None:
            self.environment_map = environment_map

    @property
    def id(self):
        """Gets the id of this InputContainerConfiguration.  # noqa: E501


        :return: The id of this InputContainerConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InputContainerConfiguration.


        :param id: The id of this InputContainerConfiguration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def port_mapping(self):
        """Gets the port_mapping of this InputContainerConfiguration.  # noqa: E501


        :return: The port_mapping of this InputContainerConfiguration.  # noqa: E501
        :rtype: ContainerPortMapping
        """
        return self._port_mapping

    @port_mapping.setter
    def port_mapping(self, port_mapping):
        """Sets the port_mapping of this InputContainerConfiguration.


        :param port_mapping: The port_mapping of this InputContainerConfiguration.  # noqa: E501
        :type: ContainerPortMapping
        """

        self._port_mapping = port_mapping

    @property
    def container_name(self):
        """Gets the container_name of this InputContainerConfiguration.  # noqa: E501


        :return: The container_name of this InputContainerConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this InputContainerConfiguration.


        :param container_name: The container_name of this InputContainerConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and container_name is None:  # noqa: E501
            raise ValueError("Invalid value for `container_name`, must not be `None`")  # noqa: E501

        self._container_name = container_name

    @property
    def run_arguments(self):
        """Gets the run_arguments of this InputContainerConfiguration.  # noqa: E501


        :return: The run_arguments of this InputContainerConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._run_arguments

    @run_arguments.setter
    def run_arguments(self, run_arguments):
        """Sets the run_arguments of this InputContainerConfiguration.


        :param run_arguments: The run_arguments of this InputContainerConfiguration.  # noqa: E501
        :type: str
        """

        self._run_arguments = run_arguments

    @property
    def environment_map(self):
        """Gets the environment_map of this InputContainerConfiguration.  # noqa: E501


        :return: The environment_map of this InputContainerConfiguration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._environment_map

    @environment_map.setter
    def environment_map(self, environment_map):
        """Sets the environment_map of this InputContainerConfiguration.


        :param environment_map: The environment_map of this InputContainerConfiguration.  # noqa: E501
        :type: dict(str, str)
        """

        self._environment_map = environment_map

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
        if not isinstance(other, InputContainerConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputContainerConfiguration):
            return True

        return self.to_dict() != other.to_dict()
