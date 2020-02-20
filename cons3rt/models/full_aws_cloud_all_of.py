# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class FullAwsCloudAllOf(object):
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
        'access_key': 'str',
        'nat_image_id': 'str',
        'nat_instance_type': 'str',
        'owner_id': 'str',
        'region_name': 'str'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'nat_image_id': 'natImageId',
        'nat_instance_type': 'natInstanceType',
        'owner_id': 'ownerId',
        'region_name': 'regionName'
    }

    def __init__(self, access_key=None, nat_image_id=None, nat_instance_type=None, owner_id=None, region_name=None, local_vars_configuration=None):  # noqa: E501
        """FullAwsCloudAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key = None
        self._nat_image_id = None
        self._nat_instance_type = None
        self._owner_id = None
        self._region_name = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if nat_image_id is not None:
            self.nat_image_id = nat_image_id
        if nat_instance_type is not None:
            self.nat_instance_type = nat_instance_type
        if owner_id is not None:
            self.owner_id = owner_id
        if region_name is not None:
            self.region_name = region_name

    @property
    def access_key(self):
        """Gets the access_key of this FullAwsCloudAllOf.  # noqa: E501


        :return: The access_key of this FullAwsCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this FullAwsCloudAllOf.


        :param access_key: The access_key of this FullAwsCloudAllOf.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def nat_image_id(self):
        """Gets the nat_image_id of this FullAwsCloudAllOf.  # noqa: E501


        :return: The nat_image_id of this FullAwsCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._nat_image_id

    @nat_image_id.setter
    def nat_image_id(self, nat_image_id):
        """Sets the nat_image_id of this FullAwsCloudAllOf.


        :param nat_image_id: The nat_image_id of this FullAwsCloudAllOf.  # noqa: E501
        :type: str
        """

        self._nat_image_id = nat_image_id

    @property
    def nat_instance_type(self):
        """Gets the nat_instance_type of this FullAwsCloudAllOf.  # noqa: E501


        :return: The nat_instance_type of this FullAwsCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._nat_instance_type

    @nat_instance_type.setter
    def nat_instance_type(self, nat_instance_type):
        """Sets the nat_instance_type of this FullAwsCloudAllOf.


        :param nat_instance_type: The nat_instance_type of this FullAwsCloudAllOf.  # noqa: E501
        :type: str
        """

        self._nat_instance_type = nat_instance_type

    @property
    def owner_id(self):
        """Gets the owner_id of this FullAwsCloudAllOf.  # noqa: E501


        :return: The owner_id of this FullAwsCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this FullAwsCloudAllOf.


        :param owner_id: The owner_id of this FullAwsCloudAllOf.  # noqa: E501
        :type: str
        """

        self._owner_id = owner_id

    @property
    def region_name(self):
        """Gets the region_name of this FullAwsCloudAllOf.  # noqa: E501


        :return: The region_name of this FullAwsCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        """Sets the region_name of this FullAwsCloudAllOf.


        :param region_name: The region_name of this FullAwsCloudAllOf.  # noqa: E501
        :type: str
        """

        self._region_name = region_name

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
        if not isinstance(other, FullAwsCloudAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullAwsCloudAllOf):
            return True

        return self.to_dict() != other.to_dict()
