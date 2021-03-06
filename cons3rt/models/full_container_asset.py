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


class FullContainerAsset(object):
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
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'offline': 'bool',
        'state': 'str',
        'visibility': 'str',
        'creator': 'MinimalUser',
        'owning_project': 'MinimalProject',
        'trusted_projects': 'list[MinimalProject]',
        'dependent_asset_count': 'int',
        'metadata': 'FullMetadata',
        'impact_level': 'str',
        'categories': 'list[MinimalCategory]',
        'type': 'str',
        'image_file': 'str',
        'image_name': 'str',
        'image_tag': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'offline': 'offline',
        'state': 'state',
        'visibility': 'visibility',
        'creator': 'creator',
        'owning_project': 'owningProject',
        'trusted_projects': 'trustedProjects',
        'dependent_asset_count': 'dependentAssetCount',
        'metadata': 'metadata',
        'impact_level': 'impactLevel',
        'categories': 'categories',
        'type': 'type',
        'image_file': 'imageFile',
        'image_name': 'ImageName',
        'image_tag': 'imageTag'
    }

    def __init__(self, id=None, name=None, description=None, offline=None, state=None, visibility=None, creator=None, owning_project=None, trusted_projects=None, dependent_asset_count=None, metadata=None, impact_level=None, categories=None, type=None, image_file=None, image_name=None, image_tag=None, local_vars_configuration=None):  # noqa: E501
        """FullContainerAsset - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._description = None
        self._offline = None
        self._state = None
        self._visibility = None
        self._creator = None
        self._owning_project = None
        self._trusted_projects = None
        self._dependent_asset_count = None
        self._metadata = None
        self._impact_level = None
        self._categories = None
        self._type = None
        self._image_file = None
        self._image_name = None
        self._image_tag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if offline is not None:
            self.offline = offline
        if state is not None:
            self.state = state
        if visibility is not None:
            self.visibility = visibility
        if creator is not None:
            self.creator = creator
        if owning_project is not None:
            self.owning_project = owning_project
        if trusted_projects is not None:
            self.trusted_projects = trusted_projects
        if dependent_asset_count is not None:
            self.dependent_asset_count = dependent_asset_count
        if metadata is not None:
            self.metadata = metadata
        if impact_level is not None:
            self.impact_level = impact_level
        if categories is not None:
            self.categories = categories
        if type is not None:
            self.type = type
        if image_file is not None:
            self.image_file = image_file
        if image_name is not None:
            self.image_name = image_name
        if image_tag is not None:
            self.image_tag = image_tag

    @property
    def id(self):
        """Gets the id of this FullContainerAsset.  # noqa: E501


        :return: The id of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FullContainerAsset.


        :param id: The id of this FullContainerAsset.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FullContainerAsset.  # noqa: E501


        :return: The name of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FullContainerAsset.


        :param name: The name of this FullContainerAsset.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FullContainerAsset.  # noqa: E501


        :return: The description of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FullContainerAsset.


        :param description: The description of this FullContainerAsset.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def offline(self):
        """Gets the offline of this FullContainerAsset.  # noqa: E501


        :return: The offline of this FullContainerAsset.  # noqa: E501
        :rtype: bool
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this FullContainerAsset.


        :param offline: The offline of this FullContainerAsset.  # noqa: E501
        :type: bool
        """

        self._offline = offline

    @property
    def state(self):
        """Gets the state of this FullContainerAsset.  # noqa: E501


        :return: The state of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FullContainerAsset.


        :param state: The state of this FullContainerAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN_DEVELOPMENT", "CERTIFIED", "DEPRECATED", "RETIRED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def visibility(self):
        """Gets the visibility of this FullContainerAsset.  # noqa: E501


        :return: The visibility of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this FullContainerAsset.


        :param visibility: The visibility of this FullContainerAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["OWNER", "OWNING_PROJECT", "TRUSTED_PROJECTS", "COMMUNITY"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and visibility not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"  # noqa: E501
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def creator(self):
        """Gets the creator of this FullContainerAsset.  # noqa: E501


        :return: The creator of this FullContainerAsset.  # noqa: E501
        :rtype: MinimalUser
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this FullContainerAsset.


        :param creator: The creator of this FullContainerAsset.  # noqa: E501
        :type: MinimalUser
        """

        self._creator = creator

    @property
    def owning_project(self):
        """Gets the owning_project of this FullContainerAsset.  # noqa: E501


        :return: The owning_project of this FullContainerAsset.  # noqa: E501
        :rtype: MinimalProject
        """
        return self._owning_project

    @owning_project.setter
    def owning_project(self, owning_project):
        """Sets the owning_project of this FullContainerAsset.


        :param owning_project: The owning_project of this FullContainerAsset.  # noqa: E501
        :type: MinimalProject
        """

        self._owning_project = owning_project

    @property
    def trusted_projects(self):
        """Gets the trusted_projects of this FullContainerAsset.  # noqa: E501


        :return: The trusted_projects of this FullContainerAsset.  # noqa: E501
        :rtype: list[MinimalProject]
        """
        return self._trusted_projects

    @trusted_projects.setter
    def trusted_projects(self, trusted_projects):
        """Sets the trusted_projects of this FullContainerAsset.


        :param trusted_projects: The trusted_projects of this FullContainerAsset.  # noqa: E501
        :type: list[MinimalProject]
        """

        self._trusted_projects = trusted_projects

    @property
    def dependent_asset_count(self):
        """Gets the dependent_asset_count of this FullContainerAsset.  # noqa: E501


        :return: The dependent_asset_count of this FullContainerAsset.  # noqa: E501
        :rtype: int
        """
        return self._dependent_asset_count

    @dependent_asset_count.setter
    def dependent_asset_count(self, dependent_asset_count):
        """Sets the dependent_asset_count of this FullContainerAsset.


        :param dependent_asset_count: The dependent_asset_count of this FullContainerAsset.  # noqa: E501
        :type: int
        """

        self._dependent_asset_count = dependent_asset_count

    @property
    def metadata(self):
        """Gets the metadata of this FullContainerAsset.  # noqa: E501


        :return: The metadata of this FullContainerAsset.  # noqa: E501
        :rtype: FullMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FullContainerAsset.


        :param metadata: The metadata of this FullContainerAsset.  # noqa: E501
        :type: FullMetadata
        """

        self._metadata = metadata

    @property
    def impact_level(self):
        """Gets the impact_level of this FullContainerAsset.  # noqa: E501


        :return: The impact_level of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._impact_level

    @impact_level.setter
    def impact_level(self, impact_level):
        """Sets the impact_level of this FullContainerAsset.


        :param impact_level: The impact_level of this FullContainerAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "FEDRAMP_LOW", "FEDRAMP_MODERATE_DOD_LEVEL_2", "FEDRAMP_HIGH_DOD_LEVEL_4", "DOD_LEVEL_5", "DOD_LEVEL_6"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and impact_level not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `impact_level` ({0}), must be one of {1}"  # noqa: E501
                .format(impact_level, allowed_values)
            )

        self._impact_level = impact_level

    @property
    def categories(self):
        """Gets the categories of this FullContainerAsset.  # noqa: E501


        :return: The categories of this FullContainerAsset.  # noqa: E501
        :rtype: list[MinimalCategory]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this FullContainerAsset.


        :param categories: The categories of this FullContainerAsset.  # noqa: E501
        :type: list[MinimalCategory]
        """

        self._categories = categories

    @property
    def type(self):
        """Gets the type of this FullContainerAsset.  # noqa: E501


        :return: The type of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FullContainerAsset.


        :param type: The type of this FullContainerAsset.  # noqa: E501
        :type: str
        """
        allowed_values = ["DOCKER", "OCI"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def image_file(self):
        """Gets the image_file of this FullContainerAsset.  # noqa: E501


        :return: The image_file of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._image_file

    @image_file.setter
    def image_file(self, image_file):
        """Sets the image_file of this FullContainerAsset.


        :param image_file: The image_file of this FullContainerAsset.  # noqa: E501
        :type: str
        """

        self._image_file = image_file

    @property
    def image_name(self):
        """Gets the image_name of this FullContainerAsset.  # noqa: E501


        :return: The image_name of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this FullContainerAsset.


        :param image_name: The image_name of this FullContainerAsset.  # noqa: E501
        :type: str
        """

        self._image_name = image_name

    @property
    def image_tag(self):
        """Gets the image_tag of this FullContainerAsset.  # noqa: E501


        :return: The image_tag of this FullContainerAsset.  # noqa: E501
        :rtype: str
        """
        return self._image_tag

    @image_tag.setter
    def image_tag(self, image_tag):
        """Sets the image_tag of this FullContainerAsset.


        :param image_tag: The image_tag of this FullContainerAsset.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, FullContainerAsset):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FullContainerAsset):
            return True

        return self.to_dict() != other.to_dict()
