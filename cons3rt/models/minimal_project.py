# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class MinimalProject(object):
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
        'name': 'str',
        'itar_restricted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'itar_restricted': 'itarRestricted'
    }

    def __init__(self, id=None, name=None, itar_restricted=None, local_vars_configuration=None):  # noqa: E501
        """MinimalProject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._itar_restricted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if itar_restricted is not None:
            self.itar_restricted = itar_restricted

    @property
    def id(self):
        """Gets the id of this MinimalProject.  # noqa: E501


        :return: The id of this MinimalProject.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalProject.


        :param id: The id of this MinimalProject.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MinimalProject.  # noqa: E501


        :return: The name of this MinimalProject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MinimalProject.


        :param name: The name of this MinimalProject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def itar_restricted(self):
        """Gets the itar_restricted of this MinimalProject.  # noqa: E501


        :return: The itar_restricted of this MinimalProject.  # noqa: E501
        :rtype: bool
        """
        return self._itar_restricted

    @itar_restricted.setter
    def itar_restricted(self, itar_restricted):
        """Sets the itar_restricted of this MinimalProject.


        :param itar_restricted: The itar_restricted of this MinimalProject.  # noqa: E501
        :type: bool
        """

        self._itar_restricted = itar_restricted

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
        if not isinstance(other, MinimalProject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalProject):
            return True

        return self.to_dict() != other.to_dict()
