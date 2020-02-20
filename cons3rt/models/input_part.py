# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputPart(object):
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
        'body_as_string': 'str',
        'media_type': 'InputPartMediaType',
        'headers': 'dict(str, list[str])',
        'content_type_from_message': 'bool'
    }

    attribute_map = {
        'body_as_string': 'bodyAsString',
        'media_type': 'mediaType',
        'headers': 'headers',
        'content_type_from_message': 'contentTypeFromMessage'
    }

    def __init__(self, body_as_string=None, media_type=None, headers=None, content_type_from_message=None, local_vars_configuration=None):  # noqa: E501
        """InputPart - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._body_as_string = None
        self._media_type = None
        self._headers = None
        self._content_type_from_message = None
        self.discriminator = None

        if body_as_string is not None:
            self.body_as_string = body_as_string
        if media_type is not None:
            self.media_type = media_type
        if headers is not None:
            self.headers = headers
        if content_type_from_message is not None:
            self.content_type_from_message = content_type_from_message

    @property
    def body_as_string(self):
        """Gets the body_as_string of this InputPart.  # noqa: E501


        :return: The body_as_string of this InputPart.  # noqa: E501
        :rtype: str
        """
        return self._body_as_string

    @body_as_string.setter
    def body_as_string(self, body_as_string):
        """Sets the body_as_string of this InputPart.


        :param body_as_string: The body_as_string of this InputPart.  # noqa: E501
        :type: str
        """

        self._body_as_string = body_as_string

    @property
    def media_type(self):
        """Gets the media_type of this InputPart.  # noqa: E501


        :return: The media_type of this InputPart.  # noqa: E501
        :rtype: InputPartMediaType
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this InputPart.


        :param media_type: The media_type of this InputPart.  # noqa: E501
        :type: InputPartMediaType
        """

        self._media_type = media_type

    @property
    def headers(self):
        """Gets the headers of this InputPart.  # noqa: E501


        :return: The headers of this InputPart.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this InputPart.


        :param headers: The headers of this InputPart.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._headers = headers

    @property
    def content_type_from_message(self):
        """Gets the content_type_from_message of this InputPart.  # noqa: E501


        :return: The content_type_from_message of this InputPart.  # noqa: E501
        :rtype: bool
        """
        return self._content_type_from_message

    @content_type_from_message.setter
    def content_type_from_message(self, content_type_from_message):
        """Sets the content_type_from_message of this InputPart.


        :param content_type_from_message: The content_type_from_message of this InputPart.  # noqa: E501
        :type: bool
        """

        self._content_type_from_message = content_type_from_message

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
        if not isinstance(other, InputPart):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputPart):
            return True

        return self.to_dict() != other.to_dict()
