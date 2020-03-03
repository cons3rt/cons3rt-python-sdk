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


class InputPhysicalHostAllOf(object):
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
        'name': 'str',
        'physical_machine': 'InputPhysicalMachine',
        'components': 'list[InputAbstractComponent]'
    }

    attribute_map = {
        'name': 'name',
        'physical_machine': 'physicalMachine',
        'components': 'components'
    }

    def __init__(self, name=None, physical_machine=None, components=None, local_vars_configuration=None):  # noqa: E501
        """InputPhysicalHostAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._physical_machine = None
        self._components = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if physical_machine is not None:
            self.physical_machine = physical_machine
        if components is not None:
            self.components = components

    @property
    def name(self):
        """Gets the name of this InputPhysicalHostAllOf.  # noqa: E501


        :return: The name of this InputPhysicalHostAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputPhysicalHostAllOf.


        :param name: The name of this InputPhysicalHostAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def physical_machine(self):
        """Gets the physical_machine of this InputPhysicalHostAllOf.  # noqa: E501


        :return: The physical_machine of this InputPhysicalHostAllOf.  # noqa: E501
        :rtype: InputPhysicalMachine
        """
        return self._physical_machine

    @physical_machine.setter
    def physical_machine(self, physical_machine):
        """Sets the physical_machine of this InputPhysicalHostAllOf.


        :param physical_machine: The physical_machine of this InputPhysicalHostAllOf.  # noqa: E501
        :type: InputPhysicalMachine
        """

        self._physical_machine = physical_machine

    @property
    def components(self):
        """Gets the components of this InputPhysicalHostAllOf.  # noqa: E501


        :return: The components of this InputPhysicalHostAllOf.  # noqa: E501
        :rtype: list[InputAbstractComponent]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this InputPhysicalHostAllOf.


        :param components: The components of this InputPhysicalHostAllOf.  # noqa: E501
        :type: list[InputAbstractComponent]
        """

        self._components = components

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
        if not isinstance(other, InputPhysicalHostAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputPhysicalHostAllOf):
            return True

        return self.to_dict() != other.to_dict()
