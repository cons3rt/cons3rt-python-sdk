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


class InputPartMediaType(object):
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
        'type': 'str',
        'subtype': 'str',
        'parameters': 'dict(str, str)',
        'wildcard_subtype': 'bool',
        'wildcard_type': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'subtype': 'subtype',
        'parameters': 'parameters',
        'wildcard_subtype': 'wildcardSubtype',
        'wildcard_type': 'wildcardType'
    }

    def __init__(self, type=None, subtype=None, parameters=None, wildcard_subtype=None, wildcard_type=None, local_vars_configuration=None):  # noqa: E501
        """InputPartMediaType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._subtype = None
        self._parameters = None
        self._wildcard_subtype = None
        self._wildcard_type = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if subtype is not None:
            self.subtype = subtype
        if parameters is not None:
            self.parameters = parameters
        if wildcard_subtype is not None:
            self.wildcard_subtype = wildcard_subtype
        if wildcard_type is not None:
            self.wildcard_type = wildcard_type

    @property
    def type(self):
        """Gets the type of this InputPartMediaType.  # noqa: E501


        :return: The type of this InputPartMediaType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InputPartMediaType.


        :param type: The type of this InputPartMediaType.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def subtype(self):
        """Gets the subtype of this InputPartMediaType.  # noqa: E501


        :return: The subtype of this InputPartMediaType.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this InputPartMediaType.


        :param subtype: The subtype of this InputPartMediaType.  # noqa: E501
        :type: str
        """

        self._subtype = subtype

    @property
    def parameters(self):
        """Gets the parameters of this InputPartMediaType.  # noqa: E501


        :return: The parameters of this InputPartMediaType.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this InputPartMediaType.


        :param parameters: The parameters of this InputPartMediaType.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    @property
    def wildcard_subtype(self):
        """Gets the wildcard_subtype of this InputPartMediaType.  # noqa: E501


        :return: The wildcard_subtype of this InputPartMediaType.  # noqa: E501
        :rtype: bool
        """
        return self._wildcard_subtype

    @wildcard_subtype.setter
    def wildcard_subtype(self, wildcard_subtype):
        """Sets the wildcard_subtype of this InputPartMediaType.


        :param wildcard_subtype: The wildcard_subtype of this InputPartMediaType.  # noqa: E501
        :type: bool
        """

        self._wildcard_subtype = wildcard_subtype

    @property
    def wildcard_type(self):
        """Gets the wildcard_type of this InputPartMediaType.  # noqa: E501


        :return: The wildcard_type of this InputPartMediaType.  # noqa: E501
        :rtype: bool
        """
        return self._wildcard_type

    @wildcard_type.setter
    def wildcard_type(self, wildcard_type):
        """Sets the wildcard_type of this InputPartMediaType.


        :param wildcard_type: The wildcard_type of this InputPartMediaType.  # noqa: E501
        :type: bool
        """

        self._wildcard_type = wildcard_type

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
        if not isinstance(other, InputPartMediaType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputPartMediaType):
            return True

        return self.to_dict() != other.to_dict()
