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


class FullVirtualServiceAllOf(object):
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
        'base_path': 'str',
        'port_string': 'str',
        'service_image_file': 'str',
        'service_model_file': 'str'
    }

    attribute_map = {
        'base_path': 'basePath',
        'port_string': 'portString',
        'service_image_file': 'serviceImageFile',
        'service_model_file': 'serviceModelFile'
    }

    def __init__(self, base_path=None, port_string=None, service_image_file=None, service_model_file=None, local_vars_configuration=None):  # noqa: E501
        """FullVirtualServiceAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._base_path = None
        self._port_string = None
        self._service_image_file = None
        self._service_model_file = None
        self.discriminator = None

        if base_path is not None:
            self.base_path = base_path
        if port_string is not None:
            self.port_string = port_string
        if service_image_file is not None:
            self.service_image_file = service_image_file
        if service_model_file is not None:
            self.service_model_file = service_model_file

    @property
    def base_path(self):
        """Gets the base_path of this FullVirtualServiceAllOf.  # noqa: E501


        :return: The base_path of this FullVirtualServiceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this FullVirtualServiceAllOf.


        :param base_path: The base_path of this FullVirtualServiceAllOf.  # noqa: E501
        :type: str
        """

        self._base_path = base_path

    @property
    def port_string(self):
        """Gets the port_string of this FullVirtualServiceAllOf.  # noqa: E501


        :return: The port_string of this FullVirtualServiceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._port_string

    @port_string.setter
    def port_string(self, port_string):
        """Sets the port_string of this FullVirtualServiceAllOf.


        :param port_string: The port_string of this FullVirtualServiceAllOf.  # noqa: E501
        :type: str
        """

        self._port_string = port_string

    @property
    def service_image_file(self):
        """Gets the service_image_file of this FullVirtualServiceAllOf.  # noqa: E501


        :return: The service_image_file of this FullVirtualServiceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._service_image_file

    @service_image_file.setter
    def service_image_file(self, service_image_file):
        """Sets the service_image_file of this FullVirtualServiceAllOf.


        :param service_image_file: The service_image_file of this FullVirtualServiceAllOf.  # noqa: E501
        :type: str
        """

        self._service_image_file = service_image_file

    @property
    def service_model_file(self):
        """Gets the service_model_file of this FullVirtualServiceAllOf.  # noqa: E501


        :return: The service_model_file of this FullVirtualServiceAllOf.  # noqa: E501
        :rtype: str
        """
        return self._service_model_file

    @service_model_file.setter
    def service_model_file(self, service_model_file):
        """Sets the service_model_file of this FullVirtualServiceAllOf.


        :param service_model_file: The service_model_file of this FullVirtualServiceAllOf.  # noqa: E501
        :type: str
        """

        self._service_model_file = service_model_file

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
        if not isinstance(other, FullVirtualServiceAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullVirtualServiceAllOf):
            return True

        return self.to_dict() != other.to_dict()
