# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputVirtualHost(object):
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
        'components': 'list[InputAbstractComponent]',
        'name': 'str',
        'template_profile': 'InputTemplateProfile'
    }

    attribute_map = {
        'components': 'components',
        'name': 'name',
        'template_profile': 'templateProfile'
    }

    def __init__(self, components=None, name=None, template_profile=None, local_vars_configuration=None):  # noqa: E501
        """InputVirtualHost - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._components = None
        self._name = None
        self._template_profile = None
        self.discriminator = None

        if components is not None:
            self.components = components
        if name is not None:
            self.name = name
        if template_profile is not None:
            self.template_profile = template_profile

    @property
    def components(self):
        """Gets the components of this InputVirtualHost.  # noqa: E501


        :return: The components of this InputVirtualHost.  # noqa: E501
        :rtype: list[InputAbstractComponent]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this InputVirtualHost.


        :param components: The components of this InputVirtualHost.  # noqa: E501
        :type: list[InputAbstractComponent]
        """

        self._components = components

    @property
    def name(self):
        """Gets the name of this InputVirtualHost.  # noqa: E501


        :return: The name of this InputVirtualHost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputVirtualHost.


        :param name: The name of this InputVirtualHost.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def template_profile(self):
        """Gets the template_profile of this InputVirtualHost.  # noqa: E501


        :return: The template_profile of this InputVirtualHost.  # noqa: E501
        :rtype: InputTemplateProfile
        """
        return self._template_profile

    @template_profile.setter
    def template_profile(self, template_profile):
        """Sets the template_profile of this InputVirtualHost.


        :param template_profile: The template_profile of this InputVirtualHost.  # noqa: E501
        :type: InputTemplateProfile
        """

        self._template_profile = template_profile

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
        if not isinstance(other, InputVirtualHost):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputVirtualHost):
            return True

        return self.to_dict() != other.to_dict()
