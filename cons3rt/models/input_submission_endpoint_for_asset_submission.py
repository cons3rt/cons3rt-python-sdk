# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class InputSubmissionEndpointForAssetSubmission(object):
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
        'port': 'int',
        'subtype': 'str'
    }

    attribute_map = {
        'port': 'port',
        'subtype': 'subtype'
    }

    discriminator_value_class_map = {
        'InputDockerRegistrySubmissionEndpointForAssetSubmission': 'InputDockerRegistrySubmissionEndpointForAssetSubmission',
        'InputSFTPSubmissionEndpointForAssetSubmission': 'InputSFTPSubmissionEndpointForAssetSubmission'
    }

    def __init__(self, port=None, subtype=None, local_vars_configuration=None):  # noqa: E501
        """InputSubmissionEndpointForAssetSubmission - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._port = None
        self._subtype = None
        self.discriminator = 'subtype'

        if port is not None:
            self.port = port
        self.subtype = subtype

    @property
    def port(self):
        """Gets the port of this InputSubmissionEndpointForAssetSubmission.  # noqa: E501


        :return: The port of this InputSubmissionEndpointForAssetSubmission.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InputSubmissionEndpointForAssetSubmission.


        :param port: The port of this InputSubmissionEndpointForAssetSubmission.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def subtype(self):
        """Gets the subtype of this InputSubmissionEndpointForAssetSubmission.  # noqa: E501


        :return: The subtype of this InputSubmissionEndpointForAssetSubmission.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this InputSubmissionEndpointForAssetSubmission.


        :param subtype: The subtype of this InputSubmissionEndpointForAssetSubmission.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, InputSubmissionEndpointForAssetSubmission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InputSubmissionEndpointForAssetSubmission):
            return True

        return self.to_dict() != other.to_dict()
