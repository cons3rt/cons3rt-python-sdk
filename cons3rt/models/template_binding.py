# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class TemplateBinding(object):
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
        'virtualization_realm_templates': 'list[MinimalCons3rtTemplateData]',
        'system_role': 'str'
    }

    attribute_map = {
        'virtualization_realm_templates': 'virtualizationRealmTemplates',
        'system_role': 'systemRole'
    }

    def __init__(self, virtualization_realm_templates=None, system_role=None, local_vars_configuration=None):  # noqa: E501
        """TemplateBinding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._virtualization_realm_templates = None
        self._system_role = None
        self.discriminator = None

        self.virtualization_realm_templates = virtualization_realm_templates
        self.system_role = system_role

    @property
    def virtualization_realm_templates(self):
        """Gets the virtualization_realm_templates of this TemplateBinding.  # noqa: E501


        :return: The virtualization_realm_templates of this TemplateBinding.  # noqa: E501
        :rtype: list[MinimalCons3rtTemplateData]
        """
        return self._virtualization_realm_templates

    @virtualization_realm_templates.setter
    def virtualization_realm_templates(self, virtualization_realm_templates):
        """Sets the virtualization_realm_templates of this TemplateBinding.


        :param virtualization_realm_templates: The virtualization_realm_templates of this TemplateBinding.  # noqa: E501
        :type: list[MinimalCons3rtTemplateData]
        """
        if self.local_vars_configuration.client_side_validation and virtualization_realm_templates is None:  # noqa: E501
            raise ValueError("Invalid value for `virtualization_realm_templates`, must not be `None`")  # noqa: E501

        self._virtualization_realm_templates = virtualization_realm_templates

    @property
    def system_role(self):
        """Gets the system_role of this TemplateBinding.  # noqa: E501


        :return: The system_role of this TemplateBinding.  # noqa: E501
        :rtype: str
        """
        return self._system_role

    @system_role.setter
    def system_role(self, system_role):
        """Sets the system_role of this TemplateBinding.


        :param system_role: The system_role of this TemplateBinding.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and system_role is None:  # noqa: E501
            raise ValueError("Invalid value for `system_role`, must not be `None`")  # noqa: E501

        self._system_role = system_role

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
        if not isinstance(other, TemplateBinding):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateBinding):
            return True

        return self.to_dict() != other.to_dict()
