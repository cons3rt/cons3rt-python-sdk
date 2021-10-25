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


class Bucket(object):
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
        'cloud_resource_visibility': 'str',
        'identifier': 'str',
        'name': 'str',
        'cloud_id': 'int',
        'scanning_disabled': 'bool'
    }

    attribute_map = {
        'cloud_resource_visibility': 'cloudResourceVisibility',
        'identifier': 'identifier',
        'name': 'name',
        'cloud_id': 'cloudId',
        'scanning_disabled': 'scanningDisabled'
    }

    def __init__(self, cloud_resource_visibility=None, identifier=None, name=None, cloud_id=None, scanning_disabled=None, local_vars_configuration=None):  # noqa: E501
        """Bucket - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_resource_visibility = None
        self._identifier = None
        self._name = None
        self._cloud_id = None
        self._scanning_disabled = None
        self.discriminator = None

        self.cloud_resource_visibility = cloud_resource_visibility
        if identifier is not None:
            self.identifier = identifier
        self.name = name
        if cloud_id is not None:
            self.cloud_id = cloud_id
        if scanning_disabled is not None:
            self.scanning_disabled = scanning_disabled

    @property
    def cloud_resource_visibility(self):
        """Gets the cloud_resource_visibility of this Bucket.  # noqa: E501


        :return: The cloud_resource_visibility of this Bucket.  # noqa: E501
        :rtype: str
        """
        return self._cloud_resource_visibility

    @cloud_resource_visibility.setter
    def cloud_resource_visibility(self, cloud_resource_visibility):
        """Sets the cloud_resource_visibility of this Bucket.


        :param cloud_resource_visibility: The cloud_resource_visibility of this Bucket.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cloud_resource_visibility is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud_resource_visibility`, must not be `None`")  # noqa: E501
        allowed_values = ["OWNER", "OWNING_PROJECT_READ", "OWNING_PROJECT_WRITE", "TRUSTED_PROJECTS", "COMMUNITY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and cloud_resource_visibility not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `cloud_resource_visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(cloud_resource_visibility, allowed_values)
            )

        self._cloud_resource_visibility = cloud_resource_visibility

    @property
    def identifier(self):
        """Gets the identifier of this Bucket.  # noqa: E501


        :return: The identifier of this Bucket.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Bucket.


        :param identifier: The identifier of this Bucket.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """Gets the name of this Bucket.  # noqa: E501


        :return: The name of this Bucket.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Bucket.


        :param name: The name of this Bucket.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cloud_id(self):
        """Gets the cloud_id of this Bucket.  # noqa: E501


        :return: The cloud_id of this Bucket.  # noqa: E501
        :rtype: int
        """
        return self._cloud_id

    @cloud_id.setter
    def cloud_id(self, cloud_id):
        """Sets the cloud_id of this Bucket.


        :param cloud_id: The cloud_id of this Bucket.  # noqa: E501
        :type: int
        """

        self._cloud_id = cloud_id

    @property
    def scanning_disabled(self):
        """Gets the scanning_disabled of this Bucket.  # noqa: E501


        :return: The scanning_disabled of this Bucket.  # noqa: E501
        :rtype: bool
        """
        return self._scanning_disabled

    @scanning_disabled.setter
    def scanning_disabled(self, scanning_disabled):
        """Sets the scanning_disabled of this Bucket.


        :param scanning_disabled: The scanning_disabled of this Bucket.  # noqa: E501
        :type: bool
        """

        self._scanning_disabled = scanning_disabled

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
        if not isinstance(other, Bucket):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Bucket):
            return True

        return self.to_dict() != other.to_dict()
