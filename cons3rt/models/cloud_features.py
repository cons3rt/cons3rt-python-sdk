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


class CloudFeatures(object):
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
        'allocation_capable': 'bool',
        'bypass_scanning_enabled': 'bool',
        'deallocation_capable': 'bool',
        'gpu_available': 'bool',
        'storage_service_enabled': 'bool'
    }

    attribute_map = {
        'allocation_capable': 'allocationCapable',
        'bypass_scanning_enabled': 'bypassScanningEnabled',
        'deallocation_capable': 'deallocationCapable',
        'gpu_available': 'gpuAvailable',
        'storage_service_enabled': 'storageServiceEnabled'
    }

    def __init__(self, allocation_capable=None, bypass_scanning_enabled=None, deallocation_capable=None, gpu_available=None, storage_service_enabled=None, local_vars_configuration=None):  # noqa: E501
        """CloudFeatures - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._allocation_capable = None
        self._bypass_scanning_enabled = None
        self._deallocation_capable = None
        self._gpu_available = None
        self._storage_service_enabled = None
        self.discriminator = None

        if allocation_capable is not None:
            self.allocation_capable = allocation_capable
        if bypass_scanning_enabled is not None:
            self.bypass_scanning_enabled = bypass_scanning_enabled
        if deallocation_capable is not None:
            self.deallocation_capable = deallocation_capable
        if gpu_available is not None:
            self.gpu_available = gpu_available
        if storage_service_enabled is not None:
            self.storage_service_enabled = storage_service_enabled

    @property
    def allocation_capable(self):
        """Gets the allocation_capable of this CloudFeatures.  # noqa: E501


        :return: The allocation_capable of this CloudFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._allocation_capable

    @allocation_capable.setter
    def allocation_capable(self, allocation_capable):
        """Sets the allocation_capable of this CloudFeatures.


        :param allocation_capable: The allocation_capable of this CloudFeatures.  # noqa: E501
        :type: bool
        """

        self._allocation_capable = allocation_capable

    @property
    def bypass_scanning_enabled(self):
        """Gets the bypass_scanning_enabled of this CloudFeatures.  # noqa: E501


        :return: The bypass_scanning_enabled of this CloudFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._bypass_scanning_enabled

    @bypass_scanning_enabled.setter
    def bypass_scanning_enabled(self, bypass_scanning_enabled):
        """Sets the bypass_scanning_enabled of this CloudFeatures.


        :param bypass_scanning_enabled: The bypass_scanning_enabled of this CloudFeatures.  # noqa: E501
        :type: bool
        """

        self._bypass_scanning_enabled = bypass_scanning_enabled

    @property
    def deallocation_capable(self):
        """Gets the deallocation_capable of this CloudFeatures.  # noqa: E501


        :return: The deallocation_capable of this CloudFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._deallocation_capable

    @deallocation_capable.setter
    def deallocation_capable(self, deallocation_capable):
        """Sets the deallocation_capable of this CloudFeatures.


        :param deallocation_capable: The deallocation_capable of this CloudFeatures.  # noqa: E501
        :type: bool
        """

        self._deallocation_capable = deallocation_capable

    @property
    def gpu_available(self):
        """Gets the gpu_available of this CloudFeatures.  # noqa: E501


        :return: The gpu_available of this CloudFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._gpu_available

    @gpu_available.setter
    def gpu_available(self, gpu_available):
        """Sets the gpu_available of this CloudFeatures.


        :param gpu_available: The gpu_available of this CloudFeatures.  # noqa: E501
        :type: bool
        """

        self._gpu_available = gpu_available

    @property
    def storage_service_enabled(self):
        """Gets the storage_service_enabled of this CloudFeatures.  # noqa: E501


        :return: The storage_service_enabled of this CloudFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._storage_service_enabled

    @storage_service_enabled.setter
    def storage_service_enabled(self, storage_service_enabled):
        """Sets the storage_service_enabled of this CloudFeatures.


        :param storage_service_enabled: The storage_service_enabled of this CloudFeatures.  # noqa: E501
        :type: bool
        """

        self._storage_service_enabled = storage_service_enabled

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
        if not isinstance(other, CloudFeatures):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CloudFeatures):
            return True

        return self.to_dict() != other.to_dict()
