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


class InputVRAdminVCloudVirtualizationRealm(object):
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
        'id': 'int',
        'additional_networks': 'list[InputVirtualizationRealmNetwork]',
        'cidr': 'str',
        'cons3rt_network': 'InputVirtualizationRealmNetwork',
        'default_windows_domain_name': 'str',
        'description': 'str',
        'name': 'str'
    }

    attribute_map = {
        'virtualization_realm_type': 'virtualizationRealmType',
        'id': 'id',
        'additional_networks': 'additionalNetworks',
        'cidr': 'cidr',
        'cons3rt_network': 'cons3rtNetwork',
        'default_windows_domain_name': 'defaultWindowsDomainName',
        'description': 'description',
        'name': 'name'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, virtualization_realm_type=None, id=None, additional_networks=None, cidr=None, cons3rt_network=None, default_windows_domain_name=None, description=None, name=None, local_vars_configuration=None):  # noqa: E501
        """InputVRAdminVCloudVirtualizationRealm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._virtualization_realm_type = None
        self._id = None
        self._additional_networks = None
        self._cidr = None
        self._cons3rt_network = None
        self._default_windows_domain_name = None
        self._description = None
        self._name = None
        self.discriminator = 'virtualization_realm_type'

        self.virtualization_realm_type = virtualization_realm_type
        if id is not None:
            self.id = id
        if additional_networks is not None:
            self.additional_networks = additional_networks
        self.cidr = cidr
        if cons3rt_network is not None:
            self.cons3rt_network = cons3rt_network
        if default_windows_domain_name is not None:
            self.default_windows_domain_name = default_windows_domain_name
        self.description = description
        self.name = name

    @property
    def virtualization_realm_type(self):
        """Gets the virtualization_realm_type of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501


        :return: The virtualization_realm_type of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._virtualization_realm_type

    @virtualization_realm_type.setter
    def virtualization_realm_type(self, virtualization_realm_type):
        """Sets the virtualization_realm_type of this InputVRAdminVCloudVirtualizationRealm.


        :param virtualization_realm_type: The virtualization_realm_type of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
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
    def id(self):
        """Gets the id of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501


        :return: The id of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InputVRAdminVCloudVirtualizationRealm.


        :param id: The id of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def additional_networks(self):
        """Gets the additional_networks of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501


        :return: The additional_networks of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :rtype: list[InputVirtualizationRealmNetwork]
        """
        return self._additional_networks

    @additional_networks.setter
    def additional_networks(self, additional_networks):
        """Sets the additional_networks of this InputVRAdminVCloudVirtualizationRealm.


        :param additional_networks: The additional_networks of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :type: list[InputVirtualizationRealmNetwork]
        """

        self._additional_networks = additional_networks

    @property
    def cidr(self):
        """Gets the cidr of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501


        :return: The cidr of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this InputVRAdminVCloudVirtualizationRealm.


        :param cidr: The cidr of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
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
    def cons3rt_network(self):
        """Gets the cons3rt_network of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501


        :return: The cons3rt_network of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :rtype: InputVirtualizationRealmNetwork
        """
        return self._cons3rt_network

    @cons3rt_network.setter
    def cons3rt_network(self, cons3rt_network):
        """Sets the cons3rt_network of this InputVRAdminVCloudVirtualizationRealm.


        :param cons3rt_network: The cons3rt_network of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :type: InputVirtualizationRealmNetwork
        """

        self._cons3rt_network = cons3rt_network

    @property
    def default_windows_domain_name(self):
        """Gets the default_windows_domain_name of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501


        :return: The default_windows_domain_name of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._default_windows_domain_name

    @default_windows_domain_name.setter
    def default_windows_domain_name(self, default_windows_domain_name):
        """Sets the default_windows_domain_name of this InputVRAdminVCloudVirtualizationRealm.


        :param default_windows_domain_name: The default_windows_domain_name of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._default_windows_domain_name = default_windows_domain_name

    @property
    def description(self):
        """Gets the description of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501


        :return: The description of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InputVRAdminVCloudVirtualizationRealm.


        :param description: The description of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def name(self):
        """Gets the name of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501


        :return: The name of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InputVRAdminVCloudVirtualizationRealm.


        :param name: The name of this InputVRAdminVCloudVirtualizationRealm.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, InputVRAdminVCloudVirtualizationRealm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputVRAdminVCloudVirtualizationRealm):
            return True

        return self.to_dict() != other.to_dict()
