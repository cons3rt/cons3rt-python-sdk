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


class InputSFTPSubmissionEndpointForAssetSubmission(object):
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
        'remote_path': 'str',
        'use_user_directory_as_root': 'bool'
    }

    attribute_map = {
        'remote_path': 'remotePath',
        'use_user_directory_as_root': 'useUserDirectoryAsRoot'
    }

    def __init__(self, remote_path=None, use_user_directory_as_root=None, local_vars_configuration=None):  # noqa: E501
        """InputSFTPSubmissionEndpointForAssetSubmission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._remote_path = None
        self._use_user_directory_as_root = None
        self.discriminator = None

        if remote_path is not None:
            self.remote_path = remote_path
        if use_user_directory_as_root is not None:
            self.use_user_directory_as_root = use_user_directory_as_root

    @property
    def remote_path(self):
        """Gets the remote_path of this InputSFTPSubmissionEndpointForAssetSubmission.  # noqa: E501


        :return: The remote_path of this InputSFTPSubmissionEndpointForAssetSubmission.  # noqa: E501
        :rtype: str
        """
        return self._remote_path

    @remote_path.setter
    def remote_path(self, remote_path):
        """Sets the remote_path of this InputSFTPSubmissionEndpointForAssetSubmission.


        :param remote_path: The remote_path of this InputSFTPSubmissionEndpointForAssetSubmission.  # noqa: E501
        :type: str
        """

        self._remote_path = remote_path

    @property
    def use_user_directory_as_root(self):
        """Gets the use_user_directory_as_root of this InputSFTPSubmissionEndpointForAssetSubmission.  # noqa: E501


        :return: The use_user_directory_as_root of this InputSFTPSubmissionEndpointForAssetSubmission.  # noqa: E501
        :rtype: bool
        """
        return self._use_user_directory_as_root

    @use_user_directory_as_root.setter
    def use_user_directory_as_root(self, use_user_directory_as_root):
        """Sets the use_user_directory_as_root of this InputSFTPSubmissionEndpointForAssetSubmission.


        :param use_user_directory_as_root: The use_user_directory_as_root of this InputSFTPSubmissionEndpointForAssetSubmission.  # noqa: E501
        :type: bool
        """

        self._use_user_directory_as_root = use_user_directory_as_root

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
        if not isinstance(other, InputSFTPSubmissionEndpointForAssetSubmission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputSFTPSubmissionEndpointForAssetSubmission):
            return True

        return self.to_dict() != other.to_dict()
