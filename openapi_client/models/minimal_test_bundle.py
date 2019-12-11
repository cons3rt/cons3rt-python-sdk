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


class MinimalTestBundle(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'offline': 'bool',
        'state': 'str',
        'visibility': 'str',
        'test_asset': 'MinimalTestAsset',
        'test_tool_pool_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'offline': 'offline',
        'state': 'state',
        'visibility': 'visibility',
        'test_asset': 'testAsset',
        'test_tool_pool_type': 'testToolPoolType'
    }

    def __init__(self, id=None, name=None, description=None, offline=None, state=None, visibility=None, test_asset=None, test_tool_pool_type=None, local_vars_configuration=None):  # noqa: E501
        """MinimalTestBundle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._offline = None
        self._state = None
        self._visibility = None
        self._test_asset = None
        self._test_tool_pool_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if offline is not None:
            self.offline = offline
        if state is not None:
            self.state = state
        if visibility is not None:
            self.visibility = visibility
        if test_asset is not None:
            self.test_asset = test_asset
        if test_tool_pool_type is not None:
            self.test_tool_pool_type = test_tool_pool_type

    @property
    def id(self):
        """Gets the id of this MinimalTestBundle.  # noqa: E501


        :return: The id of this MinimalTestBundle.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalTestBundle.


        :param id: The id of this MinimalTestBundle.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MinimalTestBundle.  # noqa: E501


        :return: The name of this MinimalTestBundle.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MinimalTestBundle.


        :param name: The name of this MinimalTestBundle.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this MinimalTestBundle.  # noqa: E501


        :return: The description of this MinimalTestBundle.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MinimalTestBundle.


        :param description: The description of this MinimalTestBundle.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def offline(self):
        """Gets the offline of this MinimalTestBundle.  # noqa: E501


        :return: The offline of this MinimalTestBundle.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this MinimalTestBundle.


        :param offline: The offline of this MinimalTestBundle.  # noqa: E501
        :type: bool
        """

        self._offline = offline

    @property
    def state(self):
        """Gets the state of this MinimalTestBundle.  # noqa: E501


        :return: The state of this MinimalTestBundle.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MinimalTestBundle.


        :param state: The state of this MinimalTestBundle.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_DEVELOPMENT", "CERTIFIED", "DEPRECATED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def visibility(self):
        """Gets the visibility of this MinimalTestBundle.  # noqa: E501


        :return: The visibility of this MinimalTestBundle.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this MinimalTestBundle.


        :param visibility: The visibility of this MinimalTestBundle.  # noqa: E501
        :type: str
        """
        allowed_values = ["OWNER", "OWNING_PROJECT", "TRUSTED_PROJECTS", "COMMUNITY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and visibility not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def test_asset(self):
        """Gets the test_asset of this MinimalTestBundle.  # noqa: E501


        :return: The test_asset of this MinimalTestBundle.  # noqa: E501
        :rtype: MinimalTestAsset
        """
        return self._test_asset

    @test_asset.setter
    def test_asset(self, test_asset):
        """Sets the test_asset of this MinimalTestBundle.


        :param test_asset: The test_asset of this MinimalTestBundle.  # noqa: E501
        :type: MinimalTestAsset
        """

        self._test_asset = test_asset

    @property
    def test_tool_pool_type(self):
        """Gets the test_tool_pool_type of this MinimalTestBundle.  # noqa: E501


        :return: The test_tool_pool_type of this MinimalTestBundle.  # noqa: E501
        :rtype: str
        """
        return self._test_tool_pool_type

    @test_tool_pool_type.setter
    def test_tool_pool_type(self, test_tool_pool_type):
        """Sets the test_tool_pool_type of this MinimalTestBundle.


        :param test_tool_pool_type: The test_tool_pool_type of this MinimalTestBundle.  # noqa: E501
        :type: str
        """
        allowed_values = ["COMMUNITY_POOL", "PROJECT_POOL", "DEPLOYMENT_RUN_ON_DEMAND"]  # noqa: E501
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
        if not isinstance(other, MinimalTestBundle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalTestBundle):
            return True

        return self.to_dict() != other.to_dict()
