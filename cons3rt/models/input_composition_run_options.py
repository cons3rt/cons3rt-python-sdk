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


class InputCompositionRunOptions(object):
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
        'description': 'str',
        'virtualization_realm_id': 'int',
        'properties': 'list[InputProperty]',
        'host_options': 'list[InputCompositionHostOption]',
        'windows_domain_name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'virtualization_realm_id': 'virtualizationRealmId',
        'properties': 'properties',
        'host_options': 'hostOptions',
        'windows_domain_name': 'windowsDomainName'
    }

    def __init__(self, description=None, virtualization_realm_id=None, properties=None, host_options=None, windows_domain_name=None, local_vars_configuration=None):  # noqa: E501
        """InputCompositionRunOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._virtualization_realm_id = None
        self._properties = None
        self._host_options = None
        self._windows_domain_name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        self.virtualization_realm_id = virtualization_realm_id
        if properties is not None:
            self.properties = properties
        if host_options is not None:
            self.host_options = host_options
        if windows_domain_name is not None:
            self.windows_domain_name = windows_domain_name

    @property
    def description(self):
        """Gets the description of this InputCompositionRunOptions.  # noqa: E501


        :return: The description of this InputCompositionRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InputCompositionRunOptions.


        :param description: The description of this InputCompositionRunOptions.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def virtualization_realm_id(self):
        """Gets the virtualization_realm_id of this InputCompositionRunOptions.  # noqa: E501


        :return: The virtualization_realm_id of this InputCompositionRunOptions.  # noqa: E501
        :rtype: int
        """
        return self._virtualization_realm_id

    @virtualization_realm_id.setter
    def virtualization_realm_id(self, virtualization_realm_id):
        """Sets the virtualization_realm_id of this InputCompositionRunOptions.


        :param virtualization_realm_id: The virtualization_realm_id of this InputCompositionRunOptions.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and virtualization_realm_id is None:  # noqa: E501
            raise ValueError("Invalid value for `virtualization_realm_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                virtualization_realm_id is not None and virtualization_realm_id < 1):  # noqa: E501
            raise ValueError("Invalid value for `virtualization_realm_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._virtualization_realm_id = virtualization_realm_id

    @property
    def properties(self):
        """Gets the properties of this InputCompositionRunOptions.  # noqa: E501


        :return: The properties of this InputCompositionRunOptions.  # noqa: E501
        :rtype: list[InputProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this InputCompositionRunOptions.


        :param properties: The properties of this InputCompositionRunOptions.  # noqa: E501
        :type: list[InputProperty]
        """

        self._properties = properties

    @property
    def host_options(self):
        """Gets the host_options of this InputCompositionRunOptions.  # noqa: E501


        :return: The host_options of this InputCompositionRunOptions.  # noqa: E501
        :rtype: list[InputCompositionHostOption]
        """
        return self._host_options

    @host_options.setter
    def host_options(self, host_options):
        """Sets the host_options of this InputCompositionRunOptions.


        :param host_options: The host_options of this InputCompositionRunOptions.  # noqa: E501
        :type: list[InputCompositionHostOption]
        """

        self._host_options = host_options

    @property
    def windows_domain_name(self):
        """Gets the windows_domain_name of this InputCompositionRunOptions.  # noqa: E501


        :return: The windows_domain_name of this InputCompositionRunOptions.  # noqa: E501
        :rtype: str
        """
        return self._windows_domain_name

    @windows_domain_name.setter
    def windows_domain_name(self, windows_domain_name):
        """Sets the windows_domain_name of this InputCompositionRunOptions.


        :param windows_domain_name: The windows_domain_name of this InputCompositionRunOptions.  # noqa: E501
        :type: str
        """

        self._windows_domain_name = windows_domain_name

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
        if not isinstance(other, InputCompositionRunOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputCompositionRunOptions):
            return True

        return self.to_dict() != other.to_dict()
