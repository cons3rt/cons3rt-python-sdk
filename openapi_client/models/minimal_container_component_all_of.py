# coding: utf-8

"""
    CONS3RT Web API

    A CONS3RT ReSTful API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class MinimalContainerComponentAllOf(object):
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
        'configuration': 'MinimalContainerConfiguration'
    }

    attribute_map = {
        'configuration': 'configuration'
    }

    def __init__(self, configuration=None, local_vars_configuration=None):  # noqa: E501
        """MinimalContainerComponentAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._configuration = None
        self.discriminator = None

        if configuration is not None:
            self.configuration = configuration

    @property
    def configuration(self):
        """Gets the configuration of this MinimalContainerComponentAllOf.  # noqa: E501


        :return: The configuration of this MinimalContainerComponentAllOf.  # noqa: E501
        :rtype: MinimalContainerConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this MinimalContainerComponentAllOf.


        :param configuration: The configuration of this MinimalContainerComponentAllOf.  # noqa: E501
        :type: MinimalContainerConfiguration
        """

        self._configuration = configuration

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
        if not isinstance(other, MinimalContainerComponentAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalContainerComponentAllOf):
            return True

        return self.to_dict() != other.to_dict()
