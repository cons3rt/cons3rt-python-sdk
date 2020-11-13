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


class VCloudRestRegisterCloudSpaceRequest(object):
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
        'local_storage_name': 'str',
        'organization': 'str',
        'organization_vdc': 'str'
    }

    attribute_map = {
        'local_storage_name': 'localStorageName',
        'organization': 'organization',
        'organization_vdc': 'organizationVdc'
    }

    def __init__(self, local_storage_name=None, organization=None, organization_vdc=None, local_vars_configuration=None):  # noqa: E501
        """VCloudRestRegisterCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._local_storage_name = None
        self._organization = None
        self._organization_vdc = None
        self.discriminator = None

        if local_storage_name is not None:
            self.local_storage_name = local_storage_name
        self.organization = organization
        self.organization_vdc = organization_vdc

    @property
    def local_storage_name(self):
        """Gets the local_storage_name of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501


        :return: The local_storage_name of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_storage_name

    @local_storage_name.setter
    def local_storage_name(self, local_storage_name):
        """Sets the local_storage_name of this VCloudRestRegisterCloudSpaceRequest.


        :param local_storage_name: The local_storage_name of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._local_storage_name = local_storage_name

    @property
    def organization(self):
        """Gets the organization of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501


        :return: The organization of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this VCloudRestRegisterCloudSpaceRequest.


        :param organization: The organization of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def organization_vdc(self):
        """Gets the organization_vdc of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501


        :return: The organization_vdc of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_vdc

    @organization_vdc.setter
    def organization_vdc(self, organization_vdc):
        """Sets the organization_vdc of this VCloudRestRegisterCloudSpaceRequest.


        :param organization_vdc: The organization_vdc of this VCloudRestRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organization_vdc is None:  # noqa: E501
            raise ValueError("Invalid value for `organization_vdc`, must not be `None`")  # noqa: E501

        self._organization_vdc = organization_vdc

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
        if not isinstance(other, VCloudRestRegisterCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VCloudRestRegisterCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
