# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputUnregisterTemplateObject(object):
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
        'remove_subscriptions': 'bool',
        'client': 'InputVirtualizationRealmClient'
    }

    attribute_map = {
        'remove_subscriptions': 'removeSubscriptions',
        'client': 'client'
    }

    def __init__(self, remove_subscriptions=None, client=None, local_vars_configuration=None):  # noqa: E501
        """InputUnregisterTemplateObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._remove_subscriptions = None
        self._client = None
        self.discriminator = None

        self.remove_subscriptions = remove_subscriptions
        if client is not None:
            self.client = client

    @property
    def remove_subscriptions(self):
        """Gets the remove_subscriptions of this InputUnregisterTemplateObject.  # noqa: E501


        :return: The remove_subscriptions of this InputUnregisterTemplateObject.  # noqa: E501
        :rtype: bool
        """
        return self._remove_subscriptions

    @remove_subscriptions.setter
    def remove_subscriptions(self, remove_subscriptions):
        """Sets the remove_subscriptions of this InputUnregisterTemplateObject.


        :param remove_subscriptions: The remove_subscriptions of this InputUnregisterTemplateObject.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and remove_subscriptions is None:  # noqa: E501
            raise ValueError("Invalid value for `remove_subscriptions`, must not be `None`")  # noqa: E501

        self._remove_subscriptions = remove_subscriptions

    @property
    def client(self):
        """Gets the client of this InputUnregisterTemplateObject.  # noqa: E501


        :return: The client of this InputUnregisterTemplateObject.  # noqa: E501
        :rtype: InputVirtualizationRealmClient
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this InputUnregisterTemplateObject.


        :param client: The client of this InputUnregisterTemplateObject.  # noqa: E501
        :type: InputVirtualizationRealmClient
        """

        self._client = client

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
        if not isinstance(other, InputUnregisterTemplateObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputUnregisterTemplateObject):
            return True

        return self.to_dict() != other.to_dict()
