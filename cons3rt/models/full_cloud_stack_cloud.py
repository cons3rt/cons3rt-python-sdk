# coding: utf-8

"""
cons3rt - Copyright Jackpine Technologies Corp.

NOTE: This file is auto-generated. Do not edit the file manually.
"""


import pprint
import re  # noqa: F401

import six

from cons3rt.configuration import Configuration


class FullCloudStackCloud(object):
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
        'hostname': 'str',
        'port': 'int',
        'protocol': 'str',
        'secret_access_key': 'str'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'hostname': 'hostname',
        'port': 'port',
        'protocol': 'protocol',
        'secret_access_key': 'secretAccessKey'
    }

    def __init__(self, access_key=None, hostname=None, port=None, protocol=None, secret_access_key=None, local_vars_configuration=None):  # noqa: E501
        """FullCloudStackCloud - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._access_key = None
        self._hostname = None
        self._port = None
        self._protocol = None
        self._secret_access_key = None
        self.discriminator = None

        self.access_key = access_key
        self.hostname = hostname
        self.port = port
        self.protocol = protocol
        self.secret_access_key = secret_access_key

    @property
    def access_key(self):
        """Gets the access_key of this FullCloudStackCloud.  # noqa: E501


        :return: The access_key of this FullCloudStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this FullCloudStackCloud.


        :param access_key: The access_key of this FullCloudStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `access_key`, must not be `None`")  # noqa: E501

        self._access_key = access_key

    @property
    def hostname(self):
        """Gets the hostname of this FullCloudStackCloud.  # noqa: E501


        :return: The hostname of this FullCloudStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this FullCloudStackCloud.


        :param hostname: The hostname of this FullCloudStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hostname is None:  # noqa: E501
            raise ValueError("Invalid value for `hostname`, must not be `None`")  # noqa: E501

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this FullCloudStackCloud.  # noqa: E501


        :return: The port of this FullCloudStackCloud.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this FullCloudStackCloud.


        :param port: The port of this FullCloudStackCloud.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and port is None:  # noqa: E501
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this FullCloudStackCloud.  # noqa: E501


        :return: The protocol of this FullCloudStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FullCloudStackCloud.


        :param protocol: The protocol of this FullCloudStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and protocol is None:  # noqa: E501
            raise ValueError("Invalid value for `protocol`, must not be `None`")  # noqa: E501

        self._protocol = protocol

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this FullCloudStackCloud.  # noqa: E501


        :return: The secret_access_key of this FullCloudStackCloud.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this FullCloudStackCloud.


        :param secret_access_key: The secret_access_key of this FullCloudStackCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and secret_access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `secret_access_key`, must not be `None`")  # noqa: E501

        self._secret_access_key = secret_access_key

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
        if not isinstance(other, FullCloudStackCloud):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullCloudStackCloud):
            return True

        return self.to_dict() != other.to_dict()
