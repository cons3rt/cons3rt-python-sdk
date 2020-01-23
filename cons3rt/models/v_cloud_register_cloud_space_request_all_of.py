# coding: utf-8

"""
    CONS3RT API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@cons3rt.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class VCloudRegisterCloudSpaceRequestAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'local_storage_name': 'str',
        'organization': 'str',
        'organization_vdc': 'str'
    }

    attribute_map = {
        'local_storage_name': 'localStorageName',
        'organization': 'organization',
        'organization_vdc': 'organizationVdc'
    }

    def __init__(self, local_storage_name=None, organization=None, organization_vdc=None, local_vars_configuration=None):  # noqa: E501
        """VCloudRegisterCloudSpaceRequestAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._local_storage_name = None
        self._organization = None
        self._organization_vdc = None
        self.discriminator = None

        if local_storage_name is not None:
            self.local_storage_name = local_storage_name
        if organization is not None:
            self.organization = organization
        if organization_vdc is not None:
            self.organization_vdc = organization_vdc

    @property
    def local_storage_name(self):
        """Gets the local_storage_name of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501


        :return: The local_storage_name of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._local_storage_name

    @local_storage_name.setter
    def local_storage_name(self, local_storage_name):
        """Sets the local_storage_name of this VCloudRegisterCloudSpaceRequestAllOf.


        :param local_storage_name: The local_storage_name of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._local_storage_name = local_storage_name

    @property
    def organization(self):
        """Gets the organization of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501


        :return: The organization of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this VCloudRegisterCloudSpaceRequestAllOf.


        :param organization: The organization of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def organization_vdc(self):
        """Gets the organization_vdc of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501


        :return: The organization_vdc of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :rtype: str
        """
        return self._organization_vdc

    @organization_vdc.setter
    def organization_vdc(self, organization_vdc):
        """Sets the organization_vdc of this VCloudRegisterCloudSpaceRequestAllOf.


        :param organization_vdc: The organization_vdc of this VCloudRegisterCloudSpaceRequestAllOf.  # noqa: E501
        :type: str
        """

        self._organization_vdc = organization_vdc

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
        if not isinstance(other, VCloudRegisterCloudSpaceRequestAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VCloudRegisterCloudSpaceRequestAllOf):
            return True

        return self.to_dict() != other.to_dict()
