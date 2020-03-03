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


class AzureCloudResourcesAllOf(object):
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
        'images': 'list[ImageReferenceDTO]',
        'instance_types': 'list[str]'
    }

    attribute_map = {
        'images': 'images',
        'instance_types': 'instanceTypes'
    }

    def __init__(self, images=None, instance_types=None, local_vars_configuration=None):  # noqa: E501
        """AzureCloudResourcesAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._images = None
        self._instance_types = None
        self.discriminator = None

        if images is not None:
            self.images = images
        if instance_types is not None:
            self.instance_types = instance_types

    @property
    def images(self):
        """Gets the images of this AzureCloudResourcesAllOf.  # noqa: E501


        :return: The images of this AzureCloudResourcesAllOf.  # noqa: E501
        :rtype: list[ImageReferenceDTO]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this AzureCloudResourcesAllOf.


        :param images: The images of this AzureCloudResourcesAllOf.  # noqa: E501
        :type: list[ImageReferenceDTO]
        """

        self._images = images

    @property
    def instance_types(self):
        """Gets the instance_types of this AzureCloudResourcesAllOf.  # noqa: E501


        :return: The instance_types of this AzureCloudResourcesAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._instance_types

    @instance_types.setter
    def instance_types(self, instance_types):
        """Sets the instance_types of this AzureCloudResourcesAllOf.


        :param instance_types: The instance_types of this AzureCloudResourcesAllOf.  # noqa: E501
        :type: list[str]
        """

        self._instance_types = instance_types

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
        if not isinstance(other, AzureCloudResourcesAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureCloudResourcesAllOf):
            return True

        return self.to_dict() != other.to_dict()
