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


class MultipartFormDataInput(object):
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
        'form_data': 'dict(str, InputPart)',
        'form_data_map': 'dict(str, list[InputPart])',
        'parts': 'list[InputPart]',
        'preamble': 'str'
    }

    attribute_map = {
        'form_data': 'formData',
        'form_data_map': 'formDataMap',
        'parts': 'parts',
        'preamble': 'preamble'
    }

    def __init__(self, form_data=None, form_data_map=None, parts=None, preamble=None, local_vars_configuration=None):  # noqa: E501
        """MultipartFormDataInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._form_data = None
        self._form_data_map = None
        self._parts = None
        self._preamble = None
        self.discriminator = None

        if form_data is not None:
            self.form_data = form_data
        if form_data_map is not None:
            self.form_data_map = form_data_map
        if parts is not None:
            self.parts = parts
        if preamble is not None:
            self.preamble = preamble

    @property
    def form_data(self):
        """Gets the form_data of this MultipartFormDataInput.  # noqa: E501


        :return: The form_data of this MultipartFormDataInput.  # noqa: E501
        :rtype: dict(str, InputPart)
        """
        return self._form_data

    @form_data.setter
    def form_data(self, form_data):
        """Sets the form_data of this MultipartFormDataInput.


        :param form_data: The form_data of this MultipartFormDataInput.  # noqa: E501
        :type: dict(str, InputPart)
        """

        self._form_data = form_data

    @property
    def form_data_map(self):
        """Gets the form_data_map of this MultipartFormDataInput.  # noqa: E501


        :return: The form_data_map of this MultipartFormDataInput.  # noqa: E501
        :rtype: dict(str, list[InputPart])
        """
        return self._form_data_map

    @form_data_map.setter
    def form_data_map(self, form_data_map):
        """Sets the form_data_map of this MultipartFormDataInput.


        :param form_data_map: The form_data_map of this MultipartFormDataInput.  # noqa: E501
        :type: dict(str, list[InputPart])
        """

        self._form_data_map = form_data_map

    @property
    def parts(self):
        """Gets the parts of this MultipartFormDataInput.  # noqa: E501


        :return: The parts of this MultipartFormDataInput.  # noqa: E501
        :rtype: list[InputPart]
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this MultipartFormDataInput.


        :param parts: The parts of this MultipartFormDataInput.  # noqa: E501
        :type: list[InputPart]
        """

        self._parts = parts

    @property
    def preamble(self):
        """Gets the preamble of this MultipartFormDataInput.  # noqa: E501


        :return: The preamble of this MultipartFormDataInput.  # noqa: E501
        :rtype: str
        """
        return self._preamble

    @preamble.setter
    def preamble(self, preamble):
        """Sets the preamble of this MultipartFormDataInput.


        :param preamble: The preamble of this MultipartFormDataInput.  # noqa: E501
        :type: str
        """

        self._preamble = preamble

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
        if not isinstance(other, MultipartFormDataInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultipartFormDataInput):
            return True

        return self.to_dict() != other.to_dict()
