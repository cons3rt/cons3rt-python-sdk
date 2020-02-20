# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class RegisterTemplateObject(object):
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
        'client': 'VirtualizationRealmClient',
        'template_data': 'Cons3rtTemplateData'
    }

    attribute_map = {
        'client': 'client',
        'template_data': 'templateData'
    }

    def __init__(self, client=None, template_data=None, local_vars_configuration=None):  # noqa: E501
        """RegisterTemplateObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._client = None
        self._template_data = None
        self.discriminator = None

        if client is not None:
            self.client = client
        self.template_data = template_data

    @property
    def client(self):
        """Gets the client of this RegisterTemplateObject.  # noqa: E501


        :return: The client of this RegisterTemplateObject.  # noqa: E501
        :rtype: VirtualizationRealmClient
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this RegisterTemplateObject.


        :param client: The client of this RegisterTemplateObject.  # noqa: E501
        :type: VirtualizationRealmClient
        """

        self._client = client

    @property
    def template_data(self):
        """Gets the template_data of this RegisterTemplateObject.  # noqa: E501


        :return: The template_data of this RegisterTemplateObject.  # noqa: E501
        :rtype: Cons3rtTemplateData
        """
        return self._template_data

    @template_data.setter
    def template_data(self, template_data):
        """Sets the template_data of this RegisterTemplateObject.


        :param template_data: The template_data of this RegisterTemplateObject.  # noqa: E501
        :type: Cons3rtTemplateData
        """
        if self.local_vars_configuration.client_side_validation and template_data is None:  # noqa: E501
            raise ValueError("Invalid value for `template_data`, must not be `None`")  # noqa: E501

        self._template_data = template_data

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
        if not isinstance(other, RegisterTemplateObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RegisterTemplateObject):
            return True

        return self.to_dict() != other.to_dict()
