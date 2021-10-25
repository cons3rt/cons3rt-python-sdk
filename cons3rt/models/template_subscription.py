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


class TemplateSubscription(object):
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
        'max_num_cpus': 'int',
        'max_ram_in_megabytes': 'int',
        'state': 'str',
        'subscribing_virtualization_realm': 'VirtualizationRealm',
        'template_registration': 'TemplateRegistration',
        'template_uuid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'max_num_cpus': 'maxNumCpus',
        'max_ram_in_megabytes': 'maxRamInMegabytes',
        'state': 'state',
        'subscribing_virtualization_realm': 'subscribingVirtualizationRealm',
        'template_registration': 'templateRegistration',
        'template_uuid': 'templateUuid'
    }

    def __init__(self, id=None, max_num_cpus=None, max_ram_in_megabytes=None, state=None, subscribing_virtualization_realm=None, template_registration=None, template_uuid=None, local_vars_configuration=None):  # noqa: E501
        """TemplateSubscription - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._max_num_cpus = None
        self._max_ram_in_megabytes = None
        self._state = None
        self._subscribing_virtualization_realm = None
        self._template_registration = None
        self._template_uuid = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if max_num_cpus is not None:
            self.max_num_cpus = max_num_cpus
        if max_ram_in_megabytes is not None:
            self.max_ram_in_megabytes = max_ram_in_megabytes
        if state is not None:
            self.state = state
        if subscribing_virtualization_realm is not None:
            self.subscribing_virtualization_realm = subscribing_virtualization_realm
        if template_registration is not None:
            self.template_registration = template_registration
        if template_uuid is not None:
            self.template_uuid = template_uuid

    @property
    def id(self):
        """Gets the id of this TemplateSubscription.  # noqa: E501


        :return: The id of this TemplateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateSubscription.


        :param id: The id of this TemplateSubscription.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def max_num_cpus(self):
        """Gets the max_num_cpus of this TemplateSubscription.  # noqa: E501


        :return: The max_num_cpus of this TemplateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._max_num_cpus

    @max_num_cpus.setter
    def max_num_cpus(self, max_num_cpus):
        """Sets the max_num_cpus of this TemplateSubscription.


        :param max_num_cpus: The max_num_cpus of this TemplateSubscription.  # noqa: E501
        :type: int
        """

        self._max_num_cpus = max_num_cpus

    @property
    def max_ram_in_megabytes(self):
        """Gets the max_ram_in_megabytes of this TemplateSubscription.  # noqa: E501


        :return: The max_ram_in_megabytes of this TemplateSubscription.  # noqa: E501
        :rtype: int
        """
        return self._max_ram_in_megabytes

    @max_ram_in_megabytes.setter
    def max_ram_in_megabytes(self, max_ram_in_megabytes):
        """Sets the max_ram_in_megabytes of this TemplateSubscription.


        :param max_ram_in_megabytes: The max_ram_in_megabytes of this TemplateSubscription.  # noqa: E501
        :type: int
        """

        self._max_ram_in_megabytes = max_ram_in_megabytes

    @property
    def state(self):
        """Gets the state of this TemplateSubscription.  # noqa: E501


        :return: The state of this TemplateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TemplateSubscription.


        :param state: The state of this TemplateSubscription.  # noqa: E501
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
    def subscribing_virtualization_realm(self):
        """Gets the subscribing_virtualization_realm of this TemplateSubscription.  # noqa: E501


        :return: The subscribing_virtualization_realm of this TemplateSubscription.  # noqa: E501
        :rtype: VirtualizationRealm
        """
        return self._subscribing_virtualization_realm

    @subscribing_virtualization_realm.setter
    def subscribing_virtualization_realm(self, subscribing_virtualization_realm):
        """Sets the subscribing_virtualization_realm of this TemplateSubscription.


        :param subscribing_virtualization_realm: The subscribing_virtualization_realm of this TemplateSubscription.  # noqa: E501
        :type: VirtualizationRealm
        """

        self._subscribing_virtualization_realm = subscribing_virtualization_realm

    @property
    def template_registration(self):
        """Gets the template_registration of this TemplateSubscription.  # noqa: E501


        :return: The template_registration of this TemplateSubscription.  # noqa: E501
        :rtype: TemplateRegistration
        """
        return self._template_registration

    @template_registration.setter
    def template_registration(self, template_registration):
        """Sets the template_registration of this TemplateSubscription.


        :param template_registration: The template_registration of this TemplateSubscription.  # noqa: E501
        :type: TemplateRegistration
        """

        self._template_registration = template_registration

    @property
    def template_uuid(self):
        """Gets the template_uuid of this TemplateSubscription.  # noqa: E501


        :return: The template_uuid of this TemplateSubscription.  # noqa: E501
        :rtype: str
        """
        return self._template_uuid

    @template_uuid.setter
    def template_uuid(self, template_uuid):
        """Sets the template_uuid of this TemplateSubscription.


        :param template_uuid: The template_uuid of this TemplateSubscription.  # noqa: E501
        :type: str
        """

        self._template_uuid = template_uuid

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
        if not isinstance(other, TemplateSubscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateSubscription):
            return True

        return self.to_dict() != other.to_dict()
