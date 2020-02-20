# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class FullSystemAsset(object):
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
        'system_asset_version': 'str',
        'status': 'str',
        'asset_version': 'str',
        'error': 'str',
        'id': 'int',
        'password': 'str',
        'url': 'str',
        'username': 'str',
        'current_asset': 'MinimalAsset',
        'template_profile': 'MinimalTemplateProfile',
        'type': 'str',
        'softwareversion': 'str'
    }

    attribute_map = {
        'system_asset_version': 'systemAssetVersion',
        'status': 'status',
        'asset_version': 'assetVersion',
        'error': 'error',
        'id': 'id',
        'password': 'password',
        'url': 'url',
        'username': 'username',
        'current_asset': 'currentAsset',
        'template_profile': 'templateProfile',
        'type': 'type',
        'softwareversion': 'softwareversion'
    }

    def __init__(self, system_asset_version=None, status=None, asset_version=None, error=None, id=None, password=None, url=None, username=None, current_asset=None, template_profile=None, type=None, softwareversion=None, local_vars_configuration=None):  # noqa: E501
        """FullSystemAsset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_asset_version = None
        self._status = None
        self._asset_version = None
        self._error = None
        self._id = None
        self._password = None
        self._url = None
        self._username = None
        self._current_asset = None
        self._template_profile = None
        self._type = None
        self._softwareversion = None
        self.discriminator = None

        if system_asset_version is not None:
            self.system_asset_version = system_asset_version
        if status is not None:
            self.status = status
        if asset_version is not None:
            self.asset_version = asset_version
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if password is not None:
            self.password = password
        if url is not None:
            self.url = url
        if username is not None:
            self.username = username
        if current_asset is not None:
            self.current_asset = current_asset
        if template_profile is not None:
            self.template_profile = template_profile
        self.type = type
        if softwareversion is not None:
            self.softwareversion = softwareversion

    @property
    def system_asset_version(self):
        """Gets the system_asset_version of this FullSystemAsset.  # noqa: E501


        :return: The system_asset_version of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._system_asset_version

    @system_asset_version.setter
    def system_asset_version(self, system_asset_version):
        """Sets the system_asset_version of this FullSystemAsset.


        :param system_asset_version: The system_asset_version of this FullSystemAsset.  # noqa: E501
        :type: str
        """

        self._system_asset_version = system_asset_version

    @property
    def status(self):
        """Gets the status of this FullSystemAsset.  # noqa: E501


        :return: The status of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FullSystemAsset.


        :param status: The status of this FullSystemAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "PENDING", "FETCHING", "PROCESSING", "ERROR", "AVAILABLE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def asset_version(self):
        """Gets the asset_version of this FullSystemAsset.  # noqa: E501


        :return: The asset_version of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        """Sets the asset_version of this FullSystemAsset.


        :param asset_version: The asset_version of this FullSystemAsset.  # noqa: E501
        :type: str
        """

        self._asset_version = asset_version

    @property
    def error(self):
        """Gets the error of this FullSystemAsset.  # noqa: E501


        :return: The error of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this FullSystemAsset.


        :param error: The error of this FullSystemAsset.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def id(self):
        """Gets the id of this FullSystemAsset.  # noqa: E501


        :return: The id of this FullSystemAsset.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FullSystemAsset.


        :param id: The id of this FullSystemAsset.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def password(self):
        """Gets the password of this FullSystemAsset.  # noqa: E501


        :return: The password of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this FullSystemAsset.


        :param password: The password of this FullSystemAsset.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def url(self):
        """Gets the url of this FullSystemAsset.  # noqa: E501


        :return: The url of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FullSystemAsset.


        :param url: The url of this FullSystemAsset.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def username(self):
        """Gets the username of this FullSystemAsset.  # noqa: E501


        :return: The username of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this FullSystemAsset.


        :param username: The username of this FullSystemAsset.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def current_asset(self):
        """Gets the current_asset of this FullSystemAsset.  # noqa: E501


        :return: The current_asset of this FullSystemAsset.  # noqa: E501
        :rtype: MinimalAsset
        """
        return self._current_asset

    @current_asset.setter
    def current_asset(self, current_asset):
        """Sets the current_asset of this FullSystemAsset.


        :param current_asset: The current_asset of this FullSystemAsset.  # noqa: E501
        :type: MinimalAsset
        """

        self._current_asset = current_asset

    @property
    def template_profile(self):
        """Gets the template_profile of this FullSystemAsset.  # noqa: E501


        :return: The template_profile of this FullSystemAsset.  # noqa: E501
        :rtype: MinimalTemplateProfile
        """
        return self._template_profile

    @template_profile.setter
    def template_profile(self, template_profile):
        """Sets the template_profile of this FullSystemAsset.


        :param template_profile: The template_profile of this FullSystemAsset.  # noqa: E501
        :type: MinimalTemplateProfile
        """

        self._template_profile = template_profile

    @property
    def type(self):
        """Gets the type of this FullSystemAsset.  # noqa: E501


        :return: The type of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FullSystemAsset.


        :param type: The type of this FullSystemAsset.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["REMOTE_ACCESS", "ELASTIC_TEST_TOOL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def softwareversion(self):
        """Gets the softwareversion of this FullSystemAsset.  # noqa: E501


        :return: The softwareversion of this FullSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._softwareversion

    @softwareversion.setter
    def softwareversion(self, softwareversion):
        """Sets the softwareversion of this FullSystemAsset.


        :param softwareversion: The softwareversion of this FullSystemAsset.  # noqa: E501
        :type: str
        """

        self._softwareversion = softwareversion

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
        if not isinstance(other, FullSystemAsset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullSystemAsset):
            return True

        return self.to_dict() != other.to_dict()
