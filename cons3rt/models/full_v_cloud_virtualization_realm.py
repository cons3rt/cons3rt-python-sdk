# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class FullVCloudVirtualizationRealm(object):
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
        'organization': 'str',
        'organization_vdc': 'str',
        'vdc_network_quota': 'int'
    }

    attribute_map = {
        'organization': 'organization',
        'organization_vdc': 'organizationVdc',
        'vdc_network_quota': 'vdcNetworkQuota'
    }

    def __init__(self, organization=None, organization_vdc=None, vdc_network_quota=None, local_vars_configuration=None):  # noqa: E501
        """FullVCloudVirtualizationRealm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._organization = None
        self._organization_vdc = None
        self._vdc_network_quota = None
        self.discriminator = None

        if organization is not None:
            self.organization = organization
        if organization_vdc is not None:
            self.organization_vdc = organization_vdc
        if vdc_network_quota is not None:
            self.vdc_network_quota = vdc_network_quota

    @property
    def organization(self):
        """Gets the organization of this FullVCloudVirtualizationRealm.  # noqa: E501


        :return: The organization of this FullVCloudVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this FullVCloudVirtualizationRealm.


        :param organization: The organization of this FullVCloudVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def organization_vdc(self):
        """Gets the organization_vdc of this FullVCloudVirtualizationRealm.  # noqa: E501


        :return: The organization_vdc of this FullVCloudVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._organization_vdc

    @organization_vdc.setter
    def organization_vdc(self, organization_vdc):
        """Sets the organization_vdc of this FullVCloudVirtualizationRealm.


        :param organization_vdc: The organization_vdc of this FullVCloudVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._organization_vdc = organization_vdc

    @property
    def vdc_network_quota(self):
        """Gets the vdc_network_quota of this FullVCloudVirtualizationRealm.  # noqa: E501


        :return: The vdc_network_quota of this FullVCloudVirtualizationRealm.  # noqa: E501
        :rtype: int
        """
        return self._vdc_network_quota

    @vdc_network_quota.setter
    def vdc_network_quota(self, vdc_network_quota):
        """Sets the vdc_network_quota of this FullVCloudVirtualizationRealm.


        :param vdc_network_quota: The vdc_network_quota of this FullVCloudVirtualizationRealm.  # noqa: E501
        :type: int
        """

        self._vdc_network_quota = vdc_network_quota

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
        if not isinstance(other, FullVCloudVirtualizationRealm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullVCloudVirtualizationRealm):
            return True

        return self.to_dict() != other.to_dict()
