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


class SoftwareComponent(object):
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
        'asset': 'Asset',
        'id': 'int',
        'load_order': 'int',
        'reboot_delay': 'int',
        'reboot_required': 'bool'
    }

    attribute_map = {
        'asset': 'asset',
        'id': 'id',
        'load_order': 'loadOrder',
        'reboot_delay': 'rebootDelay',
        'reboot_required': 'rebootRequired'
    }

    def __init__(self, asset=None, id=None, load_order=None, reboot_delay=None, reboot_required=None, local_vars_configuration=None):  # noqa: E501
        """SoftwareComponent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset = None
        self._id = None
        self._load_order = None
        self._reboot_delay = None
        self._reboot_required = None
        self.discriminator = None

        self.asset = asset
        if id is not None:
            self.id = id
        if load_order is not None:
            self.load_order = load_order
        if reboot_delay is not None:
            self.reboot_delay = reboot_delay
        if reboot_required is not None:
            self.reboot_required = reboot_required

    @property
    def asset(self):
        """Gets the asset of this SoftwareComponent.  # noqa: E501


        :return: The asset of this SoftwareComponent.  # noqa: E501
        :rtype: Asset
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this SoftwareComponent.


        :param asset: The asset of this SoftwareComponent.  # noqa: E501
        :type: Asset
        """
        if self.local_vars_configuration.client_side_validation and asset is None:  # noqa: E501
            raise ValueError("Invalid value for `asset`, must not be `None`")  # noqa: E501

        self._asset = asset

    @property
    def id(self):
        """Gets the id of this SoftwareComponent.  # noqa: E501


        :return: The id of this SoftwareComponent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SoftwareComponent.


        :param id: The id of this SoftwareComponent.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def load_order(self):
        """Gets the load_order of this SoftwareComponent.  # noqa: E501


        :return: The load_order of this SoftwareComponent.  # noqa: E501
        :rtype: int
        """
        return self._load_order

    @load_order.setter
    def load_order(self, load_order):
        """Sets the load_order of this SoftwareComponent.


        :param load_order: The load_order of this SoftwareComponent.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                load_order is not None and load_order < 0):  # noqa: E501
            raise ValueError("Invalid value for `load_order`, must be a value greater than or equal to `0`")  # noqa: E501

        self._load_order = load_order

    @property
    def reboot_delay(self):
        """Gets the reboot_delay of this SoftwareComponent.  # noqa: E501


        :return: The reboot_delay of this SoftwareComponent.  # noqa: E501
        :rtype: int
        """
        return self._reboot_delay

    @reboot_delay.setter
    def reboot_delay(self, reboot_delay):
        """Sets the reboot_delay of this SoftwareComponent.


        :param reboot_delay: The reboot_delay of this SoftwareComponent.  # noqa: E501
        :type: int
        """

        self._reboot_delay = reboot_delay

    @property
    def reboot_required(self):
        """Gets the reboot_required of this SoftwareComponent.  # noqa: E501


        :return: The reboot_required of this SoftwareComponent.  # noqa: E501
        :rtype: bool
        """
        return self._reboot_required

    @reboot_required.setter
    def reboot_required(self, reboot_required):
        """Sets the reboot_required of this SoftwareComponent.


        :param reboot_required: The reboot_required of this SoftwareComponent.  # noqa: E501
        :type: bool
        """

        self._reboot_required = reboot_required

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
        if not isinstance(other, SoftwareComponent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SoftwareComponent):
            return True

        return self.to_dict() != other.to_dict()
