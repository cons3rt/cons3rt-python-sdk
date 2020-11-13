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


class ContainerConfiguration(object):
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
        'container_name': 'str',
        'container_runtime': 'str',
        'environment_map': 'dict(str, str)',
        'mounts': 'list[ContainerMount]',
        'port_mappings': 'list[ContainerPortMapping]',
        'run_arguments': 'str',
        'run_disabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'container_name': 'containerName',
        'container_runtime': 'containerRuntime',
        'environment_map': 'environmentMap',
        'mounts': 'mounts',
        'port_mappings': 'portMappings',
        'run_arguments': 'runArguments',
        'run_disabled': 'runDisabled'
    }

    def __init__(self, id=None, container_name=None, container_runtime=None, environment_map=None, mounts=None, port_mappings=None, run_arguments=None, run_disabled=None, local_vars_configuration=None):  # noqa: E501
        """ContainerConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._container_name = None
        self._container_runtime = None
        self._environment_map = None
        self._mounts = None
        self._port_mappings = None
        self._run_arguments = None
        self._run_disabled = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.container_name = container_name
        if container_runtime is not None:
            self.container_runtime = container_runtime
        if environment_map is not None:
            self.environment_map = environment_map
        if mounts is not None:
            self.mounts = mounts
        if port_mappings is not None:
            self.port_mappings = port_mappings
        if run_arguments is not None:
            self.run_arguments = run_arguments
        if run_disabled is not None:
            self.run_disabled = run_disabled

    @property
    def id(self):
        """Gets the id of this ContainerConfiguration.  # noqa: E501


        :return: The id of this ContainerConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContainerConfiguration.


        :param id: The id of this ContainerConfiguration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def container_name(self):
        """Gets the container_name of this ContainerConfiguration.  # noqa: E501


        :return: The container_name of this ContainerConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this ContainerConfiguration.


        :param container_name: The container_name of this ContainerConfiguration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and container_name is None:  # noqa: E501
            raise ValueError("Invalid value for `container_name`, must not be `None`")  # noqa: E501

        self._container_name = container_name

    @property
    def container_runtime(self):
        """Gets the container_runtime of this ContainerConfiguration.  # noqa: E501


        :return: The container_runtime of this ContainerConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._container_runtime

    @container_runtime.setter
    def container_runtime(self, container_runtime):
        """Sets the container_runtime of this ContainerConfiguration.


        :param container_runtime: The container_runtime of this ContainerConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOCKER", "PODMAN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and container_runtime not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `container_runtime` ({0}), must be one of {1}"  # noqa: E501
                .format(container_runtime, allowed_values)
            )

        self._container_runtime = container_runtime

    @property
    def environment_map(self):
        """Gets the environment_map of this ContainerConfiguration.  # noqa: E501


        :return: The environment_map of this ContainerConfiguration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._environment_map

    @environment_map.setter
    def environment_map(self, environment_map):
        """Sets the environment_map of this ContainerConfiguration.


        :param environment_map: The environment_map of this ContainerConfiguration.  # noqa: E501
        :type: dict(str, str)
        """

        self._environment_map = environment_map

    @property
    def mounts(self):
        """Gets the mounts of this ContainerConfiguration.  # noqa: E501


        :return: The mounts of this ContainerConfiguration.  # noqa: E501
        :rtype: list[ContainerMount]
        """
        return self._mounts

    @mounts.setter
    def mounts(self, mounts):
        """Sets the mounts of this ContainerConfiguration.


        :param mounts: The mounts of this ContainerConfiguration.  # noqa: E501
        :type: list[ContainerMount]
        """

        self._mounts = mounts

    @property
    def port_mappings(self):
        """Gets the port_mappings of this ContainerConfiguration.  # noqa: E501


        :return: The port_mappings of this ContainerConfiguration.  # noqa: E501
        :rtype: list[ContainerPortMapping]
        """
        return self._port_mappings

    @port_mappings.setter
    def port_mappings(self, port_mappings):
        """Sets the port_mappings of this ContainerConfiguration.


        :param port_mappings: The port_mappings of this ContainerConfiguration.  # noqa: E501
        :type: list[ContainerPortMapping]
        """

        self._port_mappings = port_mappings

    @property
    def run_arguments(self):
        """Gets the run_arguments of this ContainerConfiguration.  # noqa: E501


        :return: The run_arguments of this ContainerConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._run_arguments

    @run_arguments.setter
    def run_arguments(self, run_arguments):
        """Sets the run_arguments of this ContainerConfiguration.


        :param run_arguments: The run_arguments of this ContainerConfiguration.  # noqa: E501
        :type: str
        """

        self._run_arguments = run_arguments

    @property
    def run_disabled(self):
        """Gets the run_disabled of this ContainerConfiguration.  # noqa: E501


        :return: The run_disabled of this ContainerConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._run_disabled

    @run_disabled.setter
    def run_disabled(self, run_disabled):
        """Sets the run_disabled of this ContainerConfiguration.


        :param run_disabled: The run_disabled of this ContainerConfiguration.  # noqa: E501
        :type: bool
        """

        self._run_disabled = run_disabled

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
        if not isinstance(other, ContainerConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerConfiguration):
            return True

        return self.to_dict() != other.to_dict()
