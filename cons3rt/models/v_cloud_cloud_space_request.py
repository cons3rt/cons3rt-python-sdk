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


class VCloudCloudSpaceRequest(object):
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
        'subtype': 'str',
        'provider_vdc_name': 'str',
        'vdc_network_pool_name': 'str',
        'username': 'str',
        'password': 'str',
        'email_address': 'str',
        'external_network_name': 'str',
        'maximum_cpu_mhz': 'int',
        'local_catalog_name': 'str',
        'vdc_network_quota': 'int'
    }

    attribute_map = {
        'cloud_space_name': 'cloudSpaceName',
        'maximum_virtual_machines': 'maximumVirtualMachines',
        'cidr': 'cidr',
        'num_availability_zones': 'numAvailabilityZones',
        'power_on_minimum_delay': 'powerOnMinimumDelay',
        'subtype': 'subtype',
        'provider_vdc_name': 'providerVdcName',
        'vdc_network_pool_name': 'vdcNetworkPoolName',
        'username': 'username',
        'password': 'password',
        'email_address': 'emailAddress',
        'external_network_name': 'externalNetworkName',
        'maximum_cpu_mhz': 'maximumCpuMhz',
        'local_catalog_name': 'localCatalogName',
        'vdc_network_quota': 'vdcNetworkQuota'
    }

    def __init__(self, cloud_space_name=None, maximum_virtual_machines=None, cidr=None, num_availability_zones=None, power_on_minimum_delay=None, subtype=None, provider_vdc_name=None, vdc_network_pool_name=None, username=None, password=None, email_address=None, external_network_name=None, maximum_cpu_mhz=None, local_catalog_name=None, vdc_network_quota=None, local_vars_configuration=None):  # noqa: E501
        """VCloudCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cloud_space_name = None
        self._maximum_virtual_machines = None
        self._cidr = None
        self._num_availability_zones = None
        self._power_on_minimum_delay = None
        self._subtype = None
        self._provider_vdc_name = None
        self._vdc_network_pool_name = None
        self._username = None
        self._password = None
        self._email_address = None
        self._external_network_name = None
        self._maximum_cpu_mhz = None
        self._local_catalog_name = None
        self._vdc_network_quota = None
        self.discriminator = None

        self.cloud_space_name = cloud_space_name
        if maximum_virtual_machines is not None:
            self.maximum_virtual_machines = maximum_virtual_machines
        self.cidr = cidr
        if num_availability_zones is not None:
            self.num_availability_zones = num_availability_zones
        if power_on_minimum_delay is not None:
            self.power_on_minimum_delay = power_on_minimum_delay
        self.subtype = subtype
        self.provider_vdc_name = provider_vdc_name
        self.vdc_network_pool_name = vdc_network_pool_name
        self.username = username
        self.password = password
        self.email_address = email_address
        self.external_network_name = external_network_name
        self.maximum_cpu_mhz = maximum_cpu_mhz
        if local_catalog_name is not None:
            self.local_catalog_name = local_catalog_name
        self.vdc_network_quota = vdc_network_quota

    @property
    def cloud_space_name(self):
        """Gets the cloud_space_name of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The cloud_space_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._cloud_space_name

    @cloud_space_name.setter
    def cloud_space_name(self, cloud_space_name):
        """Sets the cloud_space_name of this VCloudCloudSpaceRequest.


        :param cloud_space_name: The cloud_space_name of this VCloudCloudSpaceRequest.  # noqa: E501
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
        """Gets the maximum_virtual_machines of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The maximum_virtual_machines of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_virtual_machines

    @maximum_virtual_machines.setter
    def maximum_virtual_machines(self, maximum_virtual_machines):
        """Sets the maximum_virtual_machines of this VCloudCloudSpaceRequest.


        :param maximum_virtual_machines: The maximum_virtual_machines of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: int
        """

        self._maximum_virtual_machines = maximum_virtual_machines

    @property
    def cidr(self):
        """Gets the cidr of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The cidr of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this VCloudCloudSpaceRequest.


        :param cidr: The cidr of this VCloudCloudSpaceRequest.  # noqa: E501
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
        """Gets the num_availability_zones of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The num_availability_zones of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._num_availability_zones

    @num_availability_zones.setter
    def num_availability_zones(self, num_availability_zones):
        """Sets the num_availability_zones of this VCloudCloudSpaceRequest.


        :param num_availability_zones: The num_availability_zones of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: int
        """

        self._num_availability_zones = num_availability_zones

    @property
    def power_on_minimum_delay(self):
        """Gets the power_on_minimum_delay of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The power_on_minimum_delay of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._power_on_minimum_delay

    @power_on_minimum_delay.setter
    def power_on_minimum_delay(self, power_on_minimum_delay):
        """Sets the power_on_minimum_delay of this VCloudCloudSpaceRequest.


        :param power_on_minimum_delay: The power_on_minimum_delay of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                power_on_minimum_delay is not None and power_on_minimum_delay < 0):  # noqa: E501
            raise ValueError("Invalid value for `power_on_minimum_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._power_on_minimum_delay = power_on_minimum_delay

    @property
    def subtype(self):
        """Gets the subtype of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The subtype of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this VCloudCloudSpaceRequest.


        :param subtype: The subtype of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def provider_vdc_name(self):
        """Gets the provider_vdc_name of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The provider_vdc_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._provider_vdc_name

    @provider_vdc_name.setter
    def provider_vdc_name(self, provider_vdc_name):
        """Sets the provider_vdc_name of this VCloudCloudSpaceRequest.


        :param provider_vdc_name: The provider_vdc_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and provider_vdc_name is None:  # noqa: E501
            raise ValueError("Invalid value for `provider_vdc_name`, must not be `None`")  # noqa: E501

        self._provider_vdc_name = provider_vdc_name

    @property
    def vdc_network_pool_name(self):
        """Gets the vdc_network_pool_name of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The vdc_network_pool_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._vdc_network_pool_name

    @vdc_network_pool_name.setter
    def vdc_network_pool_name(self, vdc_network_pool_name):
        """Sets the vdc_network_pool_name of this VCloudCloudSpaceRequest.


        :param vdc_network_pool_name: The vdc_network_pool_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and vdc_network_pool_name is None:  # noqa: E501
            raise ValueError("Invalid value for `vdc_network_pool_name`, must not be `None`")  # noqa: E501

        self._vdc_network_pool_name = vdc_network_pool_name

    @property
    def username(self):
        """Gets the username of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The username of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this VCloudCloudSpaceRequest.


        :param username: The username of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The password of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this VCloudCloudSpaceRequest.


        :param password: The password of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def email_address(self):
        """Gets the email_address of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The email_address of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this VCloudCloudSpaceRequest.


        :param email_address: The email_address of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def external_network_name(self):
        """Gets the external_network_name of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The external_network_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._external_network_name

    @external_network_name.setter
    def external_network_name(self, external_network_name):
        """Sets the external_network_name of this VCloudCloudSpaceRequest.


        :param external_network_name: The external_network_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and external_network_name is None:  # noqa: E501
            raise ValueError("Invalid value for `external_network_name`, must not be `None`")  # noqa: E501

        self._external_network_name = external_network_name

    @property
    def maximum_cpu_mhz(self):
        """Gets the maximum_cpu_mhz of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The maximum_cpu_mhz of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_cpu_mhz

    @maximum_cpu_mhz.setter
    def maximum_cpu_mhz(self, maximum_cpu_mhz):
        """Sets the maximum_cpu_mhz of this VCloudCloudSpaceRequest.


        :param maximum_cpu_mhz: The maximum_cpu_mhz of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and maximum_cpu_mhz is None:  # noqa: E501
            raise ValueError("Invalid value for `maximum_cpu_mhz`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                maximum_cpu_mhz is not None and maximum_cpu_mhz < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_cpu_mhz`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_cpu_mhz = maximum_cpu_mhz

    @property
    def local_catalog_name(self):
        """Gets the local_catalog_name of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The local_catalog_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_catalog_name

    @local_catalog_name.setter
    def local_catalog_name(self, local_catalog_name):
        """Sets the local_catalog_name of this VCloudCloudSpaceRequest.


        :param local_catalog_name: The local_catalog_name of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._local_catalog_name = local_catalog_name

    @property
    def vdc_network_quota(self):
        """Gets the vdc_network_quota of this VCloudCloudSpaceRequest.  # noqa: E501


        :return: The vdc_network_quota of this VCloudCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._vdc_network_quota

    @vdc_network_quota.setter
    def vdc_network_quota(self, vdc_network_quota):
        """Sets the vdc_network_quota of this VCloudCloudSpaceRequest.


        :param vdc_network_quota: The vdc_network_quota of this VCloudCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and vdc_network_quota is None:  # noqa: E501
            raise ValueError("Invalid value for `vdc_network_quota`, must not be `None`")  # noqa: E501

        self._vdc_network_quota = vdc_network_quota

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
        if not isinstance(other, VCloudCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VCloudCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
