# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class AzureCloudSpaceRequest(object):
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
        'nat_image_reference': 'ImageReferenceDTO',
        'nat_instance_type': 'str'
    }

    attribute_map = {
        'nat_image_reference': 'natImageReference',
        'nat_instance_type': 'natInstanceType'
    }

    def __init__(self, nat_image_reference=None, nat_instance_type=None, local_vars_configuration=None):  # noqa: E501
        """AzureCloudSpaceRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nat_image_reference = None
        self._nat_instance_type = None
        self.discriminator = None

        self.nat_image_reference = nat_image_reference
        self.nat_instance_type = nat_instance_type

    @property
    def nat_image_reference(self):
        """Gets the nat_image_reference of this AzureCloudSpaceRequest.  # noqa: E501


        :return: The nat_image_reference of this AzureCloudSpaceRequest.  # noqa: E501
        :rtype: ImageReferenceDTO
        """
        return self._nat_image_reference

    @nat_image_reference.setter
    def nat_image_reference(self, nat_image_reference):
        """Sets the nat_image_reference of this AzureCloudSpaceRequest.


        :param nat_image_reference: The nat_image_reference of this AzureCloudSpaceRequest.  # noqa: E501
        :type: ImageReferenceDTO
        """
        if self.local_vars_configuration.client_side_validation and nat_image_reference is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_image_reference`, must not be `None`")  # noqa: E501

        self._nat_image_reference = nat_image_reference

    @property
    def nat_instance_type(self):
        """Gets the nat_instance_type of this AzureCloudSpaceRequest.  # noqa: E501


        :return: The nat_instance_type of this AzureCloudSpaceRequest.  # noqa: E501
        :rtype: str
        """
        return self._nat_instance_type

    @nat_instance_type.setter
    def nat_instance_type(self, nat_instance_type):
        """Sets the nat_instance_type of this AzureCloudSpaceRequest.


        :param nat_instance_type: The nat_instance_type of this AzureCloudSpaceRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and nat_instance_type is None:  # noqa: E501
            raise ValueError("Invalid value for `nat_instance_type`, must not be `None`")  # noqa: E501

        self._nat_instance_type = nat_instance_type

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
        if not isinstance(other, AzureCloudSpaceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AzureCloudSpaceRequest):
            return True

        return self.to_dict() != other.to_dict()
