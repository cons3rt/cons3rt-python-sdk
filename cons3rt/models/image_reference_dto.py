# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class ImageReferenceDTO(object):
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
        'publisher': 'str',
        'type': 'str',
        'image_version': 'str'
    }

    attribute_map = {
        'publisher': 'publisher',
        'type': 'type',
        'image_version': 'imageVersion'
    }

    def __init__(self, publisher=None, type=None, image_version=None, local_vars_configuration=None):  # noqa: E501
        """ImageReferenceDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._publisher = None
        self._type = None
        self._image_version = None
        self.discriminator = None

        self.publisher = publisher
        self.type = type
        self.image_version = image_version

    @property
    def publisher(self):
        """Gets the publisher of this ImageReferenceDTO.  # noqa: E501


        :return: The publisher of this ImageReferenceDTO.  # noqa: E501
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this ImageReferenceDTO.


        :param publisher: The publisher of this ImageReferenceDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and publisher is None:  # noqa: E501
            raise ValueError("Invalid value for `publisher`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                publisher is not None and len(publisher) > 255):
            raise ValueError("Invalid value for `publisher`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                publisher is not None and len(publisher) < 0):
            raise ValueError("Invalid value for `publisher`, length must be greater than or equal to `0`")  # noqa: E501

        self._publisher = publisher

    @property
    def type(self):
        """Gets the type of this ImageReferenceDTO.  # noqa: E501


        :return: The type of this ImageReferenceDTO.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageReferenceDTO.


        :param type: The type of this ImageReferenceDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) > 255):
            raise ValueError("Invalid value for `type`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 0):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `0`")  # noqa: E501

        self._type = type

    @property
    def image_version(self):
        """Gets the image_version of this ImageReferenceDTO.  # noqa: E501


        :return: The image_version of this ImageReferenceDTO.  # noqa: E501
        :rtype: str
        """
        return self._image_version

    @image_version.setter
    def image_version(self, image_version):
        """Sets the image_version of this ImageReferenceDTO.


        :param image_version: The image_version of this ImageReferenceDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image_version is None:  # noqa: E501
            raise ValueError("Invalid value for `image_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_version is not None and len(image_version) > 255):
            raise ValueError("Invalid value for `image_version`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                image_version is not None and len(image_version) < 0):
            raise ValueError("Invalid value for `image_version`, length must be greater than or equal to `0`")  # noqa: E501

        self._image_version = image_version

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
        if not isinstance(other, ImageReferenceDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ImageReferenceDTO):
            return True

        return self.to_dict() != other.to_dict()
