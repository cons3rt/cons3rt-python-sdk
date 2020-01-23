# coding: utf-8

"""
    CONS3RT API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@cons3rt.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class PocInfo(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'email': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'organization': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'email': 'email',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'organization': 'organization',
        'phone': 'phone'
    }

    def __init__(self, email=None, firstname=None, lastname=None, organization=None, phone=None, local_vars_configuration=None):  # noqa: E501
        """PocInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email = None
        self._firstname = None
        self._lastname = None
        self._organization = None
        self._phone = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if firstname is not None:
            self.firstname = firstname
        if lastname is not None:
            self.lastname = lastname
        if organization is not None:
            self.organization = organization
        if phone is not None:
            self.phone = phone

    @property
    def email(self):
        """Gets the email of this PocInfo.  # noqa: E501


        :return: The email of this PocInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PocInfo.


        :param email: The email of this PocInfo.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """Gets the firstname of this PocInfo.  # noqa: E501


        :return: The firstname of this PocInfo.  # noqa: E501
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this PocInfo.


        :param firstname: The firstname of this PocInfo.  # noqa: E501
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """Gets the lastname of this PocInfo.  # noqa: E501


        :return: The lastname of this PocInfo.  # noqa: E501
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this PocInfo.


        :param lastname: The lastname of this PocInfo.  # noqa: E501
        :type: str
        """

        self._lastname = lastname

    @property
    def organization(self):
        """Gets the organization of this PocInfo.  # noqa: E501


        :return: The organization of this PocInfo.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this PocInfo.


        :param organization: The organization of this PocInfo.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def phone(self):
        """Gets the phone of this PocInfo.  # noqa: E501


        :return: The phone of this PocInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PocInfo.


        :param phone: The phone of this PocInfo.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if not isinstance(other, PocInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PocInfo):
            return True

        return self.to_dict() != other.to_dict()
