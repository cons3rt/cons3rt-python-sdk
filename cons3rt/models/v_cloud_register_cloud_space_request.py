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


class VCloudRegisterCloudSpaceRequest(object):
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
        'virtualization_realm_type': 'str',
        'name': 'str',
        'description': 'str',
        'access_point': 'str',
        'active_after_registration': 'bool',
        'additional_network_names': 'list[str]',
        'cons3rt_network_name': 'str',
        'maximum_num_cpus': 'int',
        'maximum_num_gpus': 'int',
        'maximum_ram_in_megabytes': 'int',
        'maximum_storage_in_megabytes': 'int',
        'maximum_virtual_machines': 'int',
        'power_on_minimum_delay': 'int',
        'password': 'str',
        'power_on_initial_delay_base': 'int',
        'primary_network_name': 'str',
        'remote_access_config': 'RemoteAccessConfig',
        'username': 'str',
        'local_storage_name': 'str',
        'organization': 'str',
        'organization_vdc': 'str'
    }

    attribute_map = {
        'virtualization_realm_type': 'virtualizationRealmType',
        'name': 'name',
        'description': 'description',
        'access_point': 'accessPoint',
        'active_after_registration': 'activeAfterRegistration',
        'additional_network_names': 'additionalNetworkNames',
        'cons3rt_network_name': 'cons3rtNetworkName',
        'maximum_num_cpus': 'maximumNumCpus',
        'maximum_num_gpus': 'maximumNumGpus',
        'maximum_ram_in_megabytes': 'maximumRamInMegabytes',
        'maximum_storage_in_megabytes': 'maximumStorageInMegabytes',
        'maximum_virtual_machines': 'maximumVirtualMachines',
        'power_on_minimum_delay': 'powerOnMinimumDelay',
        'password': 'password',
        'power_on_initial_delay_base': 'powerOnInitialDelayBase',
        'primary_network_name': 'primaryNetworkName',
        'remote_access_config': 'remoteAccessConfig',
        'username': 'username',
        'local_storage_name': 'localStorageName',
        'organization': 'organization',
        'organization_vdc': 'organizationVdc'
    }

    def __init__(self, virtualization_realm_type=None, name=None, description=None, access_point=None, active_after_registration=None, additional_network_names=None, cons3rt_network_name=None, maximum_num_cpus=None, maximum_num_gpus=None, maximum_ram_in_megabytes=None, maximum_storage_in_megabytes=None, maximum_virtual_machines=None, power_on_minimum_delay=None, password=None, power_on_initial_delay_base=None, primary_network_name=None, remote_access_config=None, username=None, local_storage_name=None, organization=None, organization_vdc=None, local_vars_configuration=None):  # noqa: E501
        """VCloudRegisterCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._virtualization_realm_type = None
        self._name = None
        self._description = None
        self._access_point = None
        self._active_after_registration = None
        self._additional_network_names = None
        self._cons3rt_network_name = None
        self._maximum_num_cpus = None
        self._maximum_num_gpus = None
        self._maximum_ram_in_megabytes = None
        self._maximum_storage_in_megabytes = None
        self._maximum_virtual_machines = None
        self._power_on_minimum_delay = None
        self._password = None
        self._power_on_initial_delay_base = None
        self._primary_network_name = None
        self._remote_access_config = None
        self._username = None
        self._local_storage_name = None
        self._organization = None
        self._organization_vdc = None
        self.discriminator = None

        self.virtualization_realm_type = virtualization_realm_type
        self.name = name
        if description is not None:
            self.description = description
        if access_point is not None:
            self.access_point = access_point
        if active_after_registration is not None:
            self.active_after_registration = active_after_registration
        if additional_network_names is not None:
            self.additional_network_names = additional_network_names
        self.cons3rt_network_name = cons3rt_network_name
        if maximum_num_cpus is not None:
            self.maximum_num_cpus = maximum_num_cpus
        if maximum_num_gpus is not None:
            self.maximum_num_gpus = maximum_num_gpus
        if maximum_ram_in_megabytes is not None:
            self.maximum_ram_in_megabytes = maximum_ram_in_megabytes
        if maximum_storage_in_megabytes is not None:
            self.maximum_storage_in_megabytes = maximum_storage_in_megabytes
        if maximum_virtual_machines is not None:
            self.maximum_virtual_machines = maximum_virtual_machines
        if power_on_minimum_delay is not None:
            self.power_on_minimum_delay = power_on_minimum_delay
        self.password = password
        if power_on_initial_delay_base is not None:
            self.power_on_initial_delay_base = power_on_initial_delay_base
        self.primary_network_name = primary_network_name
        if remote_access_config is not None:
            self.remote_access_config = remote_access_config
        self.username = username
        if local_storage_name is not None:
            self.local_storage_name = local_storage_name
        self.organization = organization
        self.organization_vdc = organization_vdc

    @property
    def virtualization_realm_type(self):
        """Gets the virtualization_realm_type of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The virtualization_realm_type of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._virtualization_realm_type

    @virtualization_realm_type.setter
    def virtualization_realm_type(self, virtualization_realm_type):
        """Sets the virtualization_realm_type of this VCloudRegisterCloudSpaceRequest.


        :param virtualization_realm_type: The virtualization_realm_type of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and virtualization_realm_type is None:  # noqa: E501
            raise ValueError("Invalid value for `virtualization_realm_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Amazon", "Azure", "CloudStack", "Mock", "OpenStack", "VCloud"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and virtualization_realm_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `virtualization_realm_type` ({0}), must be one of {1}"  # noqa: E501
                .format(virtualization_realm_type, allowed_values)
            )

        self._virtualization_realm_type = virtualization_realm_type

    @property
    def name(self):
        """Gets the name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VCloudRegisterCloudSpaceRequest.


        :param name: The name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 25):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `25`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 3):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The description of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VCloudRegisterCloudSpaceRequest.


        :param description: The description of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def access_point(self):
        """Gets the access_point of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The access_point of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        """Sets the access_point of this VCloudRegisterCloudSpaceRequest.


        :param access_point: The access_point of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                access_point is not None and len(access_point) > 18):
            raise ValueError("Invalid value for `access_point`, length must be less than or equal to `18`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                access_point is not None and len(access_point) < 7):
            raise ValueError("Invalid value for `access_point`, length must be greater than or equal to `7`")  # noqa: E501

        self._access_point = access_point

    @property
    def active_after_registration(self):
        """Gets the active_after_registration of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The active_after_registration of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active_after_registration

    @active_after_registration.setter
    def active_after_registration(self, active_after_registration):
        """Sets the active_after_registration of this VCloudRegisterCloudSpaceRequest.


        :param active_after_registration: The active_after_registration of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: bool
        """

        self._active_after_registration = active_after_registration

    @property
    def additional_network_names(self):
        """Gets the additional_network_names of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The additional_network_names of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_network_names

    @additional_network_names.setter
    def additional_network_names(self, additional_network_names):
        """Sets the additional_network_names of this VCloudRegisterCloudSpaceRequest.


        :param additional_network_names: The additional_network_names of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: list[str]
        """

        self._additional_network_names = additional_network_names

    @property
    def cons3rt_network_name(self):
        """Gets the cons3rt_network_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The cons3rt_network_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._cons3rt_network_name

    @cons3rt_network_name.setter
    def cons3rt_network_name(self, cons3rt_network_name):
        """Sets the cons3rt_network_name of this VCloudRegisterCloudSpaceRequest.


        :param cons3rt_network_name: The cons3rt_network_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and cons3rt_network_name is None:  # noqa: E501
            raise ValueError("Invalid value for `cons3rt_network_name`, must not be `None`")  # noqa: E501

        self._cons3rt_network_name = cons3rt_network_name

    @property
    def maximum_num_cpus(self):
        """Gets the maximum_num_cpus of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The maximum_num_cpus of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_num_cpus

    @maximum_num_cpus.setter
    def maximum_num_cpus(self, maximum_num_cpus):
        """Sets the maximum_num_cpus of this VCloudRegisterCloudSpaceRequest.


        :param maximum_num_cpus: The maximum_num_cpus of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_num_cpus is not None and maximum_num_cpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_num_cpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_num_cpus = maximum_num_cpus

    @property
    def maximum_num_gpus(self):
        """Gets the maximum_num_gpus of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The maximum_num_gpus of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_num_gpus

    @maximum_num_gpus.setter
    def maximum_num_gpus(self, maximum_num_gpus):
        """Sets the maximum_num_gpus of this VCloudRegisterCloudSpaceRequest.


        :param maximum_num_gpus: The maximum_num_gpus of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_num_gpus is not None and maximum_num_gpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_num_gpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_num_gpus = maximum_num_gpus

    @property
    def maximum_ram_in_megabytes(self):
        """Gets the maximum_ram_in_megabytes of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The maximum_ram_in_megabytes of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_ram_in_megabytes

    @maximum_ram_in_megabytes.setter
    def maximum_ram_in_megabytes(self, maximum_ram_in_megabytes):
        """Sets the maximum_ram_in_megabytes of this VCloudRegisterCloudSpaceRequest.


        :param maximum_ram_in_megabytes: The maximum_ram_in_megabytes of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_ram_in_megabytes is not None and maximum_ram_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_ram_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_ram_in_megabytes = maximum_ram_in_megabytes

    @property
    def maximum_storage_in_megabytes(self):
        """Gets the maximum_storage_in_megabytes of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The maximum_storage_in_megabytes of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_storage_in_megabytes

    @maximum_storage_in_megabytes.setter
    def maximum_storage_in_megabytes(self, maximum_storage_in_megabytes):
        """Sets the maximum_storage_in_megabytes of this VCloudRegisterCloudSpaceRequest.


        :param maximum_storage_in_megabytes: The maximum_storage_in_megabytes of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_storage_in_megabytes is not None and maximum_storage_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_storage_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_storage_in_megabytes = maximum_storage_in_megabytes

    @property
    def maximum_virtual_machines(self):
        """Gets the maximum_virtual_machines of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The maximum_virtual_machines of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._maximum_virtual_machines

    @maximum_virtual_machines.setter
    def maximum_virtual_machines(self, maximum_virtual_machines):
        """Sets the maximum_virtual_machines of this VCloudRegisterCloudSpaceRequest.


        :param maximum_virtual_machines: The maximum_virtual_machines of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_virtual_machines is not None and maximum_virtual_machines < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_virtual_machines`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_virtual_machines = maximum_virtual_machines

    @property
    def power_on_minimum_delay(self):
        """Gets the power_on_minimum_delay of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The power_on_minimum_delay of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._power_on_minimum_delay

    @power_on_minimum_delay.setter
    def power_on_minimum_delay(self, power_on_minimum_delay):
        """Sets the power_on_minimum_delay of this VCloudRegisterCloudSpaceRequest.


        :param power_on_minimum_delay: The power_on_minimum_delay of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                power_on_minimum_delay is not None and power_on_minimum_delay < 0):  # noqa: E501
            raise ValueError("Invalid value for `power_on_minimum_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._power_on_minimum_delay = power_on_minimum_delay

    @property
    def password(self):
        """Gets the password of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The password of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this VCloudRegisterCloudSpaceRequest.


        :param password: The password of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def power_on_initial_delay_base(self):
        """Gets the power_on_initial_delay_base of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The power_on_initial_delay_base of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: int
        """
        return self._power_on_initial_delay_base

    @power_on_initial_delay_base.setter
    def power_on_initial_delay_base(self, power_on_initial_delay_base):
        """Sets the power_on_initial_delay_base of this VCloudRegisterCloudSpaceRequest.


        :param power_on_initial_delay_base: The power_on_initial_delay_base of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                power_on_initial_delay_base is not None and power_on_initial_delay_base < 0):  # noqa: E501
            raise ValueError("Invalid value for `power_on_initial_delay_base`, must be a value greater than or equal to `0`")  # noqa: E501

        self._power_on_initial_delay_base = power_on_initial_delay_base

    @property
    def primary_network_name(self):
        """Gets the primary_network_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The primary_network_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._primary_network_name

    @primary_network_name.setter
    def primary_network_name(self, primary_network_name):
        """Sets the primary_network_name of this VCloudRegisterCloudSpaceRequest.


        :param primary_network_name: The primary_network_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and primary_network_name is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_network_name`, must not be `None`")  # noqa: E501

        self._primary_network_name = primary_network_name

    @property
    def remote_access_config(self):
        """Gets the remote_access_config of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The remote_access_config of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: RemoteAccessConfig
        """
        return self._remote_access_config

    @remote_access_config.setter
    def remote_access_config(self, remote_access_config):
        """Sets the remote_access_config of this VCloudRegisterCloudSpaceRequest.


        :param remote_access_config: The remote_access_config of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: RemoteAccessConfig
        """

        self._remote_access_config = remote_access_config

    @property
    def username(self):
        """Gets the username of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The username of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this VCloudRegisterCloudSpaceRequest.


        :param username: The username of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def local_storage_name(self):
        """Gets the local_storage_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The local_storage_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._local_storage_name

    @local_storage_name.setter
    def local_storage_name(self, local_storage_name):
        """Sets the local_storage_name of this VCloudRegisterCloudSpaceRequest.


        :param local_storage_name: The local_storage_name of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """

        self._local_storage_name = local_storage_name

    @property
    def organization(self):
        """Gets the organization of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The organization of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this VCloudRegisterCloudSpaceRequest.


        :param organization: The organization of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and organization is None:  # noqa: E501
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def organization_vdc(self):
        """Gets the organization_vdc of this VCloudRegisterCloudSpaceRequest.  # noqa: E501


        :return: The organization_vdc of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_vdc

    @organization_vdc.setter
    def organization_vdc(self, organization_vdc):
        """Sets the organization_vdc of this VCloudRegisterCloudSpaceRequest.


        :param organization_vdc: The organization_vdc of this VCloudRegisterCloudSpaceRequest.  # noqa: E501
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
        if not isinstance(other, VCloudRegisterCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VCloudRegisterCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
