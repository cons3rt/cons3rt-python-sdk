"""
   Copyright 2020 Jackpine Technologies Corporation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration

__author__ = 'Jackpine Technologies Corporation'
__copyright__ = 'Copyright 2020, Jackpine Technologies Corporation'
__license__ = 'Apache 2.0',
__version__ = '1.0.0'
__maintainer__ = 'API Support'
__email__ = 'support@cons3rt.com'


class MinimalSystemAsset(object):
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
        'id': 'int',
        'type': 'str',
        'software_version': 'str'
    }

    attribute_map = {
        'system_asset_version': 'systemAssetVersion',
        'status': 'status',
        'asset_version': 'assetVersion',
        'id': 'id',
        'type': 'type',
        'software_version': 'softwareVersion'
    }

    def __init__(self, system_asset_version=None, status=None, asset_version=None, id=None, type=None, software_version=None, local_vars_configuration=None):  # noqa: E501
        """MinimalSystemAsset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_asset_version = None
        self._status = None
        self._asset_version = None
        self._id = None
        self._type = None
        self._software_version = None
        self.discriminator = None

        if system_asset_version is not None:
            self.system_asset_version = system_asset_version
        if status is not None:
            self.status = status
        if asset_version is not None:
            self.asset_version = asset_version
        if id is not None:
            self.id = id
        self.type = type
        if software_version is not None:
            self.software_version = software_version

    @property
    def system_asset_version(self):
        """Gets the system_asset_version of this MinimalSystemAsset.  # noqa: E501


        :return: The system_asset_version of this MinimalSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._system_asset_version

    @system_asset_version.setter
    def system_asset_version(self, system_asset_version):
        """Sets the system_asset_version of this MinimalSystemAsset.


        :param system_asset_version: The system_asset_version of this MinimalSystemAsset.  # noqa: E501
        :type: str
        """

        self._system_asset_version = system_asset_version

    @property
    def status(self):
        """Gets the status of this MinimalSystemAsset.  # noqa: E501


        :return: The status of this MinimalSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MinimalSystemAsset.


        :param status: The status of this MinimalSystemAsset.  # noqa: E501
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
        """Gets the asset_version of this MinimalSystemAsset.  # noqa: E501


        :return: The asset_version of this MinimalSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._asset_version

    @asset_version.setter
    def asset_version(self, asset_version):
        """Sets the asset_version of this MinimalSystemAsset.


        :param asset_version: The asset_version of this MinimalSystemAsset.  # noqa: E501
        :type: str
        """

        self._asset_version = asset_version

    @property
    def id(self):
        """Gets the id of this MinimalSystemAsset.  # noqa: E501


        :return: The id of this MinimalSystemAsset.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalSystemAsset.


        :param id: The id of this MinimalSystemAsset.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this MinimalSystemAsset.  # noqa: E501


        :return: The type of this MinimalSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MinimalSystemAsset.


        :param type: The type of this MinimalSystemAsset.  # noqa: E501
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
    def software_version(self):
        """Gets the software_version of this MinimalSystemAsset.  # noqa: E501


        :return: The software_version of this MinimalSystemAsset.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this MinimalSystemAsset.


        :param software_version: The software_version of this MinimalSystemAsset.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

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
        if not isinstance(other, MinimalSystemAsset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalSystemAsset):
            return True

        return self.to_dict() != other.to_dict()
