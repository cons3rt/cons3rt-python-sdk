# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputTestBundle(object):
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
        'test_asset': 'InputTestAsset',
        'test_tool_pool_type': 'str'
    }

    attribute_map = {
        'test_asset': 'testAsset',
        'test_tool_pool_type': 'testToolPoolType'
    }

    def __init__(self, test_asset=None, test_tool_pool_type=None, local_vars_configuration=None):  # noqa: E501
        """InputTestBundle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._test_asset = None
        self._test_tool_pool_type = None
        self.discriminator = None

        if test_asset is not None:
            self.test_asset = test_asset
        self.test_tool_pool_type = test_tool_pool_type

    @property
    def test_asset(self):
        """Gets the test_asset of this InputTestBundle.  # noqa: E501


        :return: The test_asset of this InputTestBundle.  # noqa: E501
        :rtype: InputTestAsset
        """
        return self._test_asset

    @test_asset.setter
    def test_asset(self, test_asset):
        """Sets the test_asset of this InputTestBundle.


        :param test_asset: The test_asset of this InputTestBundle.  # noqa: E501
        :type: InputTestAsset
        """

        self._test_asset = test_asset

    @property
    def test_tool_pool_type(self):
        """Gets the test_tool_pool_type of this InputTestBundle.  # noqa: E501


        :return: The test_tool_pool_type of this InputTestBundle.  # noqa: E501
        :rtype: str
        """
        return self._test_tool_pool_type

    @test_tool_pool_type.setter
    def test_tool_pool_type(self, test_tool_pool_type):
        """Sets the test_tool_pool_type of this InputTestBundle.


        :param test_tool_pool_type: The test_tool_pool_type of this InputTestBundle.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and test_tool_pool_type is None:  # noqa: E501
            raise ValueError("Invalid value for `test_tool_pool_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DEPLOYMENT_RUN_ON_DEMAND"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and test_tool_pool_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `test_tool_pool_type` ({0}), must be one of {1}"  # noqa: E501
                .format(test_tool_pool_type, allowed_values)
            )

        self._test_tool_pool_type = test_tool_pool_type

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
        if not isinstance(other, InputTestBundle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputTestBundle):
            return True

        return self.to_dict() != other.to_dict()
