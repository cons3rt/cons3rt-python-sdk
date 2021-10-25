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


class MinimalCons3rtTemplateData(object):
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
        'display_name': 'str',
        'operating_system': 'str',
        'virt_realm_id': 'int',
        'virt_realm_template_name': 'str',
        'template_registration': 'MinimalTemplateRegistration'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'operating_system': 'operatingSystem',
        'virt_realm_id': 'virtRealmId',
        'virt_realm_template_name': 'virtRealmTemplateName',
        'template_registration': 'templateRegistration'
    }

    def __init__(self, id=None, display_name=None, operating_system=None, virt_realm_id=None, virt_realm_template_name=None, template_registration=None, local_vars_configuration=None):  # noqa: E501
        """MinimalCons3rtTemplateData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._operating_system = None
        self._virt_realm_id = None
        self._virt_realm_template_name = None
        self._template_registration = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if operating_system is not None:
            self.operating_system = operating_system
        if virt_realm_id is not None:
            self.virt_realm_id = virt_realm_id
        self.virt_realm_template_name = virt_realm_template_name
        if template_registration is not None:
            self.template_registration = template_registration

    @property
    def id(self):
        """Gets the id of this MinimalCons3rtTemplateData.  # noqa: E501


        :return: The id of this MinimalCons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MinimalCons3rtTemplateData.


        :param id: The id of this MinimalCons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this MinimalCons3rtTemplateData.  # noqa: E501


        :return: The display_name of this MinimalCons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MinimalCons3rtTemplateData.


        :param display_name: The display_name of this MinimalCons3rtTemplateData.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def operating_system(self):
        """Gets the operating_system of this MinimalCons3rtTemplateData.  # noqa: E501


        :return: The operating_system of this MinimalCons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this MinimalCons3rtTemplateData.


        :param operating_system: The operating_system of this MinimalCons3rtTemplateData.  # noqa: E501
        :type: str
        """
        allowed_values = ["AMAZON_LINUX_2_LATEST_X64", "AMAZON_LINUX_LATEST_X64", "CENTOS_6_X64", "CENTOS_6_X86", "CENTOS_7_X64", "CENTOS_8_X64", "CORE_OS_1221_X64", "F5_BIGIP_X64", "FEDORA_23_X64", "FORTISIEM", "GENERIC_LINUX_X64", "GENERIC_WINDOWS_X64", "KALI_ROLLING_X64", "ORACLE_LINUX_6_X64", "ORACLE_LINUX_7_X64", "ORACLE_LINUX_8_X64", "OS_X_10", "OS_X_11", "PALO_ALTO_NETWORKS_PAN_OS_X64", "RASPBIAN", "RHEL_5_X64", "RHEL_5_X86", "RHEL_6_X64", "RHEL_6_X86", "RHEL_7_ATOMIC_HOST", "RHEL_7_PPCLE", "RHEL_7_X64", "RHEL_8_X64", "SOLARIS_11_X64", "UBUNTU_12_X64", "UBUNTU_14_X64", "UBUNTU_16_X64", "UBUNTU_18_X64", "UBUNTU_20_X64", "UBUNTU_CORE", "VYOS_1_1_X64", "VYOS_1_2_X64", "VYOS_1_3_X64", "VYOS_ROLLING_X64", "WINDOWS_10_X64", "WINDOWS_7_X64", "WINDOWS_7_X86", "WINDOWS_8_X64", "WINDOWS_SERVER_2008_R2_X64", "WINDOWS_SERVER_2008_X64", "WINDOWS_SERVER_2012_R2_X64", "WINDOWS_SERVER_2012_X64", "WINDOWS_SERVER_2016_X64", "WINDOWS_SERVER_2019_X64", "WINDOWS_SERVER_2019_CORE_X64", "WINDOWS_XP_X86"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and operating_system not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `operating_system` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system, allowed_values)
            )

        self._operating_system = operating_system

    @property
    def virt_realm_id(self):
        """Gets the virt_realm_id of this MinimalCons3rtTemplateData.  # noqa: E501


        :return: The virt_realm_id of this MinimalCons3rtTemplateData.  # noqa: E501
        :rtype: int
        """
        return self._virt_realm_id

    @virt_realm_id.setter
    def virt_realm_id(self, virt_realm_id):
        """Sets the virt_realm_id of this MinimalCons3rtTemplateData.


        :param virt_realm_id: The virt_realm_id of this MinimalCons3rtTemplateData.  # noqa: E501
        :type: int
        """

        self._virt_realm_id = virt_realm_id

    @property
    def virt_realm_template_name(self):
        """Gets the virt_realm_template_name of this MinimalCons3rtTemplateData.  # noqa: E501


        :return: The virt_realm_template_name of this MinimalCons3rtTemplateData.  # noqa: E501
        :rtype: str
        """
        return self._virt_realm_template_name

    @virt_realm_template_name.setter
    def virt_realm_template_name(self, virt_realm_template_name):
        """Sets the virt_realm_template_name of this MinimalCons3rtTemplateData.


        :param virt_realm_template_name: The virt_realm_template_name of this MinimalCons3rtTemplateData.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and virt_realm_template_name is None:  # noqa: E501
            raise ValueError("Invalid value for `virt_realm_template_name`, must not be `None`")  # noqa: E501

        self._virt_realm_template_name = virt_realm_template_name

    @property
    def template_registration(self):
        """Gets the template_registration of this MinimalCons3rtTemplateData.  # noqa: E501


        :return: The template_registration of this MinimalCons3rtTemplateData.  # noqa: E501
        :rtype: MinimalTemplateRegistration
        """
        return self._template_registration

    @template_registration.setter
    def template_registration(self, template_registration):
        """Sets the template_registration of this MinimalCons3rtTemplateData.


        :param template_registration: The template_registration of this MinimalCons3rtTemplateData.  # noqa: E501
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
        if not isinstance(other, MinimalCons3rtTemplateData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MinimalCons3rtTemplateData):
            return True

        return self.to_dict() != other.to_dict()
