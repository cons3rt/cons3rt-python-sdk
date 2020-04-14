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
        'template': 'MinimalCons3rtTemplateData',
        'best_matches': 'list[InstanceType]',
        'matches': 'list[InstanceTypeFamily]'
    }

    attribute_map = {
        'template': 'template',
        'best_matches': 'bestMatches',
        'matches': 'matches'
    }

    def __init__(self, template=None, best_matches=None, matches=None, local_vars_configuration=None):  # noqa: E501
        """TemplateBinding - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._template = None
        self._best_matches = None
        self._matches = None
        self.discriminator = None

        if template is not None:
            self.template = template
        if best_matches is not None:
            self.best_matches = best_matches
        if matches is not None:
            self.matches = matches

    @property
    def template(self):
        """Gets the template of this TemplateBinding.  # noqa: E501


        :return: The template of this TemplateBinding.  # noqa: E501
        :rtype: MinimalCons3rtTemplateData
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this TemplateBinding.


        :param template: The template of this TemplateBinding.  # noqa: E501
        :type: MinimalCons3rtTemplateData
        """

        self._template = template

    @property
    def best_matches(self):
        """Gets the best_matches of this TemplateBinding.  # noqa: E501


        :return: The best_matches of this TemplateBinding.  # noqa: E501
        :rtype: list[InstanceType]
        """
        return self._best_matches

    @best_matches.setter
    def best_matches(self, best_matches):
        """Sets the best_matches of this TemplateBinding.


        :param best_matches: The best_matches of this TemplateBinding.  # noqa: E501
        :type: list[InstanceType]
        """

        self._best_matches = best_matches

    @property
    def matches(self):
        """Gets the matches of this TemplateBinding.  # noqa: E501


        :return: The matches of this TemplateBinding.  # noqa: E501
        :rtype: list[InstanceTypeFamily]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        """Sets the matches of this TemplateBinding.


        :param matches: The matches of this TemplateBinding.  # noqa: E501
        :type: list[InstanceTypeFamily]
        """

        self._matches = matches

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
