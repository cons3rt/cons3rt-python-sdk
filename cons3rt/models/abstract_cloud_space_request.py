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


class AbstractCloudSpaceRequest(object):
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
        'cloud_space_name': 'str',
        'maximum_virtual_machines': 'int',
        'cidr': 'str',
        'num_availability_zones': 'int',
        'power_on_minimum_delay': 'int',
        'subtype': 'str'
    }

    attribute_map = {
        'cloud_space_name': 'cloudSpaceName',
        'maximum_virtual_machines': 'maximumVirtualMachines',
        'cidr': 'cidr',
        'num_availability_zones': 'numAvailabilityZones',
        'power_on_minimum_delay': 'powerOnMinimumDelay',
        'subtype': 'subtype'
    }

    discriminator_value_class_map = {
        'OpenStackCloudSpaceRequest': 'OpenStackCloudSpaceRequest',
        'VCloudRestCloudSpaceRequest': 'VCloudRestCloudSpaceRequest',
        'AwsCloudSpaceRequest': 'AwsCloudSpaceRequest',
        'AzureCloudSpaceRequest': 'AzureCloudSpaceRequest'
    }

    def __init__(self, cloud_space_name=None, maximum_virtual_machines=None, cidr=None, num_availability_zones=None, power_on_minimum_delay=None, subtype=None, local_vars_configuration=None):  # noqa: E501
        """AbstractCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_space_name = None
        self._maximum_virtual_machines = None
        self._cidr = None
        self._num_availability_zones = None
        self._power_on_minimum_delay = None
        self._subtype = None
        self.discriminator = 'subtype'

        self.cloud_space_name = cloud_space_name
        if maximum_virtual_machines is not None:
            self.maximum_virtual_machines = maximum_virtual_machines
        self.cidr = cidr
        if num_availability_zones is not None:
            self.num_availability_zones = num_availability_zones
        if power_on_minimum_delay is not None:
            self.power_on_minimum_delay = power_on_minimum_delay
        self.subtype = subtype

    @property
    def cloud_space_name(self):
        """Gets the cloud_space_name of this AbstractCloudSpaceRequest.  # noqa: E501


        :return: The cloud_space_name of this AbstractCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._cloud_space_name

    @cloud_space_name.setter
    def cloud_space_name(self, cloud_space_name):
        """Sets the cloud_space_name of this AbstractCloudSpaceRequest.


        :param cloud_space_name: The cloud_space_name of this AbstractCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cloud_space_name is None:  # noqa: E501
            raise ValueError("Invalid value for `cloud_space_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cloud_space_name is not None and len(cloud_space_name) > 25):
            raise ValueError("Invalid value for `cloud_space_name`, length must be less than or equal to `25`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cloud_space_name is not None and len(cloud_space_name) < 1):
            raise ValueError("Invalid value for `cloud_space_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._cloud_space_name = cloud_space_name

    @property
    def maximum_virtual_machines(self):
        """Gets the maximum_virtual_machines of this AbstractCloudSpaceRequest.  # noqa: E501


        :return: The maximum_virtual_machines of this AbstractCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_virtual_machines

    @maximum_virtual_machines.setter
    def maximum_virtual_machines(self, maximum_virtual_machines):
        """Sets the maximum_virtual_machines of this AbstractCloudSpaceRequest.


        :param maximum_virtual_machines: The maximum_virtual_machines of this AbstractCloudSpaceRequest.  # noqa: E501
        :type: int
        """

        self._maximum_virtual_machines = maximum_virtual_machines

    @property
    def cidr(self):
        """Gets the cidr of this AbstractCloudSpaceRequest.  # noqa: E501


        :return: The cidr of this AbstractCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this AbstractCloudSpaceRequest.


        :param cidr: The cidr of this AbstractCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cidr is None:  # noqa: E501
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cidr is not None and len(cidr) > 16):
            raise ValueError("Invalid value for `cidr`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                cidr is not None and len(cidr) < 10):
            raise ValueError("Invalid value for `cidr`, length must be greater than or equal to `10`")  # noqa: E501

        self._cidr = cidr

    @property
    def num_availability_zones(self):
        """Gets the num_availability_zones of this AbstractCloudSpaceRequest.  # noqa: E501


        :return: The num_availability_zones of this AbstractCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._num_availability_zones

    @num_availability_zones.setter
    def num_availability_zones(self, num_availability_zones):
        """Sets the num_availability_zones of this AbstractCloudSpaceRequest.


        :param num_availability_zones: The num_availability_zones of this AbstractCloudSpaceRequest.  # noqa: E501
        :type: int
        """

        self._num_availability_zones = num_availability_zones

    @property
    def power_on_minimum_delay(self):
        """Gets the power_on_minimum_delay of this AbstractCloudSpaceRequest.  # noqa: E501


        :return: The power_on_minimum_delay of this AbstractCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._power_on_minimum_delay

    @power_on_minimum_delay.setter
    def power_on_minimum_delay(self, power_on_minimum_delay):
        """Sets the power_on_minimum_delay of this AbstractCloudSpaceRequest.


        :param power_on_minimum_delay: The power_on_minimum_delay of this AbstractCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                power_on_minimum_delay is not None and power_on_minimum_delay < 0):  # noqa: E501
            raise ValueError("Invalid value for `power_on_minimum_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._power_on_minimum_delay = power_on_minimum_delay

    @property
    def subtype(self):
        """Gets the subtype of this AbstractCloudSpaceRequest.  # noqa: E501


        :return: The subtype of this AbstractCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this AbstractCloudSpaceRequest.


        :param subtype: The subtype of this AbstractCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, AbstractCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AbstractCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
