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


class ProjectLimits(object):
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
        'gpu_type_maximums': 'dict(str, int)',
        'max_num_cpus': 'int',
        'max_num_gpus': 'int',
        'max_ram_in_megabytes': 'int',
        'max_storage_in_megabytes': 'int',
        'max_virtual_machines': 'int',
        'valid_until': 'int'
    }

    attribute_map = {
        'gpu_type_maximums': 'gpuTypeMaximums',
        'max_num_cpus': 'maxNumCpus',
        'max_num_gpus': 'maxNumGpus',
        'max_ram_in_megabytes': 'maxRamInMegabytes',
        'max_storage_in_megabytes': 'maxStorageInMegabytes',
        'max_virtual_machines': 'maxVirtualMachines',
        'valid_until': 'validUntil'
    }

    def __init__(self, gpu_type_maximums=None, max_num_cpus=None, max_num_gpus=None, max_ram_in_megabytes=None, max_storage_in_megabytes=None, max_virtual_machines=None, valid_until=None, local_vars_configuration=None):  # noqa: E501
        """ProjectLimits - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._gpu_type_maximums = None
        self._max_num_cpus = None
        self._max_num_gpus = None
        self._max_ram_in_megabytes = None
        self._max_storage_in_megabytes = None
        self._max_virtual_machines = None
        self._valid_until = None
        self.discriminator = None

        if gpu_type_maximums is not None:
            self.gpu_type_maximums = gpu_type_maximums
        self.max_num_cpus = max_num_cpus
        self.max_num_gpus = max_num_gpus
        self.max_ram_in_megabytes = max_ram_in_megabytes
        self.max_storage_in_megabytes = max_storage_in_megabytes
        self.max_virtual_machines = max_virtual_machines
        if valid_until is not None:
            self.valid_until = valid_until

    @property
    def gpu_type_maximums(self):
        """Gets the gpu_type_maximums of this ProjectLimits.  # noqa: E501


        :return: The gpu_type_maximums of this ProjectLimits.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._gpu_type_maximums

    @gpu_type_maximums.setter
    def gpu_type_maximums(self, gpu_type_maximums):
        """Sets the gpu_type_maximums of this ProjectLimits.


        :param gpu_type_maximums: The gpu_type_maximums of this ProjectLimits.  # noqa: E501
        :type: dict(str, int)
        """

        self._gpu_type_maximums = gpu_type_maximums

    @property
    def max_num_cpus(self):
        """Gets the max_num_cpus of this ProjectLimits.  # noqa: E501


        :return: The max_num_cpus of this ProjectLimits.  # noqa: E501
        :rtype: int
        """
        return self._max_num_cpus

    @max_num_cpus.setter
    def max_num_cpus(self, max_num_cpus):
        """Sets the max_num_cpus of this ProjectLimits.


        :param max_num_cpus: The max_num_cpus of this ProjectLimits.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_num_cpus is None:  # noqa: E501
            raise ValueError("Invalid value for `max_num_cpus`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_num_cpus is not None and max_num_cpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_num_cpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_num_cpus = max_num_cpus

    @property
    def max_num_gpus(self):
        """Gets the max_num_gpus of this ProjectLimits.  # noqa: E501


        :return: The max_num_gpus of this ProjectLimits.  # noqa: E501
        :rtype: int
        """
        return self._max_num_gpus

    @max_num_gpus.setter
    def max_num_gpus(self, max_num_gpus):
        """Sets the max_num_gpus of this ProjectLimits.


        :param max_num_gpus: The max_num_gpus of this ProjectLimits.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_num_gpus is None:  # noqa: E501
            raise ValueError("Invalid value for `max_num_gpus`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_num_gpus is not None and max_num_gpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_num_gpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_num_gpus = max_num_gpus

    @property
    def max_ram_in_megabytes(self):
        """Gets the max_ram_in_megabytes of this ProjectLimits.  # noqa: E501


        :return: The max_ram_in_megabytes of this ProjectLimits.  # noqa: E501
        :rtype: int
        """
        return self._max_ram_in_megabytes

    @max_ram_in_megabytes.setter
    def max_ram_in_megabytes(self, max_ram_in_megabytes):
        """Sets the max_ram_in_megabytes of this ProjectLimits.


        :param max_ram_in_megabytes: The max_ram_in_megabytes of this ProjectLimits.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_ram_in_megabytes is None:  # noqa: E501
            raise ValueError("Invalid value for `max_ram_in_megabytes`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_ram_in_megabytes is not None and max_ram_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_ram_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_ram_in_megabytes = max_ram_in_megabytes

    @property
    def max_storage_in_megabytes(self):
        """Gets the max_storage_in_megabytes of this ProjectLimits.  # noqa: E501


        :return: The max_storage_in_megabytes of this ProjectLimits.  # noqa: E501
        :rtype: int
        """
        return self._max_storage_in_megabytes

    @max_storage_in_megabytes.setter
    def max_storage_in_megabytes(self, max_storage_in_megabytes):
        """Sets the max_storage_in_megabytes of this ProjectLimits.


        :param max_storage_in_megabytes: The max_storage_in_megabytes of this ProjectLimits.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_storage_in_megabytes is None:  # noqa: E501
            raise ValueError("Invalid value for `max_storage_in_megabytes`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_storage_in_megabytes is not None and max_storage_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_storage_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_storage_in_megabytes = max_storage_in_megabytes

    @property
    def max_virtual_machines(self):
        """Gets the max_virtual_machines of this ProjectLimits.  # noqa: E501


        :return: The max_virtual_machines of this ProjectLimits.  # noqa: E501
        :rtype: int
        """
        return self._max_virtual_machines

    @max_virtual_machines.setter
    def max_virtual_machines(self, max_virtual_machines):
        """Sets the max_virtual_machines of this ProjectLimits.


        :param max_virtual_machines: The max_virtual_machines of this ProjectLimits.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_virtual_machines is None:  # noqa: E501
            raise ValueError("Invalid value for `max_virtual_machines`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_virtual_machines is not None and max_virtual_machines < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_virtual_machines`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_virtual_machines = max_virtual_machines

    @property
    def valid_until(self):
        """Gets the valid_until of this ProjectLimits.  # noqa: E501


        :return: The valid_until of this ProjectLimits.  # noqa: E501
        :rtype: int
        """
        return self._valid_until

    @valid_until.setter
    def valid_until(self, valid_until):
        """Sets the valid_until of this ProjectLimits.


        :param valid_until: The valid_until of this ProjectLimits.  # noqa: E501
        :type: int
        """

        self._valid_until = valid_until

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
        if not isinstance(other, ProjectLimits):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectLimits):
            return True

        return self.to_dict() != other.to_dict()
