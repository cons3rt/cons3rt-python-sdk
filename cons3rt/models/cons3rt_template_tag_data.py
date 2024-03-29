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


class Cons3rtTemplateTagData(object):
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
        'cons3rt_site_id': 'str',
        'uuid': 'str',
        'virt_realm_template_name': 'str',
        'registered_in_this_environment': 'bool'
    }

    attribute_map = {
        'cons3rt_site_id': 'cons3rtSiteId',
        'uuid': 'uuid',
        'virt_realm_template_name': 'virtRealmTemplateName',
        'registered_in_this_environment': 'registeredInThisEnvironment'
    }

    def __init__(self, cons3rt_site_id=None, uuid=None, virt_realm_template_name=None, registered_in_this_environment=None, local_vars_configuration=None):  # noqa: E501
        """Cons3rtTemplateTagData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cons3rt_site_id = None
        self._uuid = None
        self._virt_realm_template_name = None
        self._registered_in_this_environment = None
        self.discriminator = None

        if cons3rt_site_id is not None:
            self.cons3rt_site_id = cons3rt_site_id
        if uuid is not None:
            self.uuid = uuid
        if virt_realm_template_name is not None:
            self.virt_realm_template_name = virt_realm_template_name
        if registered_in_this_environment is not None:
            self.registered_in_this_environment = registered_in_this_environment

    @property
    def cons3rt_site_id(self):
        """Gets the cons3rt_site_id of this Cons3rtTemplateTagData.  # noqa: E501


        :return: The cons3rt_site_id of this Cons3rtTemplateTagData.  # noqa: E501
        :rtype: str
        """
        return self._cons3rt_site_id

    @cons3rt_site_id.setter
    def cons3rt_site_id(self, cons3rt_site_id):
        """Sets the cons3rt_site_id of this Cons3rtTemplateTagData.


        :param cons3rt_site_id: The cons3rt_site_id of this Cons3rtTemplateTagData.  # noqa: E501
        :type: str
        """

        self._cons3rt_site_id = cons3rt_site_id

    @property
    def uuid(self):
        """Gets the uuid of this Cons3rtTemplateTagData.  # noqa: E501


        :return: The uuid of this Cons3rtTemplateTagData.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Cons3rtTemplateTagData.


        :param uuid: The uuid of this Cons3rtTemplateTagData.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def virt_realm_template_name(self):
        """Gets the virt_realm_template_name of this Cons3rtTemplateTagData.  # noqa: E501


        :return: The virt_realm_template_name of this Cons3rtTemplateTagData.  # noqa: E501
        :rtype: str
        """
        return self._virt_realm_template_name

    @virt_realm_template_name.setter
    def virt_realm_template_name(self, virt_realm_template_name):
        """Sets the virt_realm_template_name of this Cons3rtTemplateTagData.


        :param virt_realm_template_name: The virt_realm_template_name of this Cons3rtTemplateTagData.  # noqa: E501
        :type: str
        """

        self._virt_realm_template_name = virt_realm_template_name

    @property
    def registered_in_this_environment(self):
        """Gets the registered_in_this_environment of this Cons3rtTemplateTagData.  # noqa: E501


        :return: The registered_in_this_environment of this Cons3rtTemplateTagData.  # noqa: E501
        :rtype: bool
        """
        return self._registered_in_this_environment

    @registered_in_this_environment.setter
    def registered_in_this_environment(self, registered_in_this_environment):
        """Sets the registered_in_this_environment of this Cons3rtTemplateTagData.


        :param registered_in_this_environment: The registered_in_this_environment of this Cons3rtTemplateTagData.  # noqa: E501
        :type: bool
        """

        self._registered_in_this_environment = registered_in_this_environment

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
        if not isinstance(other, Cons3rtTemplateTagData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cons3rtTemplateTagData):
            return True

        return self.to_dict() != other.to_dict()
