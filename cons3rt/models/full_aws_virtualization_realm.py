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


class FullAwsVirtualizationRealm(object):
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
        'nat_image_id': 'str',
        'nat_instance_type': 'str',
        'nat_key_name': 'str',
        'nat_key_pem': 'str',
        'region': 'str',
        'security_group_id': 'str',
        'user_key_name': 'str',
        'user_key_pem': 'str',
        'virtual_network_name': 'str',
        'vpc_id': 'str',
        'vpc_subnet_name': 'str'
    }

    attribute_map = {
        'nat_image_id': 'natImageId',
        'nat_instance_type': 'natInstanceType',
        'nat_key_name': 'natKeyName',
        'nat_key_pem': 'natKeyPem',
        'region': 'region',
        'security_group_id': 'securityGroupId',
        'user_key_name': 'userKeyName',
        'user_key_pem': 'userKeyPem',
        'virtual_network_name': 'virtualNetworkName',
        'vpc_id': 'vpcId',
        'vpc_subnet_name': 'vpcSubnetName'
    }

    def __init__(self, nat_image_id=None, nat_instance_type=None, nat_key_name=None, nat_key_pem=None, region=None, security_group_id=None, user_key_name=None, user_key_pem=None, virtual_network_name=None, vpc_id=None, vpc_subnet_name=None, local_vars_configuration=None):  # noqa: E501
        """FullAwsVirtualizationRealm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._nat_image_id = None
        self._nat_instance_type = None
        self._nat_key_name = None
        self._nat_key_pem = None
        self._region = None
        self._security_group_id = None
        self._user_key_name = None
        self._user_key_pem = None
        self._virtual_network_name = None
        self._vpc_id = None
        self._vpc_subnet_name = None
        self.discriminator = None

        if nat_image_id is not None:
            self.nat_image_id = nat_image_id
        if nat_instance_type is not None:
            self.nat_instance_type = nat_instance_type
        if nat_key_name is not None:
            self.nat_key_name = nat_key_name
        if nat_key_pem is not None:
            self.nat_key_pem = nat_key_pem
        if region is not None:
            self.region = region
        if security_group_id is not None:
            self.security_group_id = security_group_id
        if user_key_name is not None:
            self.user_key_name = user_key_name
        if user_key_pem is not None:
            self.user_key_pem = user_key_pem
        if virtual_network_name is not None:
            self.virtual_network_name = virtual_network_name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if vpc_subnet_name is not None:
            self.vpc_subnet_name = vpc_subnet_name

    @property
    def nat_image_id(self):
        """Gets the nat_image_id of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The nat_image_id of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._nat_image_id

    @nat_image_id.setter
    def nat_image_id(self, nat_image_id):
        """Sets the nat_image_id of this FullAwsVirtualizationRealm.


        :param nat_image_id: The nat_image_id of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._nat_image_id = nat_image_id

    @property
    def nat_instance_type(self):
        """Gets the nat_instance_type of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The nat_instance_type of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._nat_instance_type

    @nat_instance_type.setter
    def nat_instance_type(self, nat_instance_type):
        """Sets the nat_instance_type of this FullAwsVirtualizationRealm.


        :param nat_instance_type: The nat_instance_type of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._nat_instance_type = nat_instance_type

    @property
    def nat_key_name(self):
        """Gets the nat_key_name of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The nat_key_name of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._nat_key_name

    @nat_key_name.setter
    def nat_key_name(self, nat_key_name):
        """Sets the nat_key_name of this FullAwsVirtualizationRealm.


        :param nat_key_name: The nat_key_name of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._nat_key_name = nat_key_name

    @property
    def nat_key_pem(self):
        """Gets the nat_key_pem of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The nat_key_pem of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._nat_key_pem

    @nat_key_pem.setter
    def nat_key_pem(self, nat_key_pem):
        """Sets the nat_key_pem of this FullAwsVirtualizationRealm.


        :param nat_key_pem: The nat_key_pem of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._nat_key_pem = nat_key_pem

    @property
    def region(self):
        """Gets the region of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The region of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this FullAwsVirtualizationRealm.


        :param region: The region of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def security_group_id(self):
        """Gets the security_group_id of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The security_group_id of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._security_group_id

    @security_group_id.setter
    def security_group_id(self, security_group_id):
        """Sets the security_group_id of this FullAwsVirtualizationRealm.


        :param security_group_id: The security_group_id of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._security_group_id = security_group_id

    @property
    def user_key_name(self):
        """Gets the user_key_name of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The user_key_name of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._user_key_name

    @user_key_name.setter
    def user_key_name(self, user_key_name):
        """Sets the user_key_name of this FullAwsVirtualizationRealm.


        :param user_key_name: The user_key_name of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._user_key_name = user_key_name

    @property
    def user_key_pem(self):
        """Gets the user_key_pem of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The user_key_pem of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._user_key_pem

    @user_key_pem.setter
    def user_key_pem(self, user_key_pem):
        """Sets the user_key_pem of this FullAwsVirtualizationRealm.


        :param user_key_pem: The user_key_pem of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._user_key_pem = user_key_pem

    @property
    def virtual_network_name(self):
        """Gets the virtual_network_name of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The virtual_network_name of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._virtual_network_name

    @virtual_network_name.setter
    def virtual_network_name(self, virtual_network_name):
        """Sets the virtual_network_name of this FullAwsVirtualizationRealm.


        :param virtual_network_name: The virtual_network_name of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._virtual_network_name = virtual_network_name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The vpc_id of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this FullAwsVirtualizationRealm.


        :param vpc_id: The vpc_id of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._vpc_id = vpc_id

    @property
    def vpc_subnet_name(self):
        """Gets the vpc_subnet_name of this FullAwsVirtualizationRealm.  # noqa: E501


        :return: The vpc_subnet_name of this FullAwsVirtualizationRealm.  # noqa: E501
        :rtype: str
        """
        return self._vpc_subnet_name

    @vpc_subnet_name.setter
    def vpc_subnet_name(self, vpc_subnet_name):
        """Sets the vpc_subnet_name of this FullAwsVirtualizationRealm.


        :param vpc_subnet_name: The vpc_subnet_name of this FullAwsVirtualizationRealm.  # noqa: E501
        :type: str
        """

        self._vpc_subnet_name = vpc_subnet_name

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
        if not isinstance(other, FullAwsVirtualizationRealm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullAwsVirtualizationRealm):
            return True

        return self.to_dict() != other.to_dict()
