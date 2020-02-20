# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class AwsRegisterCloudSpaceRequest(object):
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
        'account_id': 'str',
        'region': 'str',
        'vpc_id': 'str',
        'user_key_name': 'str',
        'network_security_group_map': 'dict(str, str)'
    }

    attribute_map = {
        'account_id': 'accountId',
        'region': 'region',
        'vpc_id': 'vpcId',
        'user_key_name': 'userKeyName',
        'network_security_group_map': 'networkSecurityGroupMap'
    }

    def __init__(self, account_id=None, region=None, vpc_id=None, user_key_name=None, network_security_group_map=None, local_vars_configuration=None):  # noqa: E501
        """AwsRegisterCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._account_id = None
        self._region = None
        self._vpc_id = None
        self._user_key_name = None
        self._network_security_group_map = None
        self.discriminator = None

        self.account_id = account_id
        self.region = region
        self.vpc_id = vpc_id
        if user_key_name is not None:
            self.user_key_name = user_key_name
        self.network_security_group_map = network_security_group_map

    @property
    def account_id(self):
        """Gets the account_id of this AwsRegisterCloudSpaceRequest.  # noqa: E501


        :return: The account_id of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AwsRegisterCloudSpaceRequest.


        :param account_id: The account_id of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def region(self):
        """Gets the region of this AwsRegisterCloudSpaceRequest.  # noqa: E501


        :return: The region of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AwsRegisterCloudSpaceRequest.


        :param region: The region of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def vpc_id(self):
        """Gets the vpc_id of this AwsRegisterCloudSpaceRequest.  # noqa: E501


        :return: The vpc_id of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this AwsRegisterCloudSpaceRequest.


        :param vpc_id: The vpc_id of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and vpc_id is None:  # noqa: E501
            raise ValueError("Invalid value for `vpc_id`, must not be `None`")  # noqa: E501

        self._vpc_id = vpc_id

    @property
    def user_key_name(self):
        """Gets the user_key_name of this AwsRegisterCloudSpaceRequest.  # noqa: E501


        :return: The user_key_name of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_key_name

    @user_key_name.setter
    def user_key_name(self, user_key_name):
        """Sets the user_key_name of this AwsRegisterCloudSpaceRequest.


        :param user_key_name: The user_key_name of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._user_key_name = user_key_name

    @property
    def network_security_group_map(self):
        """Gets the network_security_group_map of this AwsRegisterCloudSpaceRequest.  # noqa: E501


        :return: The network_security_group_map of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._network_security_group_map

    @network_security_group_map.setter
    def network_security_group_map(self, network_security_group_map):
        """Sets the network_security_group_map of this AwsRegisterCloudSpaceRequest.


        :param network_security_group_map: The network_security_group_map of this AwsRegisterCloudSpaceRequest.  # noqa: E501
        :type: dict(str, str)
        """
        if self.local_vars_configuration.client_side_validation and network_security_group_map is None:  # noqa: E501
            raise ValueError("Invalid value for `network_security_group_map`, must not be `None`")  # noqa: E501

        self._network_security_group_map = network_security_group_map

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
        if not isinstance(other, AwsRegisterCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsRegisterCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
