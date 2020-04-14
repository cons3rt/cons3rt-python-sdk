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


class InputHostBinding(object):
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
        'system_role': 'str',
        'template_name': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'system_role': 'systemRole',
        'template_name': 'templateName',
        'instance_type': 'instanceType'
    }

    def __init__(self, system_role=None, template_name=None, instance_type=None, local_vars_configuration=None):  # noqa: E501
        """InputHostBinding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._system_role = None
        self._template_name = None
        self._instance_type = None
        self.discriminator = None

        self.system_role = system_role
        self.template_name = template_name
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def system_role(self):
        """Gets the system_role of this InputHostBinding.  # noqa: E501


        :return: The system_role of this InputHostBinding.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this InputHostBinding.


        :param system_role: The system_role of this InputHostBinding.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_role is None:  # noqa: E501
            raise ValueError("Invalid value for `system_role`, must not be `None`")  # noqa: E501

        self._system_role = system_role

    @property
    def template_name(self):
        """Gets the template_name of this InputHostBinding.  # noqa: E501


        :return: The template_name of this InputHostBinding.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this InputHostBinding.


        :param template_name: The template_name of this InputHostBinding.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and template_name is None:  # noqa: E501
            raise ValueError("Invalid value for `template_name`, must not be `None`")  # noqa: E501

        self._template_name = template_name

    @property
    def instance_type(self):
        """Gets the instance_type of this InputHostBinding.  # noqa: E501

        Required for Azure and AWS EC2 Cloudspaces  # noqa: E501

        :return: The instance_type of this InputHostBinding.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this InputHostBinding.

        Required for Azure and AWS EC2 Cloudspaces  # noqa: E501

        :param instance_type: The instance_type of this InputHostBinding.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

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
        if not isinstance(other, InputHostBinding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputHostBinding):
            return True

        return self.to_dict() != other.to_dict()
