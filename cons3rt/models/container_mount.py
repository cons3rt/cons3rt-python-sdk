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


class ContainerMount(object):
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
        'type': 'str',
        'source': 'str',
        'target': 'str',
        'options': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'source': 'source',
        'target': 'target',
        'options': 'options'
    }

    def __init__(self, id=None, type=None, source=None, target=None, options=None, local_vars_configuration=None):  # noqa: E501
        """ContainerMount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._source = None
        self._target = None
        self._options = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.type = type
        self.source = source
        self.target = target
        if options is not None:
            self.options = options

    @property
    def id(self):
        """Gets the id of this ContainerMount.  # noqa: E501


        :return: The id of this ContainerMount.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContainerMount.


        :param id: The id of this ContainerMount.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ContainerMount.  # noqa: E501


        :return: The type of this ContainerMount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ContainerMount.


        :param type: The type of this ContainerMount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["BIND_MOUNT", "TMPFS_MOUNT", "VOLUME_MOUNT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def source(self):
        """Gets the source of this ContainerMount.  # noqa: E501


        :return: The source of this ContainerMount.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ContainerMount.


        :param source: The source of this ContainerMount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source is None:  # noqa: E501
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def target(self):
        """Gets the target of this ContainerMount.  # noqa: E501


        :return: The target of this ContainerMount.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ContainerMount.


        :param target: The target of this ContainerMount.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target is None:  # noqa: E501
            raise ValueError("Invalid value for `target`, must not be `None`")  # noqa: E501

        self._target = target

    @property
    def options(self):
        """Gets the options of this ContainerMount.  # noqa: E501


        :return: The options of this ContainerMount.  # noqa: E501
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ContainerMount.


        :param options: The options of this ContainerMount.  # noqa: E501
        :type: str
        """

        self._options = options

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
        if not isinstance(other, ContainerMount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerMount):
            return True

        return self.to_dict() != other.to_dict()
