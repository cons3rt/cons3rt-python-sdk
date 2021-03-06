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


class VCloudCloudResourcesAllOf(object):
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
        'external_network_names': 'list[str]',
        'provider_vdc_names': 'list[str]',
        'vdc_network_pool_names': 'list[str]'
    }

    attribute_map = {
        'external_network_names': 'externalNetworkNames',
        'provider_vdc_names': 'providerVdcNames',
        'vdc_network_pool_names': 'vdcNetworkPoolNames'
    }

    def __init__(self, external_network_names=None, provider_vdc_names=None, vdc_network_pool_names=None, local_vars_configuration=None):  # noqa: E501
        """VCloudCloudResourcesAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._external_network_names = None
        self._provider_vdc_names = None
        self._vdc_network_pool_names = None
        self.discriminator = None

        if external_network_names is not None:
            self.external_network_names = external_network_names
        if provider_vdc_names is not None:
            self.provider_vdc_names = provider_vdc_names
        if vdc_network_pool_names is not None:
            self.vdc_network_pool_names = vdc_network_pool_names

    @property
    def external_network_names(self):
        """Gets the external_network_names of this VCloudCloudResourcesAllOf.  # noqa: E501


        :return: The external_network_names of this VCloudCloudResourcesAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_network_names

    @external_network_names.setter
    def external_network_names(self, external_network_names):
        """Sets the external_network_names of this VCloudCloudResourcesAllOf.


        :param external_network_names: The external_network_names of this VCloudCloudResourcesAllOf.  # noqa: E501
        :type: list[str]
        """

        self._external_network_names = external_network_names

    @property
    def provider_vdc_names(self):
        """Gets the provider_vdc_names of this VCloudCloudResourcesAllOf.  # noqa: E501


        :return: The provider_vdc_names of this VCloudCloudResourcesAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._provider_vdc_names

    @provider_vdc_names.setter
    def provider_vdc_names(self, provider_vdc_names):
        """Sets the provider_vdc_names of this VCloudCloudResourcesAllOf.


        :param provider_vdc_names: The provider_vdc_names of this VCloudCloudResourcesAllOf.  # noqa: E501
        :type: list[str]
        """

        self._provider_vdc_names = provider_vdc_names

    @property
    def vdc_network_pool_names(self):
        """Gets the vdc_network_pool_names of this VCloudCloudResourcesAllOf.  # noqa: E501


        :return: The vdc_network_pool_names of this VCloudCloudResourcesAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._vdc_network_pool_names

    @vdc_network_pool_names.setter
    def vdc_network_pool_names(self, vdc_network_pool_names):
        """Sets the vdc_network_pool_names of this VCloudCloudResourcesAllOf.


        :param vdc_network_pool_names: The vdc_network_pool_names of this VCloudCloudResourcesAllOf.  # noqa: E501
        :type: list[str]
        """

        self._vdc_network_pool_names = vdc_network_pool_names

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
        if not isinstance(other, VCloudCloudResourcesAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VCloudCloudResourcesAllOf):
            return True

        return self.to_dict() != other.to_dict()
