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


class VirtualizationRealmBinding(object):
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
        'virtualization_realm': 'MinimalVirtualizationRealm',
        'template_bindings': 'list[TemplateBinding]'
    }

    attribute_map = {
        'virtualization_realm': 'virtualizationRealm',
        'template_bindings': 'templateBindings'
    }

    def __init__(self, virtualization_realm=None, template_bindings=None, local_vars_configuration=None):  # noqa: E501
        """VirtualizationRealmBinding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._virtualization_realm = None
        self._template_bindings = None
        self.discriminator = None

        self.virtualization_realm = virtualization_realm
        self.template_bindings = template_bindings

    @property
    def virtualization_realm(self):
        """Gets the virtualization_realm of this VirtualizationRealmBinding.  # noqa: E501


        :return: The virtualization_realm of this VirtualizationRealmBinding.  # noqa: E501
        :rtype: MinimalVirtualizationRealm
        """
        return self._virtualization_realm

    @virtualization_realm.setter
    def virtualization_realm(self, virtualization_realm):
        """Sets the virtualization_realm of this VirtualizationRealmBinding.


        :param virtualization_realm: The virtualization_realm of this VirtualizationRealmBinding.  # noqa: E501
        :type: MinimalVirtualizationRealm
        """
        if self.local_vars_configuration.client_side_validation and virtualization_realm is None:  # noqa: E501
            raise ValueError("Invalid value for `virtualization_realm`, must not be `None`")  # noqa: E501

        self._virtualization_realm = virtualization_realm

    @property
    def template_bindings(self):
        """Gets the template_bindings of this VirtualizationRealmBinding.  # noqa: E501


        :return: The template_bindings of this VirtualizationRealmBinding.  # noqa: E501
        :rtype: list[TemplateBinding]
        """
        return self._template_bindings

    @template_bindings.setter
    def template_bindings(self, template_bindings):
        """Sets the template_bindings of this VirtualizationRealmBinding.


        :param template_bindings: The template_bindings of this VirtualizationRealmBinding.  # noqa: E501
        :type: list[TemplateBinding]
        """
        if self.local_vars_configuration.client_side_validation and template_bindings is None:  # noqa: E501
            raise ValueError("Invalid value for `template_bindings`, must not be `None`")  # noqa: E501

        self._template_bindings = template_bindings

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
        if not isinstance(other, VirtualizationRealmBinding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VirtualizationRealmBinding):
            return True

        return self.to_dict() != other.to_dict()
