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


class TemplateRegistration(object):
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
        'offline': 'bool',
        'registering_virtualization_realm': 'VirtualizationRealm',
        'subscriptions': 'list[TemplateSubscription]',
        'template_data': 'Cons3rtTemplateData',
        'template_uuid': 'str',
        'virt_realms_shared_to': 'list[VirtualizationRealm]'
    }

    attribute_map = {
        'id': 'id',
        'offline': 'offline',
        'registering_virtualization_realm': 'registeringVirtualizationRealm',
        'subscriptions': 'subscriptions',
        'template_data': 'templateData',
        'template_uuid': 'templateUuid',
        'virt_realms_shared_to': 'virtRealmsSharedTo'
    }

    def __init__(self, id=None, offline=None, registering_virtualization_realm=None, subscriptions=None, template_data=None, template_uuid=None, virt_realms_shared_to=None, local_vars_configuration=None):  # noqa: E501
        """TemplateRegistration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._offline = None
        self._registering_virtualization_realm = None
        self._subscriptions = None
        self._template_data = None
        self._template_uuid = None
        self._virt_realms_shared_to = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if offline is not None:
            self.offline = offline
        if registering_virtualization_realm is not None:
            self.registering_virtualization_realm = registering_virtualization_realm
        if subscriptions is not None:
            self.subscriptions = subscriptions
        if template_data is not None:
            self.template_data = template_data
        if template_uuid is not None:
            self.template_uuid = template_uuid
        if virt_realms_shared_to is not None:
            self.virt_realms_shared_to = virt_realms_shared_to

    @property
    def id(self):
        """Gets the id of this TemplateRegistration.  # noqa: E501


        :return: The id of this TemplateRegistration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateRegistration.


        :param id: The id of this TemplateRegistration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def offline(self):
        """Gets the offline of this TemplateRegistration.  # noqa: E501


        :return: The offline of this TemplateRegistration.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this TemplateRegistration.


        :param offline: The offline of this TemplateRegistration.  # noqa: E501
        :type: bool
        """

        self._offline = offline

    @property
    def registering_virtualization_realm(self):
        """Gets the registering_virtualization_realm of this TemplateRegistration.  # noqa: E501


        :return: The registering_virtualization_realm of this TemplateRegistration.  # noqa: E501
        :rtype: VirtualizationRealm
        """
        return self._registering_virtualization_realm

    @registering_virtualization_realm.setter
    def registering_virtualization_realm(self, registering_virtualization_realm):
        """Sets the registering_virtualization_realm of this TemplateRegistration.


        :param registering_virtualization_realm: The registering_virtualization_realm of this TemplateRegistration.  # noqa: E501
        :type: VirtualizationRealm
        """

        self._registering_virtualization_realm = registering_virtualization_realm

    @property
    def subscriptions(self):
        """Gets the subscriptions of this TemplateRegistration.  # noqa: E501


        :return: The subscriptions of this TemplateRegistration.  # noqa: E501
        :rtype: list[TemplateSubscription]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this TemplateRegistration.


        :param subscriptions: The subscriptions of this TemplateRegistration.  # noqa: E501
        :type: list[TemplateSubscription]
        """

        self._subscriptions = subscriptions

    @property
    def template_data(self):
        """Gets the template_data of this TemplateRegistration.  # noqa: E501


        :return: The template_data of this TemplateRegistration.  # noqa: E501
        :rtype: Cons3rtTemplateData
        """
        return self._template_data

    @template_data.setter
    def template_data(self, template_data):
        """Sets the template_data of this TemplateRegistration.


        :param template_data: The template_data of this TemplateRegistration.  # noqa: E501
        :type: Cons3rtTemplateData
        """

        self._template_data = template_data

    @property
    def template_uuid(self):
        """Gets the template_uuid of this TemplateRegistration.  # noqa: E501


        :return: The template_uuid of this TemplateRegistration.  # noqa: E501
        :rtype: str
        """
        return self._template_uuid

    @template_uuid.setter
    def template_uuid(self, template_uuid):
        """Sets the template_uuid of this TemplateRegistration.


        :param template_uuid: The template_uuid of this TemplateRegistration.  # noqa: E501
        :type: str
        """

        self._template_uuid = template_uuid

    @property
    def virt_realms_shared_to(self):
        """Gets the virt_realms_shared_to of this TemplateRegistration.  # noqa: E501


        :return: The virt_realms_shared_to of this TemplateRegistration.  # noqa: E501
        :rtype: list[VirtualizationRealm]
        """
        return self._virt_realms_shared_to

    @virt_realms_shared_to.setter
    def virt_realms_shared_to(self, virt_realms_shared_to):
        """Sets the virt_realms_shared_to of this TemplateRegistration.


        :param virt_realms_shared_to: The virt_realms_shared_to of this TemplateRegistration.  # noqa: E501
        :type: list[VirtualizationRealm]
        """

        self._virt_realms_shared_to = virt_realms_shared_to

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
        if not isinstance(other, TemplateRegistration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateRegistration):
            return True

        return self.to_dict() != other.to_dict()
