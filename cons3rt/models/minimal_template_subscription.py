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


class MinimalTemplateSubscription(object):
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
        'id': 'int',
        'state': 'str',
        'template_registration': 'MinimalTemplateRegistration'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'template_registration': 'templateRegistration'
    }

    def __init__(self, id=None, state=None, template_registration=None, local_vars_configuration=None):  # noqa: E501
        """MinimalTemplateSubscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._state = None
        self._template_registration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if state is not None:
            self.state = state
        if template_registration is not None:
            self.template_registration = template_registration

    @property
    def id(self):
        """Gets the id of this MinimalTemplateSubscription.  # noqa: E501


        :return: The id of this MinimalTemplateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalTemplateSubscription.


        :param id: The id of this MinimalTemplateSubscription.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this MinimalTemplateSubscription.  # noqa: E501


        :return: The state of this MinimalTemplateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this MinimalTemplateSubscription.


        :param state: The state of this MinimalTemplateSubscription.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_DEVELOPMENT", "CERTIFIED", "DEPRECATED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def template_registration(self):
        """Gets the template_registration of this MinimalTemplateSubscription.  # noqa: E501


        :return: The template_registration of this MinimalTemplateSubscription.  # noqa: E501
        :rtype: MinimalTemplateRegistration
        """
        return self._template_registration

    @template_registration.setter
    def template_registration(self, template_registration):
        """Sets the template_registration of this MinimalTemplateSubscription.


        :param template_registration: The template_registration of this MinimalTemplateSubscription.  # noqa: E501
        :type: MinimalTemplateRegistration
        """

        self._template_registration = template_registration

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
        if not isinstance(other, MinimalTemplateSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalTemplateSubscription):
            return True

        return self.to_dict() != other.to_dict()
