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


class Metadata(object):
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
        'asset_directory': 'str',
        'version': 'int',
        'cloud': 'Cloud',
        'creation_date': 'int',
        'documentation': 'str',
        'id': 'int',
        'instance_limit': 'int',
        'itar_restricted': 'bool',
        'license': 'str',
        'modifier': 'User',
        'modifier_date': 'int',
        'properties': 'list[ModelProperty]',
        'uri': 'str',
        'validated': 'bool',
        'size_in_megabytes': 'int'
    }

    attribute_map = {
        'asset_directory': 'assetDirectory',
        'version': 'version',
        'cloud': 'cloud',
        'creation_date': 'creationDate',
        'documentation': 'documentation',
        'id': 'id',
        'instance_limit': 'instanceLimit',
        'itar_restricted': 'itarRestricted',
        'license': 'license',
        'modifier': 'modifier',
        'modifier_date': 'modifierDate',
        'properties': 'properties',
        'uri': 'uri',
        'validated': 'validated',
        'size_in_megabytes': 'sizeInMegabytes'
    }

    def __init__(self, asset_directory=None, version=None, cloud=None, creation_date=None, documentation=None, id=None, instance_limit=None, itar_restricted=None, license=None, modifier=None, modifier_date=None, properties=None, uri=None, validated=None, size_in_megabytes=None, local_vars_configuration=None):  # noqa: E501
        """Metadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_directory = None
        self._version = None
        self._cloud = None
        self._creation_date = None
        self._documentation = None
        self._id = None
        self._instance_limit = None
        self._itar_restricted = None
        self._license = None
        self._modifier = None
        self._modifier_date = None
        self._properties = None
        self._uri = None
        self._validated = None
        self._size_in_megabytes = None
        self.discriminator = None

        if asset_directory is not None:
            self.asset_directory = asset_directory
        if version is not None:
            self.version = version
        if cloud is not None:
            self.cloud = cloud
        if creation_date is not None:
            self.creation_date = creation_date
        if documentation is not None:
            self.documentation = documentation
        if id is not None:
            self.id = id
        if instance_limit is not None:
            self.instance_limit = instance_limit
        if itar_restricted is not None:
            self.itar_restricted = itar_restricted
        if license is not None:
            self.license = license
        if modifier is not None:
            self.modifier = modifier
        if modifier_date is not None:
            self.modifier_date = modifier_date
        if properties is not None:
            self.properties = properties
        if uri is not None:
            self.uri = uri
        if validated is not None:
            self.validated = validated
        if size_in_megabytes is not None:
            self.size_in_megabytes = size_in_megabytes

    @property
    def asset_directory(self):
        """Gets the asset_directory of this Metadata.  # noqa: E501


        :return: The asset_directory of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._asset_directory

    @asset_directory.setter
    def asset_directory(self, asset_directory):
        """Sets the asset_directory of this Metadata.


        :param asset_directory: The asset_directory of this Metadata.  # noqa: E501
        :type: str
        """

        self._asset_directory = asset_directory

    @property
    def version(self):
        """Gets the version of this Metadata.  # noqa: E501


        :return: The version of this Metadata.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Metadata.


        :param version: The version of this Metadata.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def cloud(self):
        """Gets the cloud of this Metadata.  # noqa: E501


        :return: The cloud of this Metadata.  # noqa: E501
        :rtype: Cloud
        """
        return self._cloud

    @cloud.setter
    def cloud(self, cloud):
        """Sets the cloud of this Metadata.


        :param cloud: The cloud of this Metadata.  # noqa: E501
        :type: Cloud
        """

        self._cloud = cloud

    @property
    def creation_date(self):
        """Gets the creation_date of this Metadata.  # noqa: E501


        :return: The creation_date of this Metadata.  # noqa: E501
        :rtype: int
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Metadata.


        :param creation_date: The creation_date of this Metadata.  # noqa: E501
        :type: int
        """

        self._creation_date = creation_date

    @property
    def documentation(self):
        """Gets the documentation of this Metadata.  # noqa: E501


        :return: The documentation of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._documentation

    @documentation.setter
    def documentation(self, documentation):
        """Sets the documentation of this Metadata.


        :param documentation: The documentation of this Metadata.  # noqa: E501
        :type: str
        """

        self._documentation = documentation

    @property
    def id(self):
        """Gets the id of this Metadata.  # noqa: E501


        :return: The id of this Metadata.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Metadata.


        :param id: The id of this Metadata.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def instance_limit(self):
        """Gets the instance_limit of this Metadata.  # noqa: E501


        :return: The instance_limit of this Metadata.  # noqa: E501
        :rtype: int
        """
        return self._instance_limit

    @instance_limit.setter
    def instance_limit(self, instance_limit):
        """Sets the instance_limit of this Metadata.


        :param instance_limit: The instance_limit of this Metadata.  # noqa: E501
        :type: int
        """

        self._instance_limit = instance_limit

    @property
    def itar_restricted(self):
        """Gets the itar_restricted of this Metadata.  # noqa: E501


        :return: The itar_restricted of this Metadata.  # noqa: E501
        :rtype: bool
        """
        return self._itar_restricted

    @itar_restricted.setter
    def itar_restricted(self, itar_restricted):
        """Sets the itar_restricted of this Metadata.


        :param itar_restricted: The itar_restricted of this Metadata.  # noqa: E501
        :type: bool
        """

        self._itar_restricted = itar_restricted

    @property
    def license(self):
        """Gets the license of this Metadata.  # noqa: E501


        :return: The license of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this Metadata.


        :param license: The license of this Metadata.  # noqa: E501
        :type: str
        """

        self._license = license

    @property
    def modifier(self):
        """Gets the modifier of this Metadata.  # noqa: E501


        :return: The modifier of this Metadata.  # noqa: E501
        :rtype: User
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this Metadata.


        :param modifier: The modifier of this Metadata.  # noqa: E501
        :type: User
        """

        self._modifier = modifier

    @property
    def modifier_date(self):
        """Gets the modifier_date of this Metadata.  # noqa: E501


        :return: The modifier_date of this Metadata.  # noqa: E501
        :rtype: int
        """
        return self._modifier_date

    @modifier_date.setter
    def modifier_date(self, modifier_date):
        """Sets the modifier_date of this Metadata.


        :param modifier_date: The modifier_date of this Metadata.  # noqa: E501
        :type: int
        """

        self._modifier_date = modifier_date

    @property
    def properties(self):
        """Gets the properties of this Metadata.  # noqa: E501


        :return: The properties of this Metadata.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Metadata.


        :param properties: The properties of this Metadata.  # noqa: E501
        :type: list[ModelProperty]
        """

        self._properties = properties

    @property
    def uri(self):
        """Gets the uri of this Metadata.  # noqa: E501


        :return: The uri of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Metadata.


        :param uri: The uri of this Metadata.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def validated(self):
        """Gets the validated of this Metadata.  # noqa: E501


        :return: The validated of this Metadata.  # noqa: E501
        :rtype: bool
        """
        return self._validated

    @validated.setter
    def validated(self, validated):
        """Sets the validated of this Metadata.


        :param validated: The validated of this Metadata.  # noqa: E501
        :type: bool
        """

        self._validated = validated

    @property
    def size_in_megabytes(self):
        """Gets the size_in_megabytes of this Metadata.  # noqa: E501


        :return: The size_in_megabytes of this Metadata.  # noqa: E501
        :rtype: int
        """
        return self._size_in_megabytes

    @size_in_megabytes.setter
    def size_in_megabytes(self, size_in_megabytes):
        """Sets the size_in_megabytes of this Metadata.


        :param size_in_megabytes: The size_in_megabytes of this Metadata.  # noqa: E501
        :type: int
        """

        self._size_in_megabytes = size_in_megabytes

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
        if not isinstance(other, Metadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Metadata):
            return True

        return self.to_dict() != other.to_dict()
