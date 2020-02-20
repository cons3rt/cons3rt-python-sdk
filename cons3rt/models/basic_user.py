# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class BasicUser(object):
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
        'username': 'str',
        'email': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'state': 'str'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'email': 'email',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'state': 'state'
    }

    def __init__(self, id=None, username=None, email=None, firstname=None, lastname=None, state=None, local_vars_configuration=None):  # noqa: E501
        """BasicUser - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._email = None
        self._firstname = None
        self._lastname = None
        self._state = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if state is not None:
            self.state = state

    @property
    def id(self):
        """Gets the id of this BasicUser.  # noqa: E501


        :return: The id of this BasicUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicUser.


        :param id: The id of this BasicUser.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this BasicUser.  # noqa: E501


        :return: The username of this BasicUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this BasicUser.


        :param username: The username of this BasicUser.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this BasicUser.  # noqa: E501


        :return: The email of this BasicUser.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BasicUser.


        :param email: The email of this BasicUser.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this BasicUser.  # noqa: E501


        :return: The firstname of this BasicUser.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this BasicUser.


        :param firstname: The firstname of this BasicUser.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this BasicUser.  # noqa: E501


        :return: The lastname of this BasicUser.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this BasicUser.


        :param lastname: The lastname of this BasicUser.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def state(self):
        """Gets the state of this BasicUser.  # noqa: E501


        :return: The state of this BasicUser.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BasicUser.


        :param state: The state of this BasicUser.  # noqa: E501
        :type: str
        """
        allowed_values = ["REQUESTED", "ACTIVE", "INACTIVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, BasicUser):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BasicUser):
            return True

        return self.to_dict() != other.to_dict()
