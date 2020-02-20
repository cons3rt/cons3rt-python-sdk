# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputCategory(object):
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
        'disruptive': 'bool',
        'hidden': 'bool',
        'id': 'int',
        'name': 'str',
        'parent': 'InputParentCategory'
    }

    attribute_map = {
        'disruptive': 'disruptive',
        'hidden': 'hidden',
        'id': 'id',
        'name': 'name',
        'parent': 'parent'
    }

    def __init__(self, disruptive=None, hidden=None, id=None, name=None, parent=None, local_vars_configuration=None):  # noqa: E501
        """InputCategory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._disruptive = None
        self._hidden = None
        self._id = None
        self._name = None
        self._parent = None
        self.discriminator = None

        if disruptive is not None:
            self.disruptive = disruptive
        if hidden is not None:
            self.hidden = hidden
        if id is not None:
            self.id = id
        self.name = name
        if parent is not None:
            self.parent = parent

    @property
    def disruptive(self):
        """Gets the disruptive of this InputCategory.  # noqa: E501


        :return: The disruptive of this InputCategory.  # noqa: E501
        :rtype: bool
        """
        return self._disruptive

    @disruptive.setter
    def disruptive(self, disruptive):
        """Sets the disruptive of this InputCategory.


        :param disruptive: The disruptive of this InputCategory.  # noqa: E501
        :type: bool
        """

        self._disruptive = disruptive

    @property
    def hidden(self):
        """Gets the hidden of this InputCategory.  # noqa: E501


        :return: The hidden of this InputCategory.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this InputCategory.


        :param hidden: The hidden of this InputCategory.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def id(self):
        """Gets the id of this InputCategory.  # noqa: E501


        :return: The id of this InputCategory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InputCategory.


        :param id: The id of this InputCategory.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InputCategory.  # noqa: E501


        :return: The name of this InputCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputCategory.


        :param name: The name of this InputCategory.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent(self):
        """Gets the parent of this InputCategory.  # noqa: E501


        :return: The parent of this InputCategory.  # noqa: E501
        :rtype: InputParentCategory
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this InputCategory.


        :param parent: The parent of this InputCategory.  # noqa: E501
        :type: InputParentCategory
        """

        self._parent = parent

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
        if not isinstance(other, InputCategory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputCategory):
            return True

        return self.to_dict() != other.to_dict()
