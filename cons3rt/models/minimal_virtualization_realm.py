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


class MinimalVirtualizationRealm(object):
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
        'name': 'str',
        'state': 'str'
    }

    attribute_map = {
        'virtualization_realm_type': 'virtualizationRealmType',
        'id': 'id',
        'name': 'name',
        'state': 'state'
    }

    def __init__(self, virtualization_realm_type=None, id=None, name=None, state=None, local_vars_configuration=None):  # noqa: E501
        """MinimalVirtualizationRealm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._virtualization_realm_type = None
        self._id = None
        self._name = None
        self._state = None
        self.discriminator = None

        if virtualization_realm_type is not None:
            self.virtualization_realm_type = virtualization_realm_type
        self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state

    @property
    def virtualization_realm_type(self):
        """Gets the virtualization_realm_type of this MinimalVirtualizationRealm.  # noqa: E501


        :return: The virtualization_realm_type of this MinimalVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._virtualization_realm_type

    @virtualization_realm_type.setter
    def virtualization_realm_type(self, virtualization_realm_type):
        """Sets the virtualization_realm_type of this MinimalVirtualizationRealm.


        :param virtualization_realm_type: The virtualization_realm_type of this MinimalVirtualizationRealm.  # noqa: E501
        :type: str
        """
        allowed_values = ["Amazon", "Azure", "Mock", "OpenStack", "VCloudRest"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and virtualization_realm_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `virtualization_realm_type` ({0}), must be one of {1}"  # noqa: E501
                .format(virtualization_realm_type, allowed_values)
            )

        self._virtualization_realm_type = virtualization_realm_type

    @property
    def id(self):
        """Gets the id of this MinimalVirtualizationRealm.  # noqa: E501


        :return: The id of this MinimalVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalVirtualizationRealm.


        :param id: The id of this MinimalVirtualizationRealm.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this MinimalVirtualizationRealm.  # noqa: E501


        :return: The name of this MinimalVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MinimalVirtualizationRealm.


        :param name: The name of this MinimalVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this MinimalVirtualizationRealm.  # noqa: E501


        :return: The state of this MinimalVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MinimalVirtualizationRealm.


        :param state: The state of this MinimalVirtualizationRealm.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "ENTERING_MAINTENANCE", "INACTIVE", "MAINTENANCE", "PENDING", "REQUESTED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

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
        if not isinstance(other, MinimalVirtualizationRealm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalVirtualizationRealm):
            return True

        return self.to_dict() != other.to_dict()
