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


class BaseIdentity(object):
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
        'identifier': 'str',
        'user': 'MinimalUser',
        'project': 'MinimalProject',
        'access_listing': 'list[CloudResourceAccessListing]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'user': 'user',
        'project': 'project',
        'access_listing': 'accessListing'
    }

    def __init__(self, identifier=None, user=None, project=None, access_listing=None, local_vars_configuration=None):  # noqa: E501
        """BaseIdentity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._identifier = None
        self._user = None
        self._project = None
        self._access_listing = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if user is not None:
            self.user = user
        if project is not None:
            self.project = project
        if access_listing is not None:
            self.access_listing = access_listing

    @property
    def identifier(self):
        """Gets the identifier of this BaseIdentity.  # noqa: E501


        :return: The identifier of this BaseIdentity.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this BaseIdentity.


        :param identifier: The identifier of this BaseIdentity.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def user(self):
        """Gets the user of this BaseIdentity.  # noqa: E501


        :return: The user of this BaseIdentity.  # noqa: E501
        :rtype: MinimalUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BaseIdentity.


        :param user: The user of this BaseIdentity.  # noqa: E501
        :type: MinimalUser
        """

        self._user = user

    @property
    def project(self):
        """Gets the project of this BaseIdentity.  # noqa: E501


        :return: The project of this BaseIdentity.  # noqa: E501
        :rtype: MinimalProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this BaseIdentity.


        :param project: The project of this BaseIdentity.  # noqa: E501
        :type: MinimalProject
        """

        self._project = project

    @property
    def access_listing(self):
        """Gets the access_listing of this BaseIdentity.  # noqa: E501


        :return: The access_listing of this BaseIdentity.  # noqa: E501
        :rtype: list[CloudResourceAccessListing]
        """
        return self._access_listing

    @access_listing.setter
    def access_listing(self, access_listing):
        """Sets the access_listing of this BaseIdentity.


        :param access_listing: The access_listing of this BaseIdentity.  # noqa: E501
        :type: list[CloudResourceAccessListing]
        """

        self._access_listing = access_listing

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
        if not isinstance(other, BaseIdentity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseIdentity):
            return True

        return self.to_dict() != other.to_dict()
