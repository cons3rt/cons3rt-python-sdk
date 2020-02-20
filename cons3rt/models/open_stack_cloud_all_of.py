# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class OpenStackCloudAllOf(object):
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
        'domain_name': 'str',
        'keystone_hostname': 'str',
        'keystone_password': 'str',
        'keystone_port': 'int',
        'keystone_protocol': 'str',
        'keystone_username': 'str',
        'keystone_version': 'str',
        'nat_image_id': 'str',
        'nat_instance_type': 'str',
        'tenant': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domainName',
        'keystone_hostname': 'keystoneHostname',
        'keystone_password': 'keystonePassword',
        'keystone_port': 'keystonePort',
        'keystone_protocol': 'keystoneProtocol',
        'keystone_username': 'keystoneUsername',
        'keystone_version': 'keystoneVersion',
        'nat_image_id': 'natImageId',
        'nat_instance_type': 'natInstanceType',
        'tenant': 'tenant',
        'tenant_id': 'tenantId'
    }

    def __init__(self, domain_name=None, keystone_hostname=None, keystone_password=None, keystone_port=None, keystone_protocol=None, keystone_username=None, keystone_version=None, nat_image_id=None, nat_instance_type=None, tenant=None, tenant_id=None, local_vars_configuration=None):  # noqa: E501
        """OpenStackCloudAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._domain_name = None
        self._keystone_hostname = None
        self._keystone_password = None
        self._keystone_port = None
        self._keystone_protocol = None
        self._keystone_username = None
        self._keystone_version = None
        self._nat_image_id = None
        self._nat_instance_type = None
        self._tenant = None
        self._tenant_id = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if keystone_hostname is not None:
            self.keystone_hostname = keystone_hostname
        if keystone_password is not None:
            self.keystone_password = keystone_password
        if keystone_port is not None:
            self.keystone_port = keystone_port
        if keystone_protocol is not None:
            self.keystone_protocol = keystone_protocol
        if keystone_username is not None:
            self.keystone_username = keystone_username
        if keystone_version is not None:
            self.keystone_version = keystone_version
        if nat_image_id is not None:
            self.nat_image_id = nat_image_id
        if nat_instance_type is not None:
            self.nat_instance_type = nat_instance_type
        if tenant is not None:
            self.tenant = tenant
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def domain_name(self):
        """Gets the domain_name of this OpenStackCloudAllOf.  # noqa: E501


        :return: The domain_name of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this OpenStackCloudAllOf.


        :param domain_name: The domain_name of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def keystone_hostname(self):
        """Gets the keystone_hostname of this OpenStackCloudAllOf.  # noqa: E501


        :return: The keystone_hostname of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._keystone_hostname

    @keystone_hostname.setter
    def keystone_hostname(self, keystone_hostname):
        """Sets the keystone_hostname of this OpenStackCloudAllOf.


        :param keystone_hostname: The keystone_hostname of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._keystone_hostname = keystone_hostname

    @property
    def keystone_password(self):
        """Gets the keystone_password of this OpenStackCloudAllOf.  # noqa: E501


        :return: The keystone_password of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._keystone_password

    @keystone_password.setter
    def keystone_password(self, keystone_password):
        """Sets the keystone_password of this OpenStackCloudAllOf.


        :param keystone_password: The keystone_password of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._keystone_password = keystone_password

    @property
    def keystone_port(self):
        """Gets the keystone_port of this OpenStackCloudAllOf.  # noqa: E501


        :return: The keystone_port of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: int
        """
        return self._keystone_port

    @keystone_port.setter
    def keystone_port(self, keystone_port):
        """Sets the keystone_port of this OpenStackCloudAllOf.


        :param keystone_port: The keystone_port of this OpenStackCloudAllOf.  # noqa: E501
        :type: int
        """

        self._keystone_port = keystone_port

    @property
    def keystone_protocol(self):
        """Gets the keystone_protocol of this OpenStackCloudAllOf.  # noqa: E501


        :return: The keystone_protocol of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._keystone_protocol

    @keystone_protocol.setter
    def keystone_protocol(self, keystone_protocol):
        """Sets the keystone_protocol of this OpenStackCloudAllOf.


        :param keystone_protocol: The keystone_protocol of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._keystone_protocol = keystone_protocol

    @property
    def keystone_username(self):
        """Gets the keystone_username of this OpenStackCloudAllOf.  # noqa: E501


        :return: The keystone_username of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._keystone_username

    @keystone_username.setter
    def keystone_username(self, keystone_username):
        """Sets the keystone_username of this OpenStackCloudAllOf.


        :param keystone_username: The keystone_username of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._keystone_username = keystone_username

    @property
    def keystone_version(self):
        """Gets the keystone_version of this OpenStackCloudAllOf.  # noqa: E501


        :return: The keystone_version of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._keystone_version

    @keystone_version.setter
    def keystone_version(self, keystone_version):
        """Sets the keystone_version of this OpenStackCloudAllOf.


        :param keystone_version: The keystone_version of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._keystone_version = keystone_version

    @property
    def nat_image_id(self):
        """Gets the nat_image_id of this OpenStackCloudAllOf.  # noqa: E501


        :return: The nat_image_id of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._nat_image_id

    @nat_image_id.setter
    def nat_image_id(self, nat_image_id):
        """Sets the nat_image_id of this OpenStackCloudAllOf.


        :param nat_image_id: The nat_image_id of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._nat_image_id = nat_image_id

    @property
    def nat_instance_type(self):
        """Gets the nat_instance_type of this OpenStackCloudAllOf.  # noqa: E501


        :return: The nat_instance_type of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._nat_instance_type

    @nat_instance_type.setter
    def nat_instance_type(self, nat_instance_type):
        """Sets the nat_instance_type of this OpenStackCloudAllOf.


        :param nat_instance_type: The nat_instance_type of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._nat_instance_type = nat_instance_type

    @property
    def tenant(self):
        """Gets the tenant of this OpenStackCloudAllOf.  # noqa: E501


        :return: The tenant of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this OpenStackCloudAllOf.


        :param tenant: The tenant of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """

        self._tenant = tenant

    @property
    def tenant_id(self):
        """Gets the tenant_id of this OpenStackCloudAllOf.  # noqa: E501


        :return: The tenant_id of this OpenStackCloudAllOf.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this OpenStackCloudAllOf.


        :param tenant_id: The tenant_id of this OpenStackCloudAllOf.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) > 255):
            raise ValueError("Invalid value for `tenant_id`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tenant_id is not None and len(tenant_id) < 1):
            raise ValueError("Invalid value for `tenant_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._tenant_id = tenant_id

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
        if not isinstance(other, OpenStackCloudAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenStackCloudAllOf):
            return True

        return self.to_dict() != other.to_dict()
