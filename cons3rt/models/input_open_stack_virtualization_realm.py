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


class InputOpenStackVirtualizationRealm(object):
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
        'access_point': 'str',
        'account_id': 'str',
        'cidr': 'str',
        'default_windows_domain_name': 'str',
        'description': 'str',
        'id': 'int',
        'local_storage_name': 'str',
        'maximum_num_cpus': 'int',
        'maximum_num_gpus': 'int',
        'maximum_ram_in_megabytes': 'int',
        'maximum_storage_in_megabytes': 'int',
        'maximum_virtual_machines': 'int',
        'name': 'str',
        'password': 'str',
        'power_on_delay_base': 'int',
        'power_on_initial_delay_base': 'int',
        'power_on_minimum_delay': 'int',
        'remote_access_config': 'RemoteAccessConfig',
        'state': 'str',
        'username': 'str',
        'zone_count': 'int'
    }

    attribute_map = {
        'virtualization_realm_type': 'virtualizationRealmType',
        'access_point': 'accessPoint',
        'account_id': 'accountId',
        'cidr': 'cidr',
        'default_windows_domain_name': 'defaultWindowsDomainName',
        'description': 'description',
        'id': 'id',
        'local_storage_name': 'localStorageName',
        'maximum_num_cpus': 'maximumNumCpus',
        'maximum_num_gpus': 'maximumNumGpus',
        'maximum_ram_in_megabytes': 'maximumRamInMegabytes',
        'maximum_storage_in_megabytes': 'maximumStorageInMegabytes',
        'maximum_virtual_machines': 'maximumVirtualMachines',
        'name': 'name',
        'password': 'password',
        'power_on_delay_base': 'powerOnDelayBase',
        'power_on_initial_delay_base': 'powerOnInitialDelayBase',
        'power_on_minimum_delay': 'powerOnMinimumDelay',
        'remote_access_config': 'remoteAccessConfig',
        'state': 'state',
        'username': 'username',
        'zone_count': 'zoneCount'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, virtualization_realm_type=None, access_point=None, account_id=None, cidr=None, default_windows_domain_name=None, description=None, id=None, local_storage_name=None, maximum_num_cpus=None, maximum_num_gpus=None, maximum_ram_in_megabytes=None, maximum_storage_in_megabytes=None, maximum_virtual_machines=None, name=None, password=None, power_on_delay_base=None, power_on_initial_delay_base=None, power_on_minimum_delay=None, remote_access_config=None, state=None, username=None, zone_count=None, local_vars_configuration=None):  # noqa: E501
        """InputOpenStackVirtualizationRealm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._virtualization_realm_type = None
        self._access_point = None
        self._account_id = None
        self._cidr = None
        self._default_windows_domain_name = None
        self._description = None
        self._id = None
        self._local_storage_name = None
        self._maximum_num_cpus = None
        self._maximum_num_gpus = None
        self._maximum_ram_in_megabytes = None
        self._maximum_storage_in_megabytes = None
        self._maximum_virtual_machines = None
        self._name = None
        self._password = None
        self._power_on_delay_base = None
        self._power_on_initial_delay_base = None
        self._power_on_minimum_delay = None
        self._remote_access_config = None
        self._state = None
        self._username = None
        self._zone_count = None
        self.discriminator = 'virtualization_realm_type'

        if virtualization_realm_type is not None:
            self.virtualization_realm_type = virtualization_realm_type
        if access_point is not None:
            self.access_point = access_point
        self.account_id = account_id
        self.cidr = cidr
        if default_windows_domain_name is not None:
            self.default_windows_domain_name = default_windows_domain_name
        self.description = description
        if id is not None:
            self.id = id
        if local_storage_name is not None:
            self.local_storage_name = local_storage_name
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
        self.name = name
        self.password = password
        if power_on_delay_base is not None:
            self.power_on_delay_base = power_on_delay_base
        if power_on_initial_delay_base is not None:
            self.power_on_initial_delay_base = power_on_initial_delay_base
        if power_on_minimum_delay is not None:
            self.power_on_minimum_delay = power_on_minimum_delay
        if remote_access_config is not None:
            self.remote_access_config = remote_access_config
        if state is not None:
            self.state = state
        self.username = username
        if zone_count is not None:
            self.zone_count = zone_count

    @property
    def virtualization_realm_type(self):
        """Gets the virtualization_realm_type of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The virtualization_realm_type of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._virtualization_realm_type

    @virtualization_realm_type.setter
    def virtualization_realm_type(self, virtualization_realm_type):
        """Sets the virtualization_realm_type of this InputOpenStackVirtualizationRealm.


        :param virtualization_realm_type: The virtualization_realm_type of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """
        allowed_values = ["Amazon", "Azure", "CloudStack", "Mock", "OpenStack", "VCloud"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and virtualization_realm_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `virtualization_realm_type` ({0}), must be one of {1}"  # noqa: E501
                .format(virtualization_realm_type, allowed_values)
            )

        self._virtualization_realm_type = virtualization_realm_type

    @property
    def access_point(self):
        """Gets the access_point of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The access_point of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        """Sets the access_point of this InputOpenStackVirtualizationRealm.


        :param access_point: The access_point of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._access_point = access_point

    @property
    def account_id(self):
        """Gets the account_id of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The account_id of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this InputOpenStackVirtualizationRealm.


        :param account_id: The account_id of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def cidr(self):
        """Gets the cidr of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The cidr of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this InputOpenStackVirtualizationRealm.


        :param cidr: The cidr of this InputOpenStackVirtualizationRealm.  # noqa: E501
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
    def default_windows_domain_name(self):
        """Gets the default_windows_domain_name of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The default_windows_domain_name of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._default_windows_domain_name

    @default_windows_domain_name.setter
    def default_windows_domain_name(self, default_windows_domain_name):
        """Sets the default_windows_domain_name of this InputOpenStackVirtualizationRealm.


        :param default_windows_domain_name: The default_windows_domain_name of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._default_windows_domain_name = default_windows_domain_name

    @property
    def description(self):
        """Gets the description of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The description of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InputOpenStackVirtualizationRealm.


        :param description: The description of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The id of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InputOpenStackVirtualizationRealm.


        :param id: The id of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def local_storage_name(self):
        """Gets the local_storage_name of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The local_storage_name of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._local_storage_name

    @local_storage_name.setter
    def local_storage_name(self, local_storage_name):
        """Sets the local_storage_name of this InputOpenStackVirtualizationRealm.


        :param local_storage_name: The local_storage_name of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._local_storage_name = local_storage_name

    @property
    def maximum_num_cpus(self):
        """Gets the maximum_num_cpus of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The maximum_num_cpus of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_num_cpus

    @maximum_num_cpus.setter
    def maximum_num_cpus(self, maximum_num_cpus):
        """Sets the maximum_num_cpus of this InputOpenStackVirtualizationRealm.


        :param maximum_num_cpus: The maximum_num_cpus of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_num_cpus is not None and maximum_num_cpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_num_cpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_num_cpus = maximum_num_cpus

    @property
    def maximum_num_gpus(self):
        """Gets the maximum_num_gpus of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The maximum_num_gpus of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_num_gpus

    @maximum_num_gpus.setter
    def maximum_num_gpus(self, maximum_num_gpus):
        """Sets the maximum_num_gpus of this InputOpenStackVirtualizationRealm.


        :param maximum_num_gpus: The maximum_num_gpus of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_num_gpus is not None and maximum_num_gpus < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_num_gpus`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_num_gpus = maximum_num_gpus

    @property
    def maximum_ram_in_megabytes(self):
        """Gets the maximum_ram_in_megabytes of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The maximum_ram_in_megabytes of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_ram_in_megabytes

    @maximum_ram_in_megabytes.setter
    def maximum_ram_in_megabytes(self, maximum_ram_in_megabytes):
        """Sets the maximum_ram_in_megabytes of this InputOpenStackVirtualizationRealm.


        :param maximum_ram_in_megabytes: The maximum_ram_in_megabytes of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_ram_in_megabytes is not None and maximum_ram_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_ram_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_ram_in_megabytes = maximum_ram_in_megabytes

    @property
    def maximum_storage_in_megabytes(self):
        """Gets the maximum_storage_in_megabytes of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The maximum_storage_in_megabytes of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_storage_in_megabytes

    @maximum_storage_in_megabytes.setter
    def maximum_storage_in_megabytes(self, maximum_storage_in_megabytes):
        """Sets the maximum_storage_in_megabytes of this InputOpenStackVirtualizationRealm.


        :param maximum_storage_in_megabytes: The maximum_storage_in_megabytes of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_storage_in_megabytes is not None and maximum_storage_in_megabytes < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_storage_in_megabytes`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_storage_in_megabytes = maximum_storage_in_megabytes

    @property
    def maximum_virtual_machines(self):
        """Gets the maximum_virtual_machines of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The maximum_virtual_machines of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._maximum_virtual_machines

    @maximum_virtual_machines.setter
    def maximum_virtual_machines(self, maximum_virtual_machines):
        """Sets the maximum_virtual_machines of this InputOpenStackVirtualizationRealm.


        :param maximum_virtual_machines: The maximum_virtual_machines of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                maximum_virtual_machines is not None and maximum_virtual_machines < 0):  # noqa: E501
            raise ValueError("Invalid value for `maximum_virtual_machines`, must be a value greater than or equal to `0`")  # noqa: E501

        self._maximum_virtual_machines = maximum_virtual_machines

    @property
    def name(self):
        """Gets the name of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The name of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputOpenStackVirtualizationRealm.


        :param name: The name of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The password of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this InputOpenStackVirtualizationRealm.


        :param password: The password of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def power_on_delay_base(self):
        """Gets the power_on_delay_base of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The power_on_delay_base of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._power_on_delay_base

    @power_on_delay_base.setter
    def power_on_delay_base(self, power_on_delay_base):
        """Sets the power_on_delay_base of this InputOpenStackVirtualizationRealm.


        :param power_on_delay_base: The power_on_delay_base of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._power_on_delay_base = power_on_delay_base

    @property
    def power_on_initial_delay_base(self):
        """Gets the power_on_initial_delay_base of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The power_on_initial_delay_base of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._power_on_initial_delay_base

    @power_on_initial_delay_base.setter
    def power_on_initial_delay_base(self, power_on_initial_delay_base):
        """Sets the power_on_initial_delay_base of this InputOpenStackVirtualizationRealm.


        :param power_on_initial_delay_base: The power_on_initial_delay_base of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._power_on_initial_delay_base = power_on_initial_delay_base

    @property
    def power_on_minimum_delay(self):
        """Gets the power_on_minimum_delay of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The power_on_minimum_delay of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._power_on_minimum_delay

    @power_on_minimum_delay.setter
    def power_on_minimum_delay(self, power_on_minimum_delay):
        """Sets the power_on_minimum_delay of this InputOpenStackVirtualizationRealm.


        :param power_on_minimum_delay: The power_on_minimum_delay of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                power_on_minimum_delay is not None and power_on_minimum_delay < 0):  # noqa: E501
            raise ValueError("Invalid value for `power_on_minimum_delay`, must be a value greater than or equal to `0`")  # noqa: E501

        self._power_on_minimum_delay = power_on_minimum_delay

    @property
    def remote_access_config(self):
        """Gets the remote_access_config of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The remote_access_config of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: RemoteAccessConfig
        """
        return self._remote_access_config

    @remote_access_config.setter
    def remote_access_config(self, remote_access_config):
        """Sets the remote_access_config of this InputOpenStackVirtualizationRealm.


        :param remote_access_config: The remote_access_config of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: RemoteAccessConfig
        """

        self._remote_access_config = remote_access_config

    @property
    def state(self):
        """Gets the state of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The state of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InputOpenStackVirtualizationRealm.


        :param state: The state of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "ENTERING_MAINTENANCE", "INACTIVE", "MAINTENANCE", "PENDING", "REQUESTED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def username(self):
        """Gets the username of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The username of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InputOpenStackVirtualizationRealm.


        :param username: The username of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def zone_count(self):
        """Gets the zone_count of this InputOpenStackVirtualizationRealm.  # noqa: E501


        :return: The zone_count of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._zone_count

    @zone_count.setter
    def zone_count(self, zone_count):
        """Sets the zone_count of this InputOpenStackVirtualizationRealm.


        :param zone_count: The zone_count of this InputOpenStackVirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._zone_count = zone_count

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
        if not isinstance(other, InputOpenStackVirtualizationRealm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputOpenStackVirtualizationRealm):
            return True

        return self.to_dict() != other.to_dict()
