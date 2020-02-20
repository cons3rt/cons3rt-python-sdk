# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputProjectFull(object):
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
        'description': 'str',
        'itar_restricted': 'bool',
        'owning_team': 'InputTeam',
        'limits': 'ProjectLimits',
        'is_private': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'itar_restricted': 'itarRestricted',
        'owning_team': 'owningTeam',
        'limits': 'limits',
        'is_private': 'isPrivate'
    }

    def __init__(self, name=None, description=None, itar_restricted=None, owning_team=None, limits=None, is_private=None, local_vars_configuration=None):  # noqa: E501
        """InputProjectFull - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._itar_restricted = None
        self._owning_team = None
        self._limits = None
        self._is_private = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if itar_restricted is not None:
            self.itar_restricted = itar_restricted
        if owning_team is not None:
            self.owning_team = owning_team
        self.limits = limits
        if is_private is not None:
            self.is_private = is_private

    @property
    def name(self):
        """Gets the name of this InputProjectFull.  # noqa: E501


        :return: The name of this InputProjectFull.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputProjectFull.


        :param name: The name of this InputProjectFull.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this InputProjectFull.  # noqa: E501


        :return: The description of this InputProjectFull.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InputProjectFull.


        :param description: The description of this InputProjectFull.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def itar_restricted(self):
        """Gets the itar_restricted of this InputProjectFull.  # noqa: E501


        :return: The itar_restricted of this InputProjectFull.  # noqa: E501
        :rtype: bool
        """
        return self._itar_restricted

    @itar_restricted.setter
    def itar_restricted(self, itar_restricted):
        """Sets the itar_restricted of this InputProjectFull.


        :param itar_restricted: The itar_restricted of this InputProjectFull.  # noqa: E501
        :type: bool
        """

        self._itar_restricted = itar_restricted

    @property
    def owning_team(self):
        """Gets the owning_team of this InputProjectFull.  # noqa: E501


        :return: The owning_team of this InputProjectFull.  # noqa: E501
        :rtype: InputTeam
        """
        return self._owning_team

    @owning_team.setter
    def owning_team(self, owning_team):
        """Sets the owning_team of this InputProjectFull.


        :param owning_team: The owning_team of this InputProjectFull.  # noqa: E501
        :type: InputTeam
        """

        self._owning_team = owning_team

    @property
    def limits(self):
        """Gets the limits of this InputProjectFull.  # noqa: E501


        :return: The limits of this InputProjectFull.  # noqa: E501
        :rtype: ProjectLimits
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this InputProjectFull.


        :param limits: The limits of this InputProjectFull.  # noqa: E501
        :type: ProjectLimits
        """
        if self.local_vars_configuration.client_side_validation and limits is None:  # noqa: E501
            raise ValueError("Invalid value for `limits`, must not be `None`")  # noqa: E501

        self._limits = limits

    @property
    def is_private(self):
        """Gets the is_private of this InputProjectFull.  # noqa: E501


        :return: The is_private of this InputProjectFull.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this InputProjectFull.


        :param is_private: The is_private of this InputProjectFull.  # noqa: E501
        :type: bool
        """

        self._is_private = is_private

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
        if not isinstance(other, InputProjectFull):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputProjectFull):
            return True

        return self.to_dict() != other.to_dict()
