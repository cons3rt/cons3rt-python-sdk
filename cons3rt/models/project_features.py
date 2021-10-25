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


class ProjectFeatures(object):
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
        'asset_bypass_scanning_enabled': 'bool',
        'remote_access_copy_enabled': 'bool',
        'remote_access_file_download_enabled': 'bool',
        'remote_access_file_upload_enabled': 'bool',
        'remote_access_paste_enabled': 'bool'
    }

    attribute_map = {
        'asset_bypass_scanning_enabled': 'assetBypassScanningEnabled',
        'remote_access_copy_enabled': 'remoteAccessCopyEnabled',
        'remote_access_file_download_enabled': 'remoteAccessFileDownloadEnabled',
        'remote_access_file_upload_enabled': 'remoteAccessFileUploadEnabled',
        'remote_access_paste_enabled': 'remoteAccessPasteEnabled'
    }

    def __init__(self, asset_bypass_scanning_enabled=None, remote_access_copy_enabled=None, remote_access_file_download_enabled=None, remote_access_file_upload_enabled=None, remote_access_paste_enabled=None, local_vars_configuration=None):  # noqa: E501
        """ProjectFeatures - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_bypass_scanning_enabled = None
        self._remote_access_copy_enabled = None
        self._remote_access_file_download_enabled = None
        self._remote_access_file_upload_enabled = None
        self._remote_access_paste_enabled = None
        self.discriminator = None

        if asset_bypass_scanning_enabled is not None:
            self.asset_bypass_scanning_enabled = asset_bypass_scanning_enabled
        if remote_access_copy_enabled is not None:
            self.remote_access_copy_enabled = remote_access_copy_enabled
        if remote_access_file_download_enabled is not None:
            self.remote_access_file_download_enabled = remote_access_file_download_enabled
        if remote_access_file_upload_enabled is not None:
            self.remote_access_file_upload_enabled = remote_access_file_upload_enabled
        if remote_access_paste_enabled is not None:
            self.remote_access_paste_enabled = remote_access_paste_enabled

    @property
    def asset_bypass_scanning_enabled(self):
        """Gets the asset_bypass_scanning_enabled of this ProjectFeatures.  # noqa: E501


        :return: The asset_bypass_scanning_enabled of this ProjectFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._asset_bypass_scanning_enabled

    @asset_bypass_scanning_enabled.setter
    def asset_bypass_scanning_enabled(self, asset_bypass_scanning_enabled):
        """Sets the asset_bypass_scanning_enabled of this ProjectFeatures.


        :param asset_bypass_scanning_enabled: The asset_bypass_scanning_enabled of this ProjectFeatures.  # noqa: E501
        :type: bool
        """

        self._asset_bypass_scanning_enabled = asset_bypass_scanning_enabled

    @property
    def remote_access_copy_enabled(self):
        """Gets the remote_access_copy_enabled of this ProjectFeatures.  # noqa: E501


        :return: The remote_access_copy_enabled of this ProjectFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._remote_access_copy_enabled

    @remote_access_copy_enabled.setter
    def remote_access_copy_enabled(self, remote_access_copy_enabled):
        """Sets the remote_access_copy_enabled of this ProjectFeatures.


        :param remote_access_copy_enabled: The remote_access_copy_enabled of this ProjectFeatures.  # noqa: E501
        :type: bool
        """

        self._remote_access_copy_enabled = remote_access_copy_enabled

    @property
    def remote_access_file_download_enabled(self):
        """Gets the remote_access_file_download_enabled of this ProjectFeatures.  # noqa: E501


        :return: The remote_access_file_download_enabled of this ProjectFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._remote_access_file_download_enabled

    @remote_access_file_download_enabled.setter
    def remote_access_file_download_enabled(self, remote_access_file_download_enabled):
        """Sets the remote_access_file_download_enabled of this ProjectFeatures.


        :param remote_access_file_download_enabled: The remote_access_file_download_enabled of this ProjectFeatures.  # noqa: E501
        :type: bool
        """

        self._remote_access_file_download_enabled = remote_access_file_download_enabled

    @property
    def remote_access_file_upload_enabled(self):
        """Gets the remote_access_file_upload_enabled of this ProjectFeatures.  # noqa: E501


        :return: The remote_access_file_upload_enabled of this ProjectFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._remote_access_file_upload_enabled

    @remote_access_file_upload_enabled.setter
    def remote_access_file_upload_enabled(self, remote_access_file_upload_enabled):
        """Sets the remote_access_file_upload_enabled of this ProjectFeatures.


        :param remote_access_file_upload_enabled: The remote_access_file_upload_enabled of this ProjectFeatures.  # noqa: E501
        :type: bool
        """

        self._remote_access_file_upload_enabled = remote_access_file_upload_enabled

    @property
    def remote_access_paste_enabled(self):
        """Gets the remote_access_paste_enabled of this ProjectFeatures.  # noqa: E501


        :return: The remote_access_paste_enabled of this ProjectFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._remote_access_paste_enabled

    @remote_access_paste_enabled.setter
    def remote_access_paste_enabled(self, remote_access_paste_enabled):
        """Sets the remote_access_paste_enabled of this ProjectFeatures.


        :param remote_access_paste_enabled: The remote_access_paste_enabled of this ProjectFeatures.  # noqa: E501
        :type: bool
        """

        self._remote_access_paste_enabled = remote_access_paste_enabled

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
        if not isinstance(other, ProjectFeatures):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectFeatures):
            return True

        return self.to_dict() != other.to_dict()
