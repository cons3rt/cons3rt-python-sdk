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


class OpenStackClient(object):
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
        'username': 'str',
        'password': 'str',
        'accept_all_certs': 'bool',
        'accept_self_signed_certs': 'bool',
        'host': 'str',
        'port': 'int',
        'protocol': 'str',
        'subtype': 'str',
        'keystone_version': 'str',
        'tenant_name': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'accept_all_certs': 'acceptAllCerts',
        'accept_self_signed_certs': 'acceptSelfSignedCerts',
        'host': 'host',
        'port': 'port',
        'protocol': 'protocol',
        'subtype': 'subtype',
        'keystone_version': 'keystoneVersion',
        'tenant_name': 'tenantName'
    }

    def __init__(self, username=None, password=None, accept_all_certs=None, accept_self_signed_certs=None, host=None, port=None, protocol=None, subtype=None, keystone_version=None, tenant_name=None, local_vars_configuration=None):  # noqa: E501
        """OpenStackClient - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._username = None
        self._password = None
        self._accept_all_certs = None
        self._accept_self_signed_certs = None
        self._host = None
        self._port = None
        self._protocol = None
        self._subtype = None
        self._keystone_version = None
        self._tenant_name = None
        self.discriminator = None

        self.username = username
        self.password = password
        if accept_all_certs is not None:
            self.accept_all_certs = accept_all_certs
        if accept_self_signed_certs is not None:
            self.accept_self_signed_certs = accept_self_signed_certs
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        self.subtype = subtype
        if keystone_version is not None:
            self.keystone_version = keystone_version
        if tenant_name is not None:
            self.tenant_name = tenant_name

    @property
    def username(self):
        """Gets the username of this OpenStackClient.  # noqa: E501


        :return: The username of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this OpenStackClient.


        :param username: The username of this OpenStackClient.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and username is None:  # noqa: E501
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def password(self):
        """Gets the password of this OpenStackClient.  # noqa: E501


        :return: The password of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this OpenStackClient.


        :param password: The password of this OpenStackClient.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and password is None:  # noqa: E501
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def accept_all_certs(self):
        """Gets the accept_all_certs of this OpenStackClient.  # noqa: E501


        :return: The accept_all_certs of this OpenStackClient.  # noqa: E501
        :rtype: bool
        """
        return self._accept_all_certs

    @accept_all_certs.setter
    def accept_all_certs(self, accept_all_certs):
        """Sets the accept_all_certs of this OpenStackClient.


        :param accept_all_certs: The accept_all_certs of this OpenStackClient.  # noqa: E501
        :type: bool
        """

        self._accept_all_certs = accept_all_certs

    @property
    def accept_self_signed_certs(self):
        """Gets the accept_self_signed_certs of this OpenStackClient.  # noqa: E501


        :return: The accept_self_signed_certs of this OpenStackClient.  # noqa: E501
        :rtype: bool
        """
        return self._accept_self_signed_certs

    @accept_self_signed_certs.setter
    def accept_self_signed_certs(self, accept_self_signed_certs):
        """Sets the accept_self_signed_certs of this OpenStackClient.


        :param accept_self_signed_certs: The accept_self_signed_certs of this OpenStackClient.  # noqa: E501
        :type: bool
        """

        self._accept_self_signed_certs = accept_self_signed_certs

    @property
    def host(self):
        """Gets the host of this OpenStackClient.  # noqa: E501


        :return: The host of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this OpenStackClient.


        :param host: The host of this OpenStackClient.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this OpenStackClient.  # noqa: E501


        :return: The port of this OpenStackClient.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this OpenStackClient.


        :param port: The port of this OpenStackClient.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this OpenStackClient.  # noqa: E501


        :return: The protocol of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this OpenStackClient.


        :param protocol: The protocol of this OpenStackClient.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def subtype(self):
        """Gets the subtype of this OpenStackClient.  # noqa: E501


        :return: The subtype of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this OpenStackClient.


        :param subtype: The subtype of this OpenStackClient.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def keystone_version(self):
        """Gets the keystone_version of this OpenStackClient.  # noqa: E501


        :return: The keystone_version of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._keystone_version

    @keystone_version.setter
    def keystone_version(self, keystone_version):
        """Sets the keystone_version of this OpenStackClient.


        :param keystone_version: The keystone_version of this OpenStackClient.  # noqa: E501
        :type: str
        """

        self._keystone_version = keystone_version

    @property
    def tenant_name(self):
        """Gets the tenant_name of this OpenStackClient.  # noqa: E501


        :return: The tenant_name of this OpenStackClient.  # noqa: E501
        :rtype: str
        """
        return self._tenant_name

    @tenant_name.setter
    def tenant_name(self, tenant_name):
        """Sets the tenant_name of this OpenStackClient.


        :param tenant_name: The tenant_name of this OpenStackClient.  # noqa: E501
        :type: str
        """

        self._tenant_name = tenant_name

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
        if not isinstance(other, OpenStackClient):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OpenStackClient):
            return True

        return self.to_dict() != other.to_dict()
