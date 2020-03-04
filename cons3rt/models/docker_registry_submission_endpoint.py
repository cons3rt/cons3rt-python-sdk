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


class DockerRegistrySubmissionEndpoint(object):
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
        'host': 'str',
        'id': 'int',
        'port': 'int',
        'type': 'str',
        'subtype': 'str',
        'image_name': 'str',
        'image_tag': 'str'
    }

    attribute_map = {
        'host': 'host',
        'id': 'id',
        'port': 'port',
        'type': 'type',
        'subtype': 'subtype',
        'image_name': 'imageName',
        'image_tag': 'imageTag'
    }

    def __init__(self, host=None, id=None, port=None, type=None, subtype=None, image_name=None, image_tag=None, local_vars_configuration=None):  # noqa: E501
        """DockerRegistrySubmissionEndpoint - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._host = None
        self._id = None
        self._port = None
        self._type = None
        self._subtype = None
        self._image_name = None
        self._image_tag = None
        self.discriminator = None

        self.host = host
        if id is not None:
            self.id = id
        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        self.subtype = subtype
        self.image_name = image_name
        self.image_tag = image_tag

    @property
    def host(self):
        """Gets the host of this DockerRegistrySubmissionEndpoint.  # noqa: E501


        :return: The host of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this DockerRegistrySubmissionEndpoint.


        :param host: The host of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and host is None:  # noqa: E501
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def id(self):
        """Gets the id of this DockerRegistrySubmissionEndpoint.  # noqa: E501


        :return: The id of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DockerRegistrySubmissionEndpoint.


        :param id: The id of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def port(self):
        """Gets the port of this DockerRegistrySubmissionEndpoint.  # noqa: E501


        :return: The port of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this DockerRegistrySubmissionEndpoint.


        :param port: The port of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def type(self):
        """Gets the type of this DockerRegistrySubmissionEndpoint.  # noqa: E501


        :return: The type of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DockerRegistrySubmissionEndpoint.


        :param type: The type of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :type: str
        """
        allowed_values = ["DockerRegistryEndpoint", "SFTPEndpoint"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def subtype(self):
        """Gets the subtype of this DockerRegistrySubmissionEndpoint.  # noqa: E501


        :return: The subtype of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._subtype

    @subtype.setter
    def subtype(self, subtype):
        """Sets the subtype of this DockerRegistrySubmissionEndpoint.


        :param subtype: The subtype of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `subtype`, must not be `None`")  # noqa: E501

        self._subtype = subtype

    @property
    def image_name(self):
        """Gets the image_name of this DockerRegistrySubmissionEndpoint.  # noqa: E501


        :return: The image_name of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this DockerRegistrySubmissionEndpoint.


        :param image_name: The image_name of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image_name is None:  # noqa: E501
            raise ValueError("Invalid value for `image_name`, must not be `None`")  # noqa: E501

        self._image_name = image_name

    @property
    def image_tag(self):
        """Gets the image_tag of this DockerRegistrySubmissionEndpoint.  # noqa: E501


        :return: The image_tag of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this DockerRegistrySubmissionEndpoint.


        :param image_tag: The image_tag of this DockerRegistrySubmissionEndpoint.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and image_tag is None:  # noqa: E501
            raise ValueError("Invalid value for `image_tag`, must not be `None`")  # noqa: E501

        self._image_tag = image_tag

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
        if not isinstance(other, DockerRegistrySubmissionEndpoint):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerRegistrySubmissionEndpoint):
            return True

        return self.to_dict() != other.to_dict()
